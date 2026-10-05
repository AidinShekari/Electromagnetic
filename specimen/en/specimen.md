# Design Specimen

## About this specimen

This chapter is a typesetting specimen of the design system. Its sentences and formulas are placeholders chosen only to exercise the layout; they are not course content and are never included in the book.

Inline mathematics in running text: $x$, $y$, $z$, $r$, $\theta$, $\phi$, $\rho$, $\vect{E}$, $\vect{H}$, $\vect{D}$, $\vect{B}$, $\vect{J}$, $\sin\theta$, $\cos\phi$, $\ln r$, $e^{\jj\omega t}$, $\Re\{z\}$, $\Im\{z\}$, $\frac{1}{x}$ and $\uvec{x}$.

### Displayed formulas

$$\vect{A}=A_x\uvec{x}+A_y\uvec{y}+A_z\uvec{z},\qquad \abs{\vect{A}}=\sqrt{A_x^2+A_y^2+A_z^2}$$

$$\grad f=\pd{f}{x}\uvec{x}+\pd{f}{y}\uvec{y}+\pd{f}{z}\uvec{z},\qquad \divg\vect{A},\qquad \curl\vect{A},\qquad \lapl f$$

$$\oint_C \vect{A}\cdot\dif\vect{l},\qquad \oiint_S \vect{A}\cdot\dif\vect{s},\qquad \iiint_V f\,\dif v,\qquad \sum_{n=1}^{\infty}\frac{1}{n^2},\qquad \lim_{x\to0}\frac{\sin x}{x}$$

## Blocks

::: {.definition title="Placeholder title"}
Body text of a definition block, with an inline formula $f(x)=\frac{1}{x}$.
$$g(x)=\int_0^x f(t)\,\dif t$$
:::

::: {.theorem}
Body text of a theorem block.
:::

::: {.proof}
Body text of a proof block; the square at the end marks its close.
$$a=b\quad\Longrightarrow\quad a+c=b+c$$
:::

::: {.lemma}
Body text of a lemma block.
:::

::: {.proposition}
Body text of a proposition block.
:::

::: {.corollary}
Body text of a corollary block.
:::

::: {.important}
Body text of an important-result block.
$$\curl\vect{H}=\vect{J}+\pd{\vect{D}}{t}$$
:::

::: {.example}
Body text of an example block.

::: {.solution}
Body text of a solution inside the example.
:::
:::

::: {.exercise}
Body text of an exercise block.
:::

::: {.remark}
Body text of a remark block.
:::

## Figures and tables

A paragraph that introduces the figure below.

```{.figure #specimen-axes caption="A placeholder figure: axes, a curve, vectors and labels"}
```

| Quantity | Symbol | Unit |
|---|---|---|
| placeholder A | $\vect{E}$ | $\mathrm{V/m}$ |
| placeholder B | $\vect{H}$ | $\mathrm{A/m}$ |
| placeholder C | $\rho$ | $\mathrm{C/m^3}$ |

- First item of a list.
- Second item of a list, with $\theta$.
