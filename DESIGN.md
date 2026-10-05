# Design system and authoring conventions

## 1. The collection standard (shared with Engineering Mathematics)

These values are identical in every book of the notes collection, so the books match in size and density
when placed side by side. They are set once, in `template/el-packages.tex`, `el-en.tex`/`el-fa.tex`
and `el-layout.tex`.

| | Value |
|---|---|
| Paper | A4, 210 × 297 mm |
| Margins | top 25 mm, bottom 24 mm, inner/outer 24 mm. Text block 162 × 247 mm |
| Running head | 15 pt high, 9 mm above the text. Folio 12 mm below the text, centred |
| Body | 11 pt (`article`), line spacing 1.08 (English) / 1.32 (Persian) |
| Text faces | TeX Gyre Termes (Times); TeX Gyre Heros for display; Vazirmatn for Persian |
| Mathematics | TeX Gyre Termes Math (Times-style), `unicode-math`. Variables italic, functions upright |
| Headings | section `\Large`, subsection `\large`, chapter title 25 pt, contents title 26 pt |
| Captions | `\small`. Footnotes use the class default |
| Paragraphs | no indent, 0.55 em between paragraphs |
| Displays | 0.7 em above/below (0.4 em short) |
| Boxes | 10 pt side padding, 6–7 pt top/bottom, 1 em before/after |
| Figures | 0.5 em before, 0.8 em after, scaled down only when wider than the text |

## 2. The Electromagnetics visual identity

The visual design is specific to this course. Its colour identity comes from the cover of Cheng's
*Field and Wave Electromagnetics*: a strong electric blue is the dominant colour, and a clear red
is used as a controlled accent. The values are original. Every colour is defined in
`template/el-palette.tex` and has one semantic role. No other file defines a colour.

| Role | Colour |
|---|---|
| text / mathematics | `ELink` #12203A |
| structure: headings, theorems, proofs | `ELnavy` #0D2B5E |
| dark blue ground: chapter panel, footer band | `ELnight` #0A2150 |
| **the Cheng blue**: cover panel, numbers, definitions; in figures the field / main object | `ELblue` #1F5FB5 |
| **the red accent**: rules, label tabs, markers, important results; in figures sources / second object | `ELred` #C8202F |
| worked examples (a quieter blue) | `ELsteel` #2F6E95 |
| exercises | `ELmaroon` #8F1D2C |
| remarks, captions, running heads | `ELslate` #56677F |

The recurring motifs of the identity are:
- the **cut-corner tab**, like the chamfer of a waveguide flange. It is used for box labels, the
  chapter label, the cover label and the part label.
- the **two-tone rule**: a short red segment at the leading edge that runs into a hairline. It
  is used under section headings, chapter titles and the contents title.
- the **arrow tip** pointing along the reading direction. It is used for subsections, list
  bullets and solutions.
- **field geometry** in the dark panels: dipole field lines and equipotentials, and a plane
  wave with its E and H components.

### Block family (`template/el-boxes.tex`, icons in `el-icons.tex`)

Every block has a strong top rule, a cut-corner label tab on that rule at the leading edge
(icon · name · number · optional title), a light tint and a thin closing rule. There are no side frames.

| Block | Colour | Icon | Distinguishing detail |
|---|---|---|---|
| Definition / تعریف | Cheng blue | ≜ | — |
| Theorem / قضیه | navy | ∇ | — |
| Lemma / لم | navy | dipole | — |
| Proposition / گزاره | navy | ⊙ | — |
| Corollary / نتیجه | navy | arrow from a point (mirrored in RTL) | — |
| Important result / نتیجهٔ مهم | red | spark | thin closed frame |
| Example / مثال | steel blue | wave | — |
| Exercise / تمرین | maroon | pen nib | dashed closing rule |
| Remark / نکته | slate | info | no tint |
| Proof / اثبات | navy | ⊢ (mirrored in RTL) | no tab: run-in heading, rail at the leading edge, ∎ at the end |

Only the proof ends with ∎. A block is numbered only when the slides number it:
`::: {.example number="1-3"}` prints Example 1-3 / مثال ۱-۳. In the Persian edition, the groups of
a compound number run right to left, as on the slides.

### Pagination

The filter groups the text into logical blocks: a paragraph with its equations, a figure with
its lead-in, a statement with the proof that follows it. Each block is measured before it is
placed. A block that fits on a page is never split; it moves to the next page whole. A block
longer than a page breaks normally. Headings wait for the block that follows them, so a
heading is never left alone at the bottom of a page. Manual `\newpage` is not used.

### Chapter openings and motifs

Each chapter opening is a dark panel with the chapter's motif, the chapter number in large
figures at the leading edge, a red "Chapter" tab, then the title, the title in the other language
and the list of sections. The motif of chapter `NN` is `template/motifs/mNN.tex`. It must
show an object that appears in that chapter of the instructor's notes. Until a chapter has its
own motif, the default `m00.tex` (a dipole field) is used. Motifs are drawn around `\ELmotifcx`
and are never mirrored.

## 3. Writing a chapter

`NN-slug/fa/moduleNN-slug.md` and `NN-slug/en/moduleNN-slug.md` hold the same structure:

~~~markdown
# Chapter title
## Section
### Subsection
Text with $inline$ maths and display maths:
$$\curl\vect{E}=-\pd{\vect{B}}{t}$$
::: {.definition title="optional title"}
...
:::
::: {.example}
... statement ...
::: {.solution}
...
:::
:::
```{.figure #mNN-name caption="caption"}
```
~~~

- Example numbers: `number="1-3"` exactly as on the slide. A figure gets a caption only when the
  slide has text for it (`caption=""` otherwise: no caption, no number). Cross-references to a
  numbered example in running text use `\ELnumc{1-11}`.
- Blocks: `definition`, `theorem`, `lemma`, `proposition`, `corollary`, `important`,
  `example`, `exercise`, `remark`, `proof`, `solution`.
- Notation always goes through the macros of `template/el-math.tex`: `\vect`, `\uvec`, `\uhat`,
  `\grad`, `\divg`, `\curl`, `\lapl`, `\pd`, `\od`, `\dif`, `\Re`, `\Im`, `\jj`, `\abs`, `\norm`.
  Set those macros to the instructor's conventions once, before the first chapter is written.
- Fractions are `\frac`, never `a/b` in plain text, also inside figures. Units are written in
  maths: `$\mathrm{V/m}$`.
- In Persian text, a Latin word next to a formula is written inside the formula
  (`$\mathrm{C/m^3}$`), so that it is not reordered.
- Figures are `template/figures/<name>.tex`, written with the styles of `el-tikz.tex`
  (`ELcurve`, `ELvec`, `ELfieldline`, `ELcharge`, `ELlab`, `\ELaxes`, `\ELframe`, `\ELinto`,
  `\ELoutof`, `ELplot`). Words inside a figure use `\ELL{English}{فارسی}`. Figures are drawn
  left to right in both editions.
- After compiling, inspect every figure for labels touching curves, arrows or other labels.
  Fix such collisions with anchors and offsets, never by changing the data.
