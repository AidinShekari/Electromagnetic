# میدان‌های الکترومغناطیسی متغیر با زمان

## سرفصل‌ها

```{.figure #m06-course-outline caption=""}
```

## مقدمه

- روابط اصلی حاکم بر الکتریسیته و مغناطیس ساکن

| Fundamental Relations | Electrostatic Model | Magnetostatic Model |
|---|:---:|:---:|
| Governing equations | $\nabla\times\vect{E}=0$, $\nabla\cdot\vect{D}=\rho$ | $\nabla\cdot\vect{B}=0$, $\nabla\times\vect{H}=\vect{J}$ |
| Constitutive relations (linear and isotropic media) | $\vect{D}=\epsilon\vect{E}$ | $\vect{H}=\dfrac1\mu\vect{B}$ |

- در حالت ساکن (نامتغیر با زمان)، بردارهای میدان الکتریکی و میدان‌های مغناطیسی جفت‌های جداگانه و مجزا از هم را تشکیل می‌دهند.
- در ادامه خواهیم دید که در حالت متغیر با زمان، یک میدان مغناطیسی متغیر با زمان میدان الکتریکی بوجود می‌آورد و بالعکس

## قانون القای فارادی

- در سال ۱۸۲۰ **هانس کریستین ارستد** نشان داد که سیم حامل جریان الکتریکی، باعث تغییر جهت عقربه قطب‌نما می‌شود.
    - حرکت عقربه قطب‌نما ناشی از نیروی مغناطیسی ایجاد شده توسط میدان مغناطیسی حاصل از جریان الکتریکی بود.
- پس از این کشف **مایکل فارادی** به صورت شهودی پی برد که میدان مغناطیسی نیز به طور مشابه باید دارای اثر الکتریکی باشد و جریانی در سیم ایجاد کند.
- پس از حدود ۱۰ سال آزمایش، او موفق به کشفی شد که به قانون القای فارادی مشهور است.

::: {.definition title="قانون القای فارادی"}
اگر شار مغناطیسی عبوری از یک مدار بسته با گذشت زمان تغییر کند، در آن مدار نیروی محرکه الکتریکی القا می‌شود. این نیروی محرکه باعث عبور جریان خواهد شد.
:::

- قطبیت نیروی محرکه الکتریکی و در نتیجه جهت جریان القایی را می‌توان توسط قانون لنز تعیین کرد.

::: {.definition title="قانون لنز"}
جریان القا شده در مدار همواره در جهتی است که با تغییر شار مغناطیسی تولید کننده آن جریان مخالفت کند.
:::

- بیان ریاضی قانون القای فارادی

::: {.important}
$$v_{emf}=-N\frac{d\Phi}{dt}=-N\frac{d}{dt}\int_S\vect{B}\cdot d\vect{s}$$
:::

- تعریف نیرو محرکه القا شده در مداری با مسیر بسته $C$

$$v_{emf}\triangleq\oint_C\vect{E}\cdot\dif\vect{\ell}$$

- با فرض ثابت بودن مدار

$$v_{emf}=\oint_C\vect{E}\cdot\dif\vect{\ell}=-\int_S\frac{\partial\vect{B}}{\partial t}\cdot d\vect{s}\quad\Longrightarrow\quad\int_S(\nabla\times\vect{E})\cdot d\vect{s}=-\int_S\frac{\partial\vect{B}}{\partial t}\cdot d\vect{s}$$

- در گام آخر از قضیه استوکس استفاده شده است.

::: {.important}
$$\nabla\times\vect{E}=-\frac{\partial\vect{B}}{\partial t}$$
:::

- در حالت متغیر با زمان، میدان الکتریکی ابقایی نیست $\ELto$ $\nabla\times\vect{E}\neq0$
- در حالت متغیر با زمان، پتانسیل اسکالر به صورت $V=-\int\vect{E}\cdot\dif\vect{\ell}$ قابل تعریف نیست. زیرا اختلاف پتانسیل بین دو نقطه فرضی وابسته به مسیر انتگرالگیری شده و مقدار ثابتی نخواهد داشت.
- در فرکانس‌های پایین $\ELto$ $\nabla\times\vect{E}\simeq0$ $\ELto$ پتانسیل اسکالر قابل تعریف است (تئوری مدارهای فشرده)

::: {.example number="6-1"}
حلقه دایره‌ای با $N$ دور سیم هادی در صفحه $xy$ قرار دارد به گونه‌ای‌که مرکز آن در مبدأ میدان مغناطیسی توصیف شده به صورت زیر است

$$\vect{B}=\uvec{z}B_0\cos\left(\frac{\pi r}{2b}\right)\sin(\omega t)$$

در رابطه فوق $b$ شعاع حلقه و $\omega$ فرکانس زاویه‌ای است. نیرو محرکه القا شده را بدست آورید.

::: {.solution}
$$\begin{aligned}\Phi=\int_S\vect{B}\cdot d\vect{s}&=\int_0^{2\pi}\!\!\int_0^b\left[B_0\cos\left(\frac{\pi r}{2b}\right)\sin(\omega t)\,\uvec{z}\right]\cdot\left(r\,dr\,d\phi\,\uvec{z}\right)\\&=\frac{8b^2}{\pi}\left(\frac\pi2-1\right)B_0\sin(\omega t)\end{aligned}$$
$$v=-N\frac{d\Phi}{dt}=-\frac{8Nb^2}{\pi}\left(\frac\pi2-1\right)B_0\omega\cos(\omega t)$$
:::
:::

## جریان جابجایی

- قانون مداری آمپر برای میدان مغناطیسی ساکن

$$\nabla\times\vect{H}=\vect{J}$$

- **جیمز کلارک ماکسول** از صحت این معادله اطمینان نداشت زیرا

$$\nabla\cdot(\nabla\times\vect{H})=0=\nabla\cdot\vect{J}$$

- که با معادله پیوستگی سازگار نیست

$$\nabla\cdot\vect{J}=-\frac{\partial\rho}{\partial t}$$

- ماکسول برای رفع این ناسازگاری رابطه فوق را به صورت زیر اصلاح کرد

$$\nabla\cdot(\nabla\times\vect{H})=0=\nabla\cdot\vect{J}+\frac{\partial\rho}{\partial t}\quad\xrightarrow{\ \nabla\cdot\vect{D}=\rho\ }\quad\nabla\cdot(\nabla\times\vect{H})=\nabla\cdot\left(\vect{J}+\frac{\partial\vect{D}}{\partial t}\right)$$

::: {.important}
$$\nabla\times\vect{H}=\vect{J}+\frac{\partial\vect{D}}{\partial t}$$
:::

- به سادگی می‌توان نشان داد که $\partial\vect{D}/\partial t$ دارای بعد چگالی جریان است. به این پارامتر **چگالی جریان جابجایی** گویند.
- شکل اصلاح شده قانون مداری آمپر بیان می‌کند که یک میدان الکتریکی متغیر با زمان، یک میدان مغناطیسی به وجود می‌آورد حتی اگر جریانی نیز وجود نداشته باشد.

## معادلات ماکسول

- معادلات حاکم بر میدان‌های الکتریکی و مغناطیسی در حالت متغیر با زمان یا **معادلات ماکسول**

| Differential Form | Integral Form | Significance |
|---|---|---|
| $\nabla\times\vect{E}=-\dfrac{\partial\vect{B}}{\partial t}$ | $\oint_C\vect{E}\cdot\dif\vect{\ell}=-\dfrac{d\Phi}{dt}$ | Faraday's law |
| $\nabla\times\vect{H}=\vect{J}+\dfrac{\partial\vect{D}}{\partial t}$ | $\oint_C\vect{H}\cdot\dif\vect{\ell}=I+\int_S\dfrac{\partial\vect{D}}{\partial t}\cdot d\vect{s}$ | Ampère's circuital law |
| $\nabla\cdot\vect{D}=\rho$ | $\oint_S\vect{D}\cdot d\vect{s}=Q$ | Gauss's law |
| $\nabla\cdot\vect{B}=0$ | $\oint_S\vect{B}\cdot d\vect{s}=0$ | No isolated magnetic charge |
