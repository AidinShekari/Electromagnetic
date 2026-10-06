<div align="center">

<img src="template/ferdowsi-logo-white.png" width="130" alt="Ferdowsi University of Mashhad">

# الکترومغناطیس
### Electromagnetics

دانشگاه فردوسی مشهد · Ferdowsi University of Mashhad

استاد · Instructor: سیدمحمد سعید ماجدی

گردآوری شده توسط [آیدین شکاری](https://shekari.me) · Compiled by [Aidin Shekari](https://shekari.me)

</div>

---

## 📘 جزوه کامل · Complete Notes

| | فارسی | English |
|---|---|---|
| جزوه کامل (همه فصل‌ها) · Full notes | [Electromagnetics-fa.pdf](00-full-notes/fa/Electromagnetics-fa.pdf) | [Electromagnetics-en.pdf](00-full-notes/en/Electromagnetics-en.pdf) |

## 📑 فصل‌ها · Chapters

| # | فصل | Chapter | PDF (fa) | PDF (en) |
|---|---|---|---|---|
| 1 | آنالیز برداری | Vector Analysis | [PDF](01-vector-analysis/fa/module01-vector-analysis.pdf) | [PDF](01-vector-analysis/en/module01-vector-analysis.pdf) |
| 2 | میدان‌های الکتریکی ساکن | Static Electric Fields | [PDF](02-static-electric-fields/fa/module02-static-electric-fields.pdf) | [PDF](02-static-electric-fields/en/module02-static-electric-fields.pdf) |
| 3 | حل مسائل الکتریسیته ساکن | Solution of Electrostatic Problems | [PDF](03-electrostatic-problems/fa/module03-electrostatic-problems.pdf) | [PDF](03-electrostatic-problems/en/module03-electrostatic-problems.pdf) |
| 4 | جریان‌های الکتریکی دائم | Steady Electric Currents | [PDF](04-steady-electric-currents/fa/module04-steady-electric-currents.pdf) | [PDF](04-steady-electric-currents/en/module04-steady-electric-currents.pdf) |

The notes contain only the chapters whose slides have been provided ([source/](source/README.md)).
The instructor's slides are the only source of the content; every deliberate difference is
listed in [REVIEW.md](REVIEW.md). The design system is described in [DESIGN.md](DESIGN.md).

## 🗂 ساختار پوشه‌ها · Repository layout

```
Electromagnetic/
├── 00-full-notes/
│   ├── fa/   Electromagnetics-fa.tex + .pdf   جزوه کامل فارسی (با فهرست مطالب)
│   └── en/   Electromagnetics-en.tex + .pdf   complete English notes
├── 01-vector-analysis/
│   ├── fa/   module01-vector-analysis.md · .tex · content.tex · .pdf
│   └── en/   module01-vector-analysis.md · .tex · content.tex · .pdf
├── …                                          (one folder per chapter, 01 … 04)
├── source/                                    اسلایدهای استاد · the instructor's slides
├── specimen/                                  design specimen (layout check only)
├── template/                                  قالب لتک، لوگوی دانشگاه، فونت Vazirmatn، شکل‌ها
└── tools/                                     build script, Markdown → LaTeX filter, figure generator
```

هر فایل `.tex` داخل پوشه‌ی خودش با XeLaTeX کامپایل می‌شود ·
Every `.tex` compiles with XeLaTeX from inside its own folder
(fonts: *Vazirmatn* bundled in `template/fonts/`, *TeX Gyre Termes*, *Heros* and *Termes Math*).

To regenerate everything from the Markdown sources (needs `pandoc` ≥ 3 and `latexmk`):

```bash
python3 tools/build.py                 # all chapters and the complete notes, both languages
python3 tools/build.py --chapter 03    # one chapter, both languages
python3 tools/build.py --only fa       # one language
python3 tools/genfigs.py               # regenerate the computed figures
```
