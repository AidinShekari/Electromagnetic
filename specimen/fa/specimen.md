# نمونهٔ طراحی

## دربارهٔ این نمونه

این فصل نمونهٔ حروف‌چینی سامانهٔ طراحی است. جمله‌ها و فرمول‌های آن فقط برای آزمودن صفحه‌آرایی نوشته شده‌اند؛ محتوای درس نیستند و هرگز در کتاب قرار نمی‌گیرند.

ریاضیات درون متن: $x$، $y$، $z$، $r$، $\theta$، $\phi$، $\rho$، $\vect{E}$، $\vect{H}$، $\vect{D}$، $\vect{B}$، $\vect{J}$، $\sin\theta$، $\cos\phi$، $\ln r$، $e^{\jj\omega t}$، $\Re\{z\}$، $\Im\{z\}$، $\frac{1}{x}$ و $\uvec{x}$. واژهٔ لاتین درون متن: Electromagnetics (نمونه).

### فرمول‌های نمایشی

$$\vect{A}=A_x\uvec{x}+A_y\uvec{y}+A_z\uvec{z},\qquad \abs{\vect{A}}=\sqrt{A_x^2+A_y^2+A_z^2}$$

$$\grad f=\pd{f}{x}\uvec{x}+\pd{f}{y}\uvec{y}+\pd{f}{z}\uvec{z},\qquad \divg\vect{A},\qquad \curl\vect{A},\qquad \lapl f$$

$$\oint_C \vect{A}\cdot\dif\vect{l},\qquad \oiint_S \vect{A}\cdot\dif\vect{s},\qquad \iiint_V f\,\dif v,\qquad \sum_{n=1}^{\infty}\frac{1}{n^2},\qquad \lim_{x\to0}\frac{\sin x}{x}$$

## قالب‌ها

::: {.definition title="عنوان نمونه"}
متن قالب تعریف، با فرمول درون‌متنی $f(x)=\frac{1}{x}$ (در پرانتز).
$$g(x)=\int_0^x f(t)\,\dif t$$
:::

::: {.theorem}
متن قالب قضیه.
:::

::: {.proof}
متن قالب اثبات؛ مربع پایانی، پایان اثبات را نشان می‌دهد.
$$a=b\quad\Longrightarrow\quad a+c=b+c$$
:::

::: {.lemma}
متن قالب لم.
:::

::: {.proposition}
متن قالب گزاره.
:::

::: {.corollary}
متن قالب نتیجه.
:::

::: {.important}
متن قالب نتیجهٔ مهم.
$$\curl\vect{H}=\vect{J}+\pd{\vect{D}}{t}$$
:::

::: {.example}
متن قالب مثال.

::: {.solution}
متن حل درون مثال.
:::
:::

::: {.exercise}
متن قالب تمرین.
:::

::: {.remark}
متن قالب نکته.
:::

## شکل‌ها و جدول‌ها

بندی که شکل زیر را معرفی می‌کند.

```{.figure #specimen-axes caption="شکل نمونه: محورها، یک منحنی، بردارها و برچسب‌ها"}
```

| کمیت | نماد | یکا |
|---|---|---|
| نمونهٔ الف | $\vect{E}$ | $\mathrm{V/m}$ |
| نمونهٔ ب | $\vect{H}$ | $\mathrm{A/m}$ |
| نمونهٔ ج | $\rho$ | $\mathrm{C/m^3}$ |

- نخستین مورد فهرست.
- دومین مورد فهرست، با $\theta$.
