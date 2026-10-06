# Electromagnetics — Lecture Notes / جزوهٔ الکترومغناطیس

Typeset lecture notes of the course *Electromagnetics* (الکترومغناطیس), Ferdowsi University of
Mashhad, in Persian (RTL) and English (LTR).

- **Instructor / استاد:** سیدمحمد سعید ماجدی
- **Compiled and edited by / جمع‌آوری و تنظیم:** Aidin Shekari / آیدین شکاری

The instructor's notes are the only source of the academic content. The typeset notes follow
their order, notation, values, figures and wording. Nothing is added from textbooks. Every
deliberate difference from the source (an unambiguous typo, for example) is listed in
[REVIEW.md](REVIEW.md).

## Status

| Part | State |
|---|---|
| Design system, both editions (`template/`) | done |
| Build pipeline (`tools/`) | done |
| Design specimen, both editions (`specimen/`) | done (QA only, not course content) |
| Chapter 1, Vector Analysis (slides `Ch1_1` to `Ch1_5`), both editions | done |
| Chapter 2, Static Electric Fields (slides `Ch2_1` to `Ch2_8`), both editions | done |
| Later chapters | waiting for the instructor's slides |

## Complete book / کتاب کامل
- [English](00-full-notes/en/Electromagnetics-en.pdf)
- [فارسی](00-full-notes/fa/Electromagnetics-fa.pdf)

## Chapters
| # | Chapter | فصل | PDF |
|---|---|---|---|
| 01 | Vector Analysis | آنالیز برداری | [EN](01-vector-analysis/en/module01-vector-analysis.pdf) · [FA](01-vector-analysis/fa/module01-vector-analysis.pdf) |
| 02 | Static Electric Fields | میدان‌های الکتریکی ساکن | [EN](02-static-electric-fields/en/module02-static-electric-fields.pdf) · [FA](02-static-electric-fields/fa/module02-static-electric-fields.pdf) |

The book contains only the chapters whose slides have been provided ([source/](source/README.md)).

## Design specimen
- [English](specimen/en/specimen-en.pdf)
- [فارسی](specimen/fa/specimen-fa.pdf)

The specimen shows the cover, title page, contents, a chapter opening and every block type.
Its text is placeholder text for checking the layout.

## Build / ساخت
Needs `pandoc` ≥ 3 and XeLaTeX with `latexmk`, TeX Gyre Termes, Heros and Termes Math
(`fonts-texgyre`, `fonts-texgyre-math` on Debian/Ubuntu).

```bash
python3 tools/build.py                 # chapters and the complete book, both languages
python3 tools/build.py --chapter 05    # one chapter, both languages
python3 tools/build.py --only fa       # one language
python3 tools/build.py --specimen      # the design specimen
python3 tools/genfigs.py               # regenerate the computed figures
python3 tools/contact.py book.pdf out/  # contact sheets of a PDF for visual QA (needs Pillow)
```

Layout: `NN-slug/{fa,en}/moduleNN-slug.md` (source) → `.tex` → `.pdf`. The complete book goes to
`00-full-notes/{fa,en}/Electromagnetics-{fa,en}.pdf`. `template/` holds the shared style layer,
the fonts (Vazirmatn, OFL), the university logo, the figures (native TikZ/PGFPlots) and the
chapter-opening motifs. `tools/` holds the build script and the Markdown → LaTeX filter. The
design system and the authoring conventions are described in [DESIGN.md](DESIGN.md).
