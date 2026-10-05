#!/bin/bash
# QA harness: every figure of template/figures on its own, in one language ($1 = en|fa)
L=$1; shift
{
printf '%s\n' '\documentclass[11pt]{article}\def\ELroot{../../template}\input{\ELroot/el-'$L'}\begin{document}'
for f in "$@"; do n=$(basename $f .tex); printf '%s\n' "\\par\\noindent{\\ttfamily\\small \\lr{$n}}\\par\\ELfigure{$n}{}"; done
printf '%s\n' '\end{document}'
} > figs-$L.tex
xelatex -interaction=nonstopmode -halt-on-error figs-$L.tex > /dev/null 2>&1; xelatex -interaction=nonstopmode -halt-on-error figs-$L.tex > log-$L.txt 2>&1; echo "exit $?"; grep -E "^!|^l\.[0-9]" figs-$L.log | head -8
