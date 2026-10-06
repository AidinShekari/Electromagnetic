# جریان‌های الکتریکی دائم

## سرفصل‌ها

```{.figure #m04-course-outline caption=""}
```

## جریان‌های الکتریکی دائم

- در فصل‌های قبل با مسائل الکتریسیته ساکن ناشی از بارهای الکتریکی ساکن سروکار داشتیم.
    - اکنون در این فصل به بارهای متحرک الکتریکی که جریان الکتریکی را ایجاد می‌کنند می‌پردازیم.
- جریان‌های الکتریکی ناشی از حرکت بارهای آزاد به سه دسته تقسیم می‌شوند
    - **جریان‌های هدایتی:** در هادی‌ها و نیمه‌هادی‌ها توسط حرکت رانشی الکترون‌ها یا حفره‌ها بوجود می‌آیند.
    - **جریان‌های الکترولیتی:** ناشی از حرکت یون‌های مثبت و منفی
    - **جریان‌های انتقالی:** ناشی از حرکت الکترون‌ها یا یون‌ها در خلاء
- در این فصل توجه خود را به جریان‌های هدایتی که قانون اهم بر آن‌ها حاکم است متمرکز می‌کنیم.

```{.figure #m04-map caption=""}
```

- مفهوم **چگالی حجمی جریان** چیست و رابطه **چگالی جریان انتقالی** چگونه است؟
- رابطه **چگالی جریان هدایتی** چگونه است؟
- شکل نقطه ای **قانون اهم** چگونه است؟
- **معادله پیوستگی** چیست و چگونه از روی آن **قانون جریان کرشهف** استخراج می شود؟
- رابطه **قانون ژول** که نشان دهنده میزان اتلاف توان بر اثر عبور جریان از یک جسم هادی است، چگونه است؟

## مفهوم چگالی جریان و استخراج قانون اهم

```{.figure #m04-current-element caption=""}
```

- حرکت دائمی تعدادی حامل بار، هر یک با بار $q$ گذرنده از جز کوچک سطحیِ $\Delta s$ با سرعت $\vect{u}$ را در نظر بگیرید
- اگر $N$ تعداد حامل‌های بار در واحد حجم باشد، آنگاه مقدار بار گذرنده از سطح $\Delta s$ در مدت زمان $\Delta t$ برابر است با

$$\Delta Q=Nq\vect{u}\cdot\uvec{n}\,\Delta s\,\Delta t\qquad(\mathrm{C})$$

- چون جریان نرخ زمانی تغییر بار است داریم

$$\Delta I=\frac{\Delta Q}{\Delta t}=Nq\vect{u}\cdot\uvec{n}\,\Delta s=Nq\vect{u}\cdot\Delta\vect{s}\qquad(\mathrm{A})$$

- چگالی جریان حجمی با واحد آمپر بر متر مربع را به صورت زیر تعریف می‌کنیم

$$\vect{J}=Nq\vect{u}\qquad(\mathrm{A/m^2})$$

::: {.important title="چگالی جریان انتقالی"}
$$\vect{J}=\rho\vect{u}\qquad(\mathrm{A/m^2})$$
:::

- بنابراین

$$\Delta I=\vect{J}\cdot\Delta\vect{s}$$

- به این ترتیب کل جریان گذرنده از سطح دلخواه $S$ برابر است با

::: {.important}
$$I=\int_S\vect{J}\cdot d\vect{s}\qquad(\mathrm{A})$$
:::

- جریان‌های هدایتی نتیجه حرکت رانشی حامل‌های بار تحت تأثیر یک میدان الکتریکی اعمال شده می‌باشند.
- در مورد اکثر مواد هادی سرعت رانش متوسط، مستقیماً با شدت میدان الکتریکی متناسب است.
    - در مورد هادی‌های فلزی داریم

$$\vect{u}=-\mu_e\vect{E}\qquad(\mathrm{m/s})$$

- $\mu_e$: ضریب تحرک الکترونی با واحد $\mathrm{m^2/V\cdot s}$

$$\vect{J}=-\rho_e\mu_e\vect{E}$$

- $\rho_e=-Ne$: چگالی حجمی بار الکترون‌های رانشی بوده و یک کمیت منفی است

::: {.important title="شکل نقطه ای قانون اهم"}
$$\vect{J}=\sigma\vect{E}\qquad(\mathrm{A/m^2})$$
:::

- $\sigma=-\rho_e\mu_e$: یک پارامتر اساسی محیط بوده و رسانندگی نام دارد
- واحد رسانندگی $\mathrm{A/V\cdot m}$ یا زیمنس بر متر است. عکس رسانندگی را ضریب مقاومت می‌نامند و واحد آن $\Omega\cdot\mathrm{m}$ است.

- بدست آوردن رابطه بین ولتاژ و جریان یک قطعه از ماده‌ای همگن با رسانندگی $\sigma$، طول $\ell$ و سطح مقطع یکنواخت $S$ با استفاده از شکل نقطه‌ای قانون اهم

```{.figure #m04-resistor caption=""}
```

$$\left.\begin{aligned}V_{12}=E\ell\quad&\Longrightarrow\quad E=\frac{V_{12}}{\ell}\\I=\int_S\vect{J}\cdot d\vect{s}=JS\quad&\Longrightarrow\quad J=\frac IS\end{aligned}\right\}\quad\frac IS=\sigma\frac{V_{12}}{\ell}$$
$$V_{12}=\left(\frac{\ell}{\sigma S}\right)I=RI$$

::: {.important}
$$R=\frac{\ell}{\sigma S}\qquad(\Omega)$$
$$G=\frac1R=\sigma\frac S\ell\qquad(\mathrm{S})$$
:::

- $G$: رسانایی یا عکس مقاومت با واحد مهو یا زیمنس

## معادله پیوستگی و استخراج قانون جریان کرشهف

```{.figure #m04-map-continuity caption=""}
```

- اصل بقای بار یکی از اصول موضوعی اساسی فیزیک است.
    - بار الکتریکی نمی‌تواند تولید یا نابود شود.
- حجم دلخواه $V$ را که با سطح $S$ احاطه شده است در نظر بگیرید. بار خالص $Q$ درون این ناحیه وجود دارد. اگر جریان خالص $I$ از سطح به سمت بیرون ناحیه عبور کند، بار درون حجم باید با نرخی برابر با جریان کاهش یابد. برعکس اگر جریان خالصی از سطح به سمت درون ناحیه عبور کند، بار درون حجم باید با نرخی برابر با جریان افزایش یابد.
- جریان خارج شونده از ناحیه، کل شار خروجی بردار چگالی جریان از سطح $S$ است

$$I=\oint_S\vect{J}\cdot d\vect{s}=-\frac{dQ}{dt}=-\frac{d}{dt}\int_V\rho\,dv$$
$$\int_V\nabla\cdot\vect{J}\,dv=-\int_V\frac{\partial\rho}{\partial t}\,dv$$

- چون معادله فوق باید مستقل از انتخاب $V$ باشد

::: {.important title="معادله پیوستگی"}
$$\nabla\cdot\vect{J}=-\frac{\partial\rho}{\partial t}\qquad(\mathrm{A/m^3})$$
:::

- اگر تغییرات زمانی نداشته باشیم

$$\nabla\cdot\vect{J}=0$$

::: {.important title="قانون جریان کرشهف"}
$$\oint_S\vect{J}\cdot d\vect{s}=0$$
:::

- پیش از این گفته بودیم که بارهای قرار داده شده درون یک هادی به سطح آن حرکت کرده به گونه‌ایکه در حالت تعادل درون هادی $\rho=0$ است. اکنون می‌خواهیم این بیان را ثابت کنیم

$$\left.\begin{aligned}\sigma\nabla\cdot\vect{E}&=-\frac{\partial\rho}{\partial t}\\\nabla\cdot\vect{E}&=\rho/\epsilon\end{aligned}\right\}\quad\frac{\partial\rho}{\partial t}+\frac\sigma\epsilon\rho=0\quad\Longrightarrow\quad\rho=\rho_0e^{-(\sigma/\epsilon)t}\qquad(\mathrm{C/m^3})$$

- $\rho_0$: چگالی بار اولیه
- معادله فوق بیان می‌کند که چگالی بار در یک نقطه خاص به صورت نمایی با زمان کاهش می‌یابد.
- چگالی اولیه در زمانی برابر با $\tau=\epsilon/\sigma$ به $1/e$ یا $36.8\%$ مقدار خود کاهش می‌یابد.
    - در یک هادی خوب مانند مس $\tau=1.52\times10^{-19}\,\mathrm{s}$ است.
    - برای یک عایق خوب این زمان ممکن است ساعت‌ها یا روزها به طول انجامد.

## اتلاف توان و قانون ژول

```{.figure #m04-map-joule caption=""}
```

- تحت تأثیر یک میدان الکتریکی، الکترون‌های آزاد در هادی حرکت کرده و با اتم‌های موجود در شبکه کریستالی برخورد می‌کنند. بنابراین انرژی از میدان الکتریکی به اتم‌های تحت ارتعاش منتقل می‌گردد.
- کار انجام شده توسط میدان الکتریکی در حرکت بار $q$ تا فاصله $\Delta\ell$ برابر است با

$$\Delta W=\vect{F}\cdot\Delta\vect{\ell}=q\vect{E}\cdot\Delta\vect{\ell}$$

- این کار متناظر با توان زیر است

$$p=\lim_{\Delta t\to0}\frac{\Delta w}{\Delta t}=q\vect{E}\cdot\vect{u}$$

- $\vect{u}$: سرعت حرکت حامل های بار

$$dp=\rho\,dv\,\vect{E}\cdot\vect{u}$$
$$dP=\vect{E}\cdot\vect{J}\,dv$$

- به ازای حجم مشخص $V$ کل توان تبدیل شده به حرارت برابر است با

::: {.important title="قانون ژول"}
$$P=\int_V\vect{E}\cdot\vect{J}\,dv\qquad(\mathrm{W})$$
:::

- در یک هادی با سطح مقطع ثابت داریم

$$P=\int_LE\,d\ell\int_SJ\,ds=VI$$

::: {.important}
$$P=I^2R\qquad(\mathrm{W})$$
:::

- که همان رابطه آشنای توان اهمی است و حرارت تلف شده در مقاومت $R$ را نشان می‌دهد.

## بررسی شرایط مرزی چگالی جریان

```{.figure #m04-map-boundary caption=""}
```

- هنگامیکه جریان به طور مایل از فصل مشترک بین دو محیط با رسانندگی‌های متفاوت عبور می‌کند، بردار چگالی جریان هم در جهت و هم در اندازه تغییر می‌کند.
- معادلات حاکم بر چگالی جریان دائم عبارتند از

**Governing Equations for Steady Current Density**

| Differential Form | Integral Form |
|---|---|
| $\nabla\cdot\vect{J}=0$ | $\oint_S\vect{J}\cdot d\vect{s}=0$ |
| $\nabla\times\left(\dfrac{\vect{J}}{\sigma}\right)=0$ | $\oint_C\dfrac1\sigma\vect{J}\cdot\dif\vect{\ell}=0$ |


- شرایط مرزی به صورت زیرند

::: {.important}
$$\nabla\cdot\vect{J}=0\quad\Longrightarrow\quad J_{1n}=J_{2n}\qquad(\mathrm{A/m^2})$$
$$\nabla\times(\vect{J}/\sigma)=0\quad\Longrightarrow\quad\frac{J_{1t}}{J_{2t}}=\frac{\sigma_1}{\sigma_2}$$
:::

- هنگامیکه جریان دائمی از مرز دو دی‌الکتریک متفاوت با اتلاف عبور می‌کند

$$J_{1n}=J_{2n}\to\sigma_1E_{1n}=\sigma_2E_{2n}$$
$$D_{1n}-D_{2n}=\rho_s\to\epsilon_1E_{1n}-\epsilon_2E_{2n}=\rho_s$$
$$\rho_s=\left(\epsilon_1\frac{\sigma_2}{\sigma_1}-\epsilon_2\right)E_{2n}=\left(\epsilon_1-\epsilon_2\frac{\sigma_1}{\sigma_2}\right)E_{1n}$$

- $E_{1n}=\uvec{n2}\cdot\vect{E}_1$ و $E_{2n}=\uvec{n2}\cdot\vect{E}_2$
- اگر محیط ۲ نسبت به محیط ۱ هادی به مراتب بهتری باشد

$$\rho_s=\epsilon_1E_{1n}=D_{1n}$$

- که همان رابطه شرط مرزی هادی است.

::: {.example number="4-1"}
اختلاف پتانسیل $\mathcal{V}$ به یک خازن صفحه ای موازی با مساحت $S$ اعمال شده است. فضای بین صفحات هادی با دو ماده دی الکتریک تلفاتی به ضخامت های $d_1$ و $d_2$، گذردهی های $\epsilon_1$ و $\epsilon_2$ و رسانایی های $\sigma_1$ و $\sigma_2$ پر شده است. مطلوبست

- الف. شدت میدان الکتریکی در دو محیط
- ب. چگالی جریان در دو محیط
- ج. چگالی بار سطحی روی صفحات هادی و در مرز دو دی الکتریک

```{.figure #m04-ex1 caption=""}
```

::: {.solution}
- الف.

$$J_1=J_2\quad\Longrightarrow\quad\begin{aligned}\mathcal{V}&=E_1d_1+E_2d_2\\\sigma_1E_1&=\sigma_2E_2\end{aligned}$$
$$E_1=\frac{\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}\qquad E_2=\frac{\sigma_1\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$

- ب.

$$J_1=J_2=\sigma_1E_1=\sigma_2E_2=\frac{\sigma_1\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$

- ج.

$$\uvec{n}\cdot\vect{E}_1=\frac{\rho_{s1}}{\epsilon_1}\quad\Longrightarrow\quad\rho_{s1}=\epsilon_1E_1=\frac{\epsilon_1\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$
$$\uvec{n}\cdot\vect{E}_2=\frac{\rho_{s2}}{\epsilon_2}\quad\Longrightarrow\quad\rho_{s2}=-\epsilon_2E_2=-\frac{\epsilon_2\sigma_1\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$
$$\rho_{si}=\left(\epsilon_1-\epsilon_2\frac{\sigma_1}{\sigma_2}\right)E_{1n}\quad\Longrightarrow\quad\begin{aligned}\rho_{si}&=\left(\epsilon_2\frac{\sigma_1}{\sigma_2}-\epsilon_1\right)\frac{\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}\\&=\frac{(\epsilon_2\sigma_1-\epsilon_1\sigma_2)\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}\qquad(\mathrm{C/m^2})\end{aligned}$$
:::
:::

## محاسبه مقاومت

```{.figure #m04-map-resistance caption=""}
```

- نحوه محاسبه مقدار **مقاومت نشتی** در ساختارهای خازنی چگونه است؟
- نحوه محاسبه مقدار مقاومت ساختارهای مختلف چگونه است؟

- ظرفیت بین دو هادی که توسط یک محیط دی‌الکتریک از هم جدا شده‌اند برابر است با

$$C=\frac QV=\frac{\oint_S\vect{D}\cdot d\vect{s}}{-\int_L\vect{E}\cdot\dif\vect{\ell}}=\frac{\oint_S\epsilon\vect{E}\cdot d\vect{s}}{-\int_L\vect{E}\cdot\dif\vect{\ell}}$$

- انتگرال سطحی روی سطح در برگیرنده هادی مثبت و انتگرال خطی از هادی منفی تا هادی مثبت انجام می‌گیرد.
- اگر محیط دی‌الکتریک با اتلاف باشد، جریانی از هادی مثبت به هادی منفی عبور خواهد کرد. مقاومت بین هادی‌ها (مقاومت نشتی) برابر است با

$$R=\frac VI=\frac{-\int_L\vect{E}\cdot\dif\vect{\ell}}{\oint_S\vect{J}\cdot d\vect{s}}=\frac{-\int_L\vect{E}\cdot\dif\vect{\ell}}{\oint_S\sigma\vect{E}\cdot d\vect{s}}$$

- درصورتیکه ضریب گذردهی و رسانندگی دارای وابستگی فضایی مشابهی باشند ($\epsilon(x,y,z)=k\sigma(x,y,z)$) و یا محیط دی‌الکتریک همگن باشد ($\epsilon$ و $\sigma$ وابستگی به مختصات فضایی نداشته باشند)

::: {.important}
$$RC=\frac CG=\frac\epsilon\sigma$$
:::

::: {.example number="4-2"}
مطلوبست محاسبه مقاومت نشتی در واحد طول

- الف. بین هادی های داخلی و خارجی یک کابل هم محور با شعاع $a$ برای هادی داخلی، شعاع $b$ برای هادی خارجی و محیط دی الکتریک با رسانندگی $\sigma$
- ب. خط انتقال دو سیمه شامل دو سیم با شعاع $a$ و فاصله $D$ درون محیطی با رسانندگی $\sigma$

::: {.solution}
- الف. ظرفیت در واحد طول یک کابل کواکسیال

$$C_1=\frac{2\pi\epsilon}{\ln(b/a)}\qquad(\mathrm{F/m})$$

- مقاومت نشتی در واحد طول

$$R_1=\frac\epsilon\sigma\left(\frac{1}{C_1}\right)=\frac{1}{2\pi\sigma}\ln\left(\frac ba\right)\qquad(\Omega\cdot\mathrm{m})$$

- ب. ظرفیت در واحد طول یک خط انتقال دوسیمه

$$C'_1=\frac{\pi\epsilon}{\cosh^{-1}\left(\dfrac{D}{2a}\right)}\qquad(\mathrm{F/m})$$

- مقاومت نشتی در واحد طول

$$\begin{aligned}R'_1&=\frac\epsilon\sigma\left(\frac{1}{C'_1}\right)=\frac{1}{\pi\sigma}\cosh^{-1}\left(\frac{D}{2a}\right)\\&=\frac{1}{\pi\sigma}\ln\left[\frac{D}{2a}+\sqrt{\left(\frac{D}{2a}\right)^2-1}\right]\qquad(\Omega\cdot\mathrm{m})\end{aligned}$$
:::
:::

- در وضعیت‌های خاصی مسائل الکتریسیته ساکن و جریان دائم دقیقاً مشابه هم نیستند.
- **روش اول** محاسبه مقاومت یک قطعه از ماده هادی بین دو سطح یا دو سر به صورت زیر است
    - انتخاب دستگاه مختصات مناسب
    - قرار دادن اختلاف پتانسیل $V_0$ بین دو سر هادی
    - یافتن شدت میدان الکتریکی (اگر ماده همگن باشد، حل معادله لاپلاس و بدست آوردن پتانسیل الکتریکی و سپس محاسبه شدت میدان الکتریکی)
    - یافتن جریان کل
$$I=\int_S\vect{J}\cdot d\vect{s}=\int_S\sigma\vect{E}\cdot d\vect{s}$$
    - $S$: سطح مقطعی که جریان از آن می گذرد
    - مقاومت برابر است با $V_0/I$

- **روش دوم** محاسبه مقاومت یک قطعه از ماده هادی بین دو سطح یا دو سر به صورت زیر است (در صورتیکه $J$ به سادگی از روی $I$ قابل تعیین باشد)
    - انتخاب دستگاه مختصات مناسب
    - قرار دادن جریان $I$ بین دو سر هادی
    - یافتن $J$ از روی $I$
    - محاسبه شدت میدان الکتریکی $\vect{E}=\vect{J}/\sigma$ و اختلاف پتانسیل $V_0$
$$V_0=-\int\vect{E}\cdot\dif\vect{\ell}$$
        - انتگرالگیری از سر با پتانسیل پایین تا سر با پتانسیل بالا انجام می‌گیرد.
    - مقاومت برابر است با $V_0/I$

::: {.example number="4-3"}
یک ماده هادی با ضخامت یکنواخت $h$ و رسانندگی $\sigma$ را به صورت شکل زیر در نظر بگیرید. مقاومت بین دو وجه انتهایی آن را بدست آورید.

```{.figure #m04-ex3 caption=""}
```

::: {.solution}
- انتخاب دستگاه مختصات استوانه ای

$$V=0\quad\text{at}\quad\phi=0,\qquad V=V_0\quad\text{at}\quad\phi=\pi/2$$
$$\frac{d^2V}{d\phi^2}=0\quad\Longrightarrow\quad V=c_1\phi+c_2\quad\Longrightarrow\quad V=\frac{2V_0}{\pi}\phi$$
$$\begin{aligned}\vect{J}=\sigma\vect{E}&=-\sigma\nabla V\\&=-\uvec{\phi}\sigma\frac{\partial V}{r\,\partial\phi}=-\uvec{\phi}\frac{2\sigma V_0}{\pi r}\end{aligned}$$
$$\begin{aligned}I=\int_S\vect{J}\cdot d\vect{s}&=\int_0^h\!\!\int_a^b\left(-\uvec{\phi}\frac{2\sigma V_0}{\pi r}\right)\cdot\left(-\uvec{\phi}\,dr\,dz\right)\\&=\frac{2\sigma hV_0}{\pi}\ln\frac ba\end{aligned}$$
$$R=\frac{V_0}{I}=\frac{\pi}{2\sigma h\ln(b/a)}$$
:::
:::
