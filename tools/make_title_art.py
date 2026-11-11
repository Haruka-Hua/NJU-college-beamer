#!/usr/bin/env python3
"""Generate the title-page artwork used by ``collegeBeamer``.

Each college ships a ``background.png``: a black-and-white line drawing of a
campus landmark on a white sheet.  On the new (solid main-colour) title page
that white sheet is unusable, so this script converts every drawing into
"white ink on transparency", which reads well on any dark background.

    python tools/make_title_art.py            # regenerate every college
    python tools/make_title_art.py NJU PolyU  # only the listed colleges

The result is written to ``src/<College>/art.png`` (the cover artwork) and
``src/<College>/sectionart.png`` (a feathered, blurred copy used as the
watermark on the section dividers).

Colleges with a hand-made colour collage (NJU) use it on the title page and
keep it in ``src/<College>/art/``; run ``--optimise`` to shrink those PNGs.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps, ImageStat

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# Colleges whose *title page* uses a hand-made colour collage instead of the
# converted line drawing.  They still get a line-art version for the section
# pages, so they are not skipped by the generator.
COLLAGE = {"NJU"}


def mean_saturation(im: Image.Image) -> float:
    """Average HSV saturation over the opaque pixels of ``im``."""
    sat = im.convert("RGB").convert("HSV").getchannel("S")
    mask = im.getchannel("A").point(lambda v: 255 if v > 8 else 0)
    if not mask.getbbox():
        return 0.0
    return ImageStat.Stat(sat, mask).mean[0] / 255


def to_white_art(path: Path) -> Image.Image:
    """Turn a dark-ink-on-white drawing into white-ink-on-transparent.

    The existing alpha channel is respected and multiplied in, so the empty
    margins of the original file stay empty.
    """
    im = Image.open(path).convert("RGBA")
    red, green, blue, alpha = im.split()

    # Perceived brightness of the artwork; dark pixels are "ink".
    luma = Image.merge("RGB", (red, green, blue)).convert("L")

    # Ink density: 1 for black, 0 for white.  The gamma < 1 thickens the
    # strokes: a sparse line drawing then carries about as much visual
    # weight as a dense photograph when it is used as a watermark.
    ink = ImageOps.invert(luma).point(lambda v: int(255 * (v / 255) ** 0.62))

    out = Image.new("RGBA", im.size, (255, 255, 255, 0))
    out.putalpha(ImageChops.multiply(ink, alpha))
    return out


def crop_to_content(im: Image.Image, threshold: int = 4) -> Image.Image:
    """Trim fully transparent margins so the artwork can be positioned freely."""
    bbox = im.getchannel("A").point(lambda v: 255 if v > threshold else 0).getbbox()
    return im.crop(bbox) if bbox else im


def shrink(im: Image.Image) -> Image.Image:
    """Store white-on-transparent artwork as greyscale+alpha (much smaller).

    The drawing is pure white ink, so only the alpha channel carries
    information.  It is also quantised to 32 levels, which is
    indistinguishable at presentation size and roughly halves the file.
    """
    if im.mode == "RGBA":
        r, g, b, a = im.split()
        if r.getextrema() == (255, 255) and g.getextrema() == (255, 255) and b.getextrema() == (255, 255):
            a = a.point(lambda v: (v // 8) * 8)
            return Image.merge("LA", (a, a))
    return im


def make_watermark(art: Image.Image) -> Image.Image:
    """Soften the drawing so it can sit behind text as a watermark.

    Two things happen: the alpha is feathered towards the edges, so a
    drawing cropped out of a photograph no longer shows a straight cut,
    and the whole thing is blurred a little, which turns a hard
    thresholded photo into a soft tonal image.
    """
    im = art.convert("RGBA")
    w, h = im.size
    alpha = im.getchannel("A")

    # a ramp that is transparent at the border and opaque in the middle
    ramp = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(ramp)
    fx, fy = max(2, int(w * 0.14)), max(2, int(h * 0.14))
    draw.rectangle([fx, fy, w - fx - 1, h - fy - 1], fill=255)
    ramp = ramp.filter(ImageFilter.GaussianBlur(radius=max(1, min(fx, fy) // 3)))

    im.putalpha(ImageChops.multiply(alpha, ramp))
    return im.filter(ImageFilter.GaussianBlur(radius=max(1, min(w, h) // 250)))


def optimise_collages() -> int:
    """Shrink the hand-made colour collages without visible loss.

    A 192 colour palette with dithering cuts the PNGs to a quarter of their
    size; the illustrations are line art on flat washes, so the result is
    visually indistinguishable at presentation size.
    """
    for path in sorted(SRC.glob("*/art/*.png")):
        before = path.stat().st_size
        im = Image.open(path).convert("RGBA")
        im.quantize(
            colors=192, method=Image.FASTOCTREE, dither=Image.FLOYDSTEINBERG
        ).save(path, optimize=True)
        after = path.stat().st_size
        print(f"{path.relative_to(ROOT)}  {before // 1024} kB -> {after // 1024} kB")
    return 0


def main(argv: list[str]) -> int:
    if argv[1:2] == ["--optimise"]:
        return optimise_collages()
    colleges = argv[1:] or sorted(p.name for p in SRC.iterdir() if p.is_dir())
    for college in colleges:
        src = SRC / college / "background.png"
        if not src.is_file():
            print(f"skip {college}: no background.png", file=sys.stderr)
            continue
        original = Image.open(src).convert("RGBA")
        if mean_saturation(original) > 0.12:
            # Colourful artwork (e.g. the Red college's flag) already reads
            # well on a dark background -- keep it as it is.
            art = crop_to_content(original)
            kind = "colour"
        else:
            art = crop_to_content(to_white_art(src))
            kind = "line art"
        out = SRC / college / "art.png"
        shrink(art).save(out, optimize=True)
        print(f"wrote {out.relative_to(ROOT)}  ({art.width}x{art.height}, {kind})")

        # a softened copy for the section-divider watermark
        mark = SRC / college / "sectionart.png"
        shrink(make_watermark(art)).save(mark, optimize=True)
        print(f"wrote {mark.relative_to(ROOT)}  ({art.width}x{art.height}, watermark)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
