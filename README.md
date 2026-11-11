# NJU-beamer
这是一个NJU的beamer模板。此模板基于[SINTEF Presentation](https://www.overleaf.com/latex/templates/sintef-presentation/jhbhdffczpnx)。

模板的视觉风格已按南京大学版演示稿重做：整版主色标题页、页眉处的「章节序号 + 章节名」运行页眉、
页眉下方的主色分隔线、浅色信息面板与卡片、以及右下角的页码。所有学校通用 —— 配色随所选学校的主色自动适配。

这是我的第一个github项目，我并不熟悉git操作，欢迎批评指正。

## 视觉设计

| 元素 | 说明 |
| --- | --- |
| 标题页 | 整版主色底，校徽置于左上角，右侧为学校建筑插画（出血裁切） |
| 页眉 | 左上角主色细框校徽 + `NN 章节名` 运行页眉，下方一条主色粗横线 |
| 帧标题 | 位于分隔线下方的粗体主色引导句，可选副标题为灰色小字 |
| 页码 | 右下角两位补零的浅灰页码 |
| 章节页 | 主色斜向渐变底 + 右下角淡化的建筑线稿，当前章节高亮 |
| 子节页 | 与章节页同一套渐变底，左侧显示章节号与子节名 |
| 组件 | `\callout`、`\stat`、`\card`、`\keypoint` 四种浅色信息块 |

### 新增命令

```latex
\callout[小标题]{正文}          % 浅色面板 + 左侧主色竖条
\stat{标签}{数值}                 % 小卡片：主色标签 + 大号数值
\card{序号}{标题}{正文}           % 编号卡片
\keypoint{正文}                  % 空心箭头 + 粗体主色结论句
\thead{表头}                      % 粗体主色表头单元格
\zebra                            % 表格隔行浅色底纹（放在 tabular 之前）
```

代码块使用 `codepanel` 环境，它与正文栏严格对齐：

```latex
\begin{codepanel}{Python}
\begin{lstlisting}[language=Python]
print("hello")
\end{lstlisting}
\end{codepanel}
```

### 可重定义的宏

在 `\usepackage{collegeBeamer}` 之后用 `\renewcommand` 覆盖：

```latex
\renewcommand{\collegeMotto}{校训}      % 页脚口号（配合 \footlinecolor{主色}）
\renewcommand{\collegeRunningHead}{...}  % 页眉运行标题
\renewcommand{\collegeSectionNumber}{...}% 页眉中的章节序号
```

### 颜色

```latex
\color{maincolor}     % 学校主色
\color{mainlight}     % 浅色面板底（主色 8%）
\color{mainpaler}     % 更浅的底纹（主色 5%）
\color{mainrule}      % 细线与描边（主色 30%）
\color{inkcolor}      % 正文
\color{mutedcolor}    % 次要文字、页码
```

# 原readme文档 
Hi👋 Here are some beamer templates which are secondary creations of [SINTEF Presentation](https://www.overleaf.com/latex/templates/sintef-presentation/jhbhdffczpnx) template. Thanks [Federico Zenith](federico.zenith@sintef.no) for creating such well-designed works. To use it in my and my friends' schools/institutes, I rewrote and added some icons and features to adapt to specific surroundings✨.

## Colleges & institutes

- Nanjing University
![NJU](https://github.com/liu-qilong/college-beamer/blob/main/gallery/NJU.png?raw=true)
- The Hong Kong Polytechnic University
![PolyU](https://github.com/liu-qilong/college-beamer/blob/main/gallery/PolyU.png?raw=true)
- Southwest University
![SWU](https://github.com/liu-qilong/college-beamer/blob/main/gallery/SWU.png?raw=true)
- Shenzhen University
![SZU](https://github.com/liu-qilong/college-beamer/blob/main/gallery/SZU.png?raw=true)
- Shenzhen Academic of Environmental Science
![SAES](https://github.com/liu-qilong/college-beamer/blob/main/gallery/SAES.png?raw=true)
  > ⚠️ `src/SAES/background.png` is currently a copy of the PolyU drawing, so the
  > SAES cover shows the same artwork. Replace it with a real SAES landmark.
- Harbin Institute of Technology
![HIT](https://github.com/liu-qilong/college-beamer/blob/main/gallery/HIT.png?raw=true)
  > Thank [LeeWlving](https://github.com/LeeWlving) for contributing this template!
- Zhejiang A&F University
![ZAFU](https://github.com/liu-qilong/college-beamer/blob/main/gallery/ZAFU.png?raw=true)
  > Thank [ke1ewang](https://github.com/ke1ewang) for contributing this template!

Some of these templates have been submitted to [Overleaf](https://cs.overleaf.com/gallery), please check them here👇
- [The Honk Kong Polytechnic University (PolyU) Beamer Presentation Theme](https://www.overleaf.com/latex/templates/the-honk-kong-polytechnic-university-polyu-beamer-presentation-theme/vywngqprjwrq)
- [西南大学 SWU Beamer 模板](https://www.overleaf.com/latex/templates/xi-nan-da-xue-swu-beamer-mo-ban-zhu-ti/bgprxfbyhqsb)
- [深圳大学 SZU Beamer 模板](https://www.overleaf.com/latex/templates/shen-zhen-da-xue-szu-beamer-mo-ban/bjwzmkpsgygf)
- [深圳环境科学院 SAES Beamer 模版](https://www.overleaf.com/latex/templates/shen-zhen-huan-jing-ke-xue-yuan-saes-beamer-zhu-ti/gqfgpdwcrcpt)
- [哈尔滨工业大学 Beamer 模版](https://www.overleaf.com/latex/templates/harbin-institute-of-technology-hit-beamer-presentation-theme/prwxqwfdzkqj)
- [浙江农林大学 ZAFU Beamer 模版](https://www.overleaf.com/latex/templates/zafu-beamer-theme-beta/rcxzphbhnddf)

## Options & usage

### Switch college/institute

Switching between different college/institute is quite easy, just add college/institute name (all lower case) to the `collegeBeamer` package. For example, to switch to the PolyU theme, add `polyu` to the package:

```
\usepackage[polyu,en]{collegeBeamer}
```

### Switch language

To switch the language, just change the language option in the `collegeBeamer` package. For example, to switch to the Chinese language, add `zh` to the package:

```
\usepackage[szu,zh]{collegeBeamer}
```

> When `zh` is selected, Chinese text needs [XeLaTeX](https://www.overleaf.com/learn/latex/XeLaTeX)
> or LuaLaTeX. The package loads `xeCJK` (XeLaTeX) or `luatexja-fontspec`
> (LuaLaTeX) for you and picks the first available CJK family
> (Noto Sans/Serif CJK SC → Source Han Sans/Serif SC → Microsoft YaHei).
> You can still override the fonts yourself in the preamble:
>
> ```
> \setCJKmainfont{Source Han Serif SC}
> \setCJKsansfont{Source Han Sans SC}
> ```

### Logo style

By default the outlined (`trans-logo.png`) badge is used, which matches the
reference design. To use the solid colour tile (`color-logo.png`) instead, add
the `logo=color` option:

```
\usepackage[nju,zh,logo=color]{collegeBeamer}
```

### Page elements

- Cover page

  A solid main-colour cover with the badge, the title block and the campus artwork bleeding off the right edge.
- Section divider

  At the beginning of each section: a diagonal main-colour gradient, the campus line drawing faded into the
  bottom-right corner, and the table of contents with the current chapter highlighted.
- Running header

  Every content slide repeats the section number and name, with the accent rule underneath.
- Sub-section page

  The same gradient as the section divider, with the section and sub-section names on the left.
- Math equation
- Code block
- End page

  The gradient again, without the corner artwork so it cannot clash with the centred text.

### Compiling the demo

`pre.tex` is a Chinese demo that exercises every component of the template.
Compile it with XeLaTeX or LuaLaTeX (twice, so that the table of contents is
complete):

```
xelatex pre.tex
xelatex pre.tex
```

## Add your own college?

Would like to make your own theme on top of these themes? It's quite easy, only a few steps are needed:

### Step 1: Get the files

To get the files, you can fork & clone the repository to your computer.

Alternatively, you can open the templates' Overleaf webpages and click `Open as Template`.

### Step 2: Place logos and artwork

Create a subfolder under `src/` named as your college. Place `color-logo.png` (logo image with background color), `trans-logo.png` (logo image with transparent background), and `background.png` (a line drawing of a campus landmark) into it.

`background.png` is converted into the cover artwork by
`tools/make_title_art.py`, which turns the drawing into white ink on a
transparent background so it reads on the solid colour cover:

```
python tools/make_title_art.py          # every college
python tools/make_title_art.py NJU      # just one
```

The result is written to `src/<College>/art.png` (cover artwork) and
`src/<College>/sectionart.png` (a feathered, blurred copy used as the watermark
on the section dividers, so a drawing cropped out of a photograph dissolves
into the corner instead of showing a straight cut). Colourful artwork (such as
the `red` college's flag) is kept as it is.

If you would rather use your own colour collage on the cover, put the PNGs in
`src/<College>/art/` and override `\collegeTitleArt` in your college option.

### Step 3: Add college/institute option

All college/institute options are defined near the top of `collegebeamer.sty`. Add your college/institute name in the same format, e.g.:

```
\DeclareOption{polyu}{
  \renewcommand{\maincolorRGB}{128, 57, 61}  % the theme's main color in RGB
  \renewcommand{\colorlogoPath}{src/PolyU/color-logo.png}  % path to the logo image with background color
  \renewcommand{\translogoPath}{src/PolyU/trans-logo.png}  % path to the logo image with transparent background
  \renewcommand{\backgroundPath}{src/PolyU/background.png}  % path to the background image
  \renewcommand{\titleartPath}{src/PolyU/art.png}  % path to the cover artwork
}
```

Noted that the theme's main color will be used in the front-ground of titles and background colors of the sectional page.

> _P.S. You may also choose to use a logo with white background for `\translogoPath`. Please refer to [issue #8](https://github.com/liu-qilong/college-beamer/issues/8) for considerations._

Now you have your brand new template 👏🎉

## Issues & suggestions

If you have any revision suggestions, please create an issue in this repository. Thanks indeed🤝
