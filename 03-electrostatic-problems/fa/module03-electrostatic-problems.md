# حل مسائل الکتریسیته ساکن

## سرفصل‌ها

```{.figure #m03-course-outline caption=""}
```

## حل مسائل الکتریسیته ساکن

- مسائل الکتریسیته ساکن مسائلی هستند که با تأثیرات بارهای الکتریکی در حال سکون سروکار دارند. حل این نوع مسائل معمولاً شامل تعیین پتانسیل الکتریکی، شدت میدان الکتریکی و یا توزیع بار الکتریکی است.
- در صورتیکه توزیع بار الکتریکی داده شده باشد، با استفاده از روابط فصل قبل هم پتانسیل و هم میدان الکتریکی قابل محاسبه خواهد بود.
    - در بسیاری از مسائل عملی توزیع دقیق بار در تمام نقاط معلوم نیست و یافتن پتانسیل و میدان الکتریکی مستقیماً با استفاده از فرمول‌های فصل قبل امکانپذیر نمی‌باشد. $\ELto$ امکان استفاده از روش تصاویر در دسته ای خاص از مسائل
    - در نوع دیگری از مسائل، پتانسیل تمام اجسام هادی معلوم است و می‌خواهیم پتانسیل و شدت میدان الکتریکی در فضای پیرامون و نیز توزیع بارهای سطحی را روی مرزهای هادی پیدا کنیم. $\ELto$ حل مسائل مقدار مرزی

```{.figure #m03-map caption=""}
```

- فرم معادلات پواسون و لاپلاس که بر پتانسیل الکتریکی حاکم هستند چگونه است و هرکدام در چه حالتی کاربرد دارند؟
- چگونه می توان با حل معادلات پواسون و لاپلاس، پتانسیل الکتریکی و شدت میدان الکتریکی را بدست آورد؟
- آیا جواب معادله پواسون که شرایط مرزی مشخصی را برآورده می کند یکتاست؟

## معادلات پواسون و لاپلاس

- دو معادله اصلی حاکم بر الکتریسیته ساکن در کلیه محیط‌ها

$$\nabla\cdot\vect{D}=\rho\qquad\qquad \nabla\times\vect{E}=0$$

- از طرفی داریم

$$\vect{E}=-\nabla V$$
$$\vect{D}=\epsilon\vect{E}\quad\Longrightarrow\quad\nabla\cdot\epsilon\vect{E}=\rho\quad\Longrightarrow\quad\nabla\cdot(\epsilon\nabla V)=-\rho$$

- اگر محیط همگن باشد ($\epsilon$ ثابت باشد)

::: {.important}
$$\nabla^2V=-\frac{\rho}{\epsilon}$$
:::

- $\rho$: چگالی بار آزاد
- در معادله فوق که به **معادله پواسون** معروف است، از عملگر **لاپلاسین** (دیورژانسِ گرادیان) استفاده شده است.

- لاپلاسین یک کمیت عددی در دستگاه‌های مختصات مختلف
    - کارتزین
$$\nabla^2V=\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}$$
    - استوانه ای
$$\nabla^2V=\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2V}{\partial\phi^2}+\frac{\partial^2V}{\partial z^2}$$
    - کروی
$$\nabla^2V=\frac{1}{R^2}\frac{\partial}{\partial R}\left(R^2\frac{\partial V}{\partial R}\right)+\frac{1}{R^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial V}{\partial\theta}\right)+\frac{1}{R^2\sin^2\theta}\frac{\partial^2V}{\partial\phi^2}$$

- حل معادله پواسون در فضای سه بعدی و با شرایط مرزی مشخص معمولاً کار ساده‌ای نیست.
- در نقاطی از یک محیط ساده که بار آزادی وجود ندارد

::: {.important}
$$\nabla^2V=0$$
:::

- معادله فوق **معادله لاپلاس** نامیده می‌شود.
    - این معادله حاکم بر مسائلی است که شامل مجموعه‌ای از هادی‌ها باشد که در پتانسیل‌های مختلف نگه داشته شوند.
    - وقتی با استفاده از این معادله $V$ بدست آمد، $\vect{E}$ و توزیع بار روی سطوح هادی نیز به سادگی بدست خواهند آمد

$$\vect{E}=-\nabla V\qquad\qquad \rho_s=-\epsilon E_n$$

::: {.example number="3-1"}
دو صفحه خازن صفحه ای موازی، به فاصله $d$ از یکدیگر قرار دارند و مطابق شکل زیر در پتانسیل های $0$ و $V_0$ نگه داشته می شوند. با چشم پوشی از میدان های حاشیه ای مطلوبست

- الف. پتانسیل در تمام نقاط بین صفحات
- ب. چگالی های بار سطحی روی صفحات

```{.figure #m03-ex1 caption=""}
```

::: {.solution}
- الف. استفاده از معادله لاپلاس

$$\nabla^2V=0\quad\Longrightarrow\quad\frac{d^2V}{dy^2}=0\quad\Longrightarrow\quad\frac{dV}{dy}=C_1\quad\Longrightarrow\quad V=C_1y+C_2$$

- شرایط مرزی:

$$\left.\begin{aligned}&\text{At }y=0,\quad V=0\\&\text{At }y=d,\quad V=V_0\end{aligned}\right\}\quad\Longrightarrow\quad V=\frac{V_0}{d}y$$

- ب.

$$\vect{E}=-\nabla V\quad\Longrightarrow\quad\vect{E}=-\uvec{y}\frac{dV}{dy}=-\uvec{y}\frac{V_0}{d}$$
$$E_n=\uvec{n}\cdot\vect{E}=\frac{\rho_s}{\epsilon}$$

- برای صفحه پایینی

$$\uvec{n}=\uvec{y},\qquad E_{n\ell}=-\frac{V_0}{d},\qquad \rho_{s\ell}=-\frac{\epsilon V_0}{d}$$

- برای صفحه بالایی

$$\uvec{n}=-\uvec{y},\qquad E_{nu}=\frac{V_0}{d},\qquad \rho_{su}=\frac{\epsilon V_0}{d}$$
:::
:::

::: {.example number="3-2"}
با حل معادله پواسون و لاپلاس نسبت به $V$، میدان $\vect{E}$ را درون و بیرون یک ابر الکترونی کروی با چگالی بار حجمی یکنواخت $\rho=-\rho_0$ در $0\leq R\leq b$ و $\rho=0$ در $R>b$ تعیین کنید.

::: {.solution}
- درون ابر الکترونی $\ELto$ استفاده از معادله پواسون

$$\nabla^2V=-\frac\rho\epsilon\quad\Longrightarrow\quad\frac{1}{R^2}\frac{d}{dR}\left(R^2\frac{dV_i}{dR}\right)=\frac{\rho_0}{\epsilon_0}\quad\Longrightarrow\quad\frac{d}{dR}\left(R^2\frac{dV_i}{dR}\right)=\frac{\rho_0}{\epsilon_0}R^2\quad\Longrightarrow\quad R^2\frac{dV_i}{dR}=\frac{\rho_0}{3\epsilon_0}R^3+C_1$$
$$\frac{dV_i}{dR}=\frac{\rho_0}{3\epsilon_0}R+\frac{C_1}{R^2}\quad\Longrightarrow\quad\vect{E}_i=-\nabla V_i=-\uvec{R}\left(\frac{dV_i}{dR}\right)$$

- با توجه به اینکه میدان در $R=0$ نمی تواند بی نهایت باشد

$$C_1=0\quad\Longrightarrow\quad\vect{E}_i=-\uvec{R}\frac{\rho_0}{3\epsilon_0}R,\qquad 0\leq R\leq b$$

- بیرون ابر الکترونی $\ELto$ استفاده از معادله لاپلاس

$$\nabla^2V=0\quad\Longrightarrow\quad\frac{1}{R^2}\frac{\partial}{\partial R}\left(R^2\frac{dV_o}{dR}\right)=0\quad\Longrightarrow\quad\frac{dV_o}{dR}=\frac{C_2}{R^2}$$
$$\vect{E}_o=-\nabla V_o=-\uvec{R}\frac{dV_o}{dR}=-\uvec{R}\frac{C_2}{R^2}$$

- با توجه به پیوستگی محیط، میدان های $\vect{E}_i$ و $\vect{E}_o$ در $R=b$ با هم برابرند

$$\frac{C_2}{b^2}=\frac{\rho_0}{3\epsilon_0}b\quad\Longrightarrow\quad C_2=\frac{\rho_0b^3}{3\epsilon_0}\quad\Longrightarrow\quad\vect{E}_o=-\uvec{R}\frac{\rho_0b^3}{3\epsilon_0R^2},\qquad R\geq b$$
:::
:::

## قضیه یکتایی

```{.figure #m03-map-unique caption=""}
```

- یک جواب معادله پواسون (و در حالت خاص معادله لاپلاس) که شرایط مرزی مفروضی را برآورده می‌کند، جواب یکتای معادله مذکور خواهد بود.
- نتیجه این قضیه آن است که یک جواب هر مسئله الکتریسیته ساکن که در شرایط مرزی صدق کند، بدون توجه به روش بدست آوردن آن جواب، تنها جواب ممکن است.

## روش تصاویر

```{.figure #m03-map-images caption=""}
```

- روش تصاویر چیست و چگونه می توان از این روش برای حل دسته ای خاص از مسائل الکتریسیته ساکن استفاده کرد؟

- در دسته‌ای از مسائل الکترومغناطیس، حل معادله لاپلاس به همراه برقراری شرایط مرزی بسیار مشکل است. اما در این مسائل می‌توان شرایط مرزی را به کمک **بارهای تصویر** ارضا کرد.
    - به این روش که عبارتست از جایگزینی سطوح مرزی با بارهای تصویرِ معادل **روش تصویر** گویند.
- به عنوان مثال مسئله زیر را در نظر می‌گیریم. می‌خواهیم پتانسیل را در تمام نقط $y>0$ بدست آوریم.

```{.figure #m03-image-problem caption=""}
```

- از قانون گوس نمی‌توان برای محاسبه میدان و سپس پتانسیل استفاده کرد زیرا تعیین سطح گوسی ممکن نیست.
- به صورت مستقیم نیز نمی توان پتانسیل را محاسبه کرد زیرا حضور بار مثبت $Q$ باعث القای بارهای منفی روی سطح هادی می‌شود و چگالی بار سطحی $\rho_s$ را نتیجه می‌دهد. داریم

$$V(x,y,z)=\frac{Q}{4\pi\epsilon_0\sqrt{x^2+(y-d)^2+z^2}}+\frac{1}{4\pi\epsilon_0}\int_S\frac{\rho_s}{R_1}\,ds$$

- مشکل اینجاست که ابتدا باید $\rho_s$ را بدست آوریم و حتی در صورت بدست آوردن $\rho_s$ محاسبه انتگرال سطحی مشکل خواهد بود.
- حل معادله لاپلاس برای دستیابی به جواب نیز غیرممکن یا بسیار مشکل است. در واقع جواب معادله لاپلاس باید شرایط زیر را برآورده کند

$$V(x,0,z)=0$$
$$V\to\frac{Q}{4\pi\epsilon_0R},\ \text{as}\ R\to0$$

- در فواصل بسیار دور از بار $Q$، پتانسیل باید صفر باشد

$$V(x,y,z)=V(-x,y,z)$$
$$V(x,y,z)=V(x,y,-z)$$

- می توان چنین مسئله ای را به سادگی با استفاده از روش تصاویر حل کرد.

### بار نقطه ای و صفحه هادی

- صفحه هادی را برمی‌داریم و آن را با بار نقطه‌ای تصویر $-Q$ در $y=-d$ جایگزین می‌کنیم

```{.figure #m03-image-plane caption=""}
```

::: {.important}
$$V(x,y,z)=\frac{Q}{4\pi\epsilon_0}\left(\frac{1}{R_+}-\frac{1}{R_-}\right)$$
$$R_+=\left[x^2+(y-d)^2+z^2\right]^{1/2},\qquad R_-=\left[x^2+(y+d)^2+z^2\right]^{1/2}$$
:::

- به سادگی می‌توان نشان داد که این جواب در معادله لاپلاس صدق کرده و شرایط مرزی را ارضا می‌کند. بنابراین این جواب یک جواب مسئله بوده و مطابق با قضیه یکتایی تنها جواب آن نیز می‌باشد.
- با بدست آوردن پتانسیل، محاسبه میدان و توزیع بار سطحی روی هادی آسان خواهد بود.

::: {.remark}
نکته‌ای که باید توجه شود این است که این روش نمی‌تواند برای محاسبه پتانسیل در نواحی $y<0$ بکار رود.
:::

### بار خطی و استوانه هادی موازی

```{.figure #m03-line-cylinder caption=""}
```

- هدف یافتن پتانسیل در خارج استوانه هادی است.
- تصویر باید یک بار خطی موازی در درون استوانه باشد تا سطح استوانه در $r=a$ را یک سطح هم‌پتانسیل کند. هدف یافتن $d_i$ و $\rho_i$ است.
- فرض می‌کنیم

::: {.important}
$$\rho_i=-\rho_\ell$$
:::

- پتانسیل در فاصله $r$ ناشی از بار خطی به چگالی $\rho_\ell$ با فرض مرجع در $r_0$ برابر است با

$$V=-\int_{r_0}^{r}E_r\,dr=-\frac{\rho_\ell}{2\pi\epsilon_0}\int_{r_0}^{r}\frac1r\,dr=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_0}{r}$$

- پتانسیل در نقطه $M$ روی سطح استوانه برابر است با

$$\begin{aligned}V_M&=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_0}{r}-\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_0}{r_i}\\&=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_i}{r}\end{aligned}$$

- بنابراین سطوح هم‌پتانسیل به صورت زیر مشخص می‌شوند

$$\frac{r_i}{r}=\text{Constant}$$

```{.figure #m03-similar-triangles caption=""}
```

- اگر شرط $\dfrac{d_i}{a}=\dfrac ad$ برقرار باشد، از تشابه بین دو مثلث $OMP_i$ و $OPM$ همواره نسبت $\dfrac{r_i}{r}$ ثابت خواهد بود. بنابراین

::: {.important}
$$d_i=\frac{a^2}{d}$$
:::

- به این ترتیب بار خطی $-\rho_\ell$ می‌تواند جایگزین سطح استوانه‌ای هادی شود و پتانسیل و میدان الکتریکی را هر نقطه خارج استوانه بدست آورد.

::: {.remark}
نکته‌ای که باید توجه شود این است که این روش نمی‌تواند برای محاسبه پتانسیل در نواحی درون استوانه هادی بکار رود.
:::

::: {.example number="3-3"}
ظرفیت در واحد طول بین دو سیم هادی دایروی موازی بسیار بلند به شعاع $a$ و فاصله $D$ را بدست آورید.

```{.figure #m03-ex3 caption=""}
```

::: {.solution}
- بارهای $+Q$ و $-Q$ را به ترتیب روی هادی های ۱ و ۲ قرار می دهیم.
- با استفاده از روش تصاویر می توان سطوح هم پتانسیل سیم ها را با دو بارخطی $+\rho_\ell$ و $-\rho_\ell$ جایگزین کرد.

$$V_2=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac ad$$
$$V_1=-\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac ad$$
$$C=\frac{\rho_\ell}{V_1-V_2}=\frac{\pi\epsilon_0}{\ln(d/a)}$$
$$d=D-d_i=D-\frac{a^2}{d}\quad\Longrightarrow\quad d=\tfrac12\left(D+\sqrt{D^2-4a^2}\right)$$
$$C=\frac{\pi\epsilon_0}{\ln\left[(D/2a)+\sqrt{(D/2a)^2-1}\right]}\qquad(\mathrm{F/m})$$

::: {.important}
$$C=\frac{\pi\epsilon_0}{\cosh^{-1}(D/2a)}\qquad(\mathrm{F/m})$$
:::
:::
:::

## مسائل مقدار مرزی

```{.figure #m03-map-bvp caption=""}
```

- روش تصاویر در حل مسائلی که شامل بار آزاد در نزدیکی مرزهای هادی با شکل هندسی ساده هستند، کاربرد دارد.
- اگر مسئله شامل دسته‌ای از هادی‌های نگه داشته شده در پتانسیل مشخص و بدون بار آزاد مجزا باشد، با روش تصاویر قابل حل نخواهد بود و نیاز به حل معادله لاپلاس است.
- معادله لاپلاس، یک معادله دیفرانسیل جزئی است. مسائلی را که از معادلات دیفرانسیل جزئی با شرایط مرزی مشخص پیروی می‌کنند، **مسائل مقدار مرزی** گویند.
- مسائل مقدار مرزی در توابع پتانسیل به دسته تقسیم می‌شوند
    - مسائل دیریشله: مقدار پتانسیل در تمام نقاط مرزها مشخص شده است.
    - مسائل نویمن: مشتق عمودی پتانسیل در تمام مرزها مشخص است.
    - مسائل مقدار مرزی ترکیبی: پتانسل در بعضی از نقاط مرزها و مشتق عمودی پتانسیل در بقیه نقاط مشخص شده است.

- نحوه حل مسائل مقدار مرزی در حوزه الکتریسیته ساکن در دستگاه های مختصات مختلف و برای دستیابی به توزیع پتانسیل چگونه است؟

### مختصات کارتزین

- معادله لاپلاس در مختصات کارتزین

$$\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}=0$$

- با استفاده از روش جداسازی متغیرها

$$V(x,y,z)=X(x)Y(y)Z(z)$$
$$Y(y)Z(z)\frac{d^2X(x)}{dx^2}+X(x)Z(z)\frac{d^2Y(y)}{dy^2}+X(x)Y(y)\frac{d^2Z(z)}{dz^2}=0$$
$$\underbrace{\frac{1}{X(x)}\frac{d^2X(x)}{dx^2}}_{-k_x^2}+\underbrace{\frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2}}_{-k_y^2}+\underbrace{\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}}_{-k_z^2}=0$$
$$k_x^2+k_y^2+k_z^2=0$$

::: {.important}
$$\frac{d^2X(x)}{dx^2}+k_x^2X(x)=0\qquad \frac{d^2Y(y)}{dy^2}+k_y^2Y(y)=0\qquad \frac{d^2Z(z)}{dz^2}+k_z^2Z(z)=0$$
:::

**\lr{Possible Solutions of $X''(x)+k_x^2X(x)=0$}**

| $k_x^2$ | $k_x$ | $X(x)$ | Exponential forms of $X(x)$ |
|---|---|---|---|
| $0$ | $0$ | $A_0x+B_0$ | |
| $+$ | $k$ | $A_1\sin kx+B_1\cos kx$ | $C_1e^{jkx}+D_1e^{-jkx}$ |
| $-$ | $jk$ | $A_2\sinh kx+B_2\cosh kx$ | $C_2e^{kx}+D_2e^{-kx}$ |


::: {.example number="3-4"}
دو صفحه هادی موازی زمین شده نیمه بینهایت به فاصله $d$ از هم قرار دارند. صفحه سوم عمود بر این دو صفحه و جدا از آن ها در پتانسیل $V_0$ نگه داشته می شود. توزیع پتانسیل را در ناحیه احاطه شده توسط این صفحات تعیین کنید.

```{.figure #m03-ex4 caption=""}
```

::: {.solution}
- شرایط مرزی

$$\text{(1)}\ \ V(x,y,z)=V(x,y)\qquad\text{(2)}\ \ V(0,y)=V_0\qquad\text{(3)}\ \ V(\infty,y)=0\qquad\text{(4)}\ \ V(x,0)=0\qquad\text{(5)}\ \ V(x,b)=0$$

$$\text{(1)}\quad\Longrightarrow\quad\frac{\partial V}{\partial z}=0\quad\Longrightarrow\quad Z(z)=B_0$$
$$\left.\begin{aligned}k_z^2&=-\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}=0\\k_x^2+k_y^2+k_z^2&=0\end{aligned}\right\}\quad k_y^2=-k_x^2=k^2\qquad(k\ \text{real})$$
$$k_x=jk\quad\Longrightarrow\quad X(x)=C_2e^{kx}+D_2e^{-kx}\quad\overset{(3)}{\Longrightarrow}\quad X(x)=D_2e^{-kx}$$
$$k_y=k\quad\Longrightarrow\quad Y(y)=A_1\sin ky+B_1\cos ky\quad\overset{(4)}{\Longrightarrow}\quad Y(y)=A_1\sin ky$$
$$\begin{aligned}V_n(x,y)&=(B_0D_2A_1)e^{-kx}\sin ky\\&=C_ne^{-kx}\sin ky\end{aligned}$$
$$\overset{(5)}{\Longrightarrow}\quad V_n(x,b)=C_ne^{-kx}\sin kb=0\quad\Longrightarrow\quad\sin kb=0\quad\Longrightarrow\quad kb=n\pi$$
$$k=\frac{n\pi}{b},\qquad n=1,2,3,\ldots$$
$$V_n(x,y)=C_ne^{-n\pi x/b}\sin\frac{n\pi}{b}y$$

- رابطه فوق در معادله لاپلاس صدق می کند اما به تنهایی نمی تواند شرط مرزی دوم در $x=0$ را برای همه $y$ ها از $0$ تا $b$ ارضا کند.
- از آنجا که معادله لاپلاس یک معادله دیفرانسیل جزیی خطی است، ترکیب $V_n$ هایی به فرم فوق و به ازای مقادیر مختلف $n$ نیز یک پاسخ خواهد بود.

$$V(x,y)=\sum_{n=1}^{\infty}V_n(x,y)$$

$$\overset{(2)}{\Longrightarrow}\quad\begin{aligned}V(0,y)&=\sum_{n=1}^{\infty}V_n(0,y)=\sum_{n=1}^{\infty}C_n\sin\frac{n\pi}{b}y\\&=V_0,\qquad 0<y<b\end{aligned}$$

- رابطه فوق بسط سری فوریه یک تابع متناوب و فرد است که در بازه $0<y<b$ مقدار آن $V_0$ می باشد.

```{.figure #m03-ex4-square caption=""}
```

::: {.remark title="یادآوری"}
$$f(t)=a_0+\sum_{n=1}^{\infty}\left[a_n\cos\left(\frac{2n\pi}{T}t\right)+b_n\sin\left(\frac{2n\pi}{T}t\right)\right]$$
$$b_n=\frac2T\int_{-T/2}^{T/2}f(t)\sin\left(\frac{2n\pi}{T}t\right)dt\qquad a_n=\frac2T\int_{-T/2}^{T/2}f(t)\cos\left(\frac{2n\pi}{T}t\right)dt\qquad a_0=\frac1T\int_{-T/2}^{T/2}f(t)\,dt$$
:::

$$\begin{aligned}C_n&=\frac{2}{2b}\left[\int_0^bV_0\sin\left(\frac{2n\pi}{2b}y\right)dy+\int_b^{2b}-V_0\sin\left(\frac{2n\pi}{2b}y\right)dy\right]\\&=\frac{V_0}{n\pi}(-2\cos n\pi+2)=\begin{cases}\dfrac{4V_0}{n\pi}&\text{if }n\text{ is odd}\\[2mm]0&\text{if }n\text{ is even}\end{cases}\end{aligned}$$

::: {.important}
$$\begin{aligned}V(x,y)&=\sum_{n=1}^{\infty}C_ne^{-n\pi x/b}\sin\frac{n\pi}{b}y\\&=\frac{4V_0}{\pi}\sum_{n=\text{odd}}^{\infty}\frac1ne^{-n\pi x/b}\sin\frac{n\pi}{b}y,\end{aligned}$$
$$n=1,3,5,\ldots,\qquad x>0\quad\text{and}\quad 0<y<b$$
:::
:::
:::

### مختصات استوانه ای

- معادله لاپلاس در مختصات استوانه ای

$$\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2V}{\partial\phi^2}+\frac{\partial^2V}{\partial z^2}=0$$

- با فرض بزرگ بودن بعد طولی در مقایسه با شعاع، در هندسه استوانه ای، پتانسیل مستقل از $z$ است.

$$\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2V}{\partial\phi^2}=0$$

- با استفاده از روش جداسازی متغیرها

$$V(r,\phi)=R(r)\Phi(\phi)$$
$$\underbrace{\frac{r}{R(r)}\frac{d}{dr}\left[r\frac{dR(r)}{dr}\right]}_{k^2}+\underbrace{\frac{1}{\Phi(\phi)}\frac{d^2\Phi(\phi)}{d\phi^2}}_{-k^2}=0$$

- معادله دیفرانسیل برحسب $\phi$

::: {.important}
$$\frac{d^2\Phi(\phi)}{d\phi^2}+k^2\Phi(\phi)=0$$
:::

- **وقتی $k\neq0$**
    - در شکل‌بندی‌های استوانه‌ای مدور، توابع پتانسیل و در نتیجه $\Phi(\phi)$ نسبت به $\phi$ متناوب بوده و توابع هذلولوی بکار نمی‌روند.
        - اگر دامنه $\phi$ محدود نشده باشد، $k$ باید عدد صحیح باشد ($k=n$)

$$\Phi(\phi)=A_\phi\sin n\phi+B_\phi\cos n\phi$$

- معادله دیفرانسیل برحسب $r$ (معادله اویلر)

$$r^2\frac{d^2R(r)}{dr^2}+r\frac{dR(r)}{dr}-n^2R(r)=0$$
$$R(r)=A_rr^n+B_rr^{-n}$$

::: {.important}
$$V_n(r,\phi)=r^n(A_n\sin n\phi+B_n\cos n\phi)+r^{-n}(A'_n\sin n\phi+B'_n\cos n\phi),\qquad n\neq0$$
:::

- هنگامیکه ناحیه مورد نظر شامل $r=0$ باشد، جملات شامل $r^{-n}$ و هنگامیکه ناحیه مورد نظر شامل بی‌نهایت باشد، جملات شامل $r^n$ نمی‌توانند وجود داشته باشند.

- **وقتی $k=0$**

$$\frac{d^2\Phi(\phi)}{d\phi^2}=0$$
$$\Phi(\phi)=A_0\phi+B_0\quad\Longrightarrow\quad\Phi(\phi)=B_0$$

- اگر هیچ تغییرات پیرامونی وجود نداشته باشد

$$\frac{d}{dr}\left[r\frac{dR(r)}{dr}\right]=0$$
$$R(r)=C_0\ln r+D_0$$

::: {.example number="3-5"}
یک کابل هم محور بسیار بلند را در نظر بگیرید. شعاع هادی داخلی $a$ و در پتانسیل $V_0$ نگه داشته شده است. هادی خارجی دارای شعاع $b$ بوده و زمین شده است. توزیع پتانسیل در فضای بین دو هادی را بدست آورید.

```{.figure #m03-ex5 caption=""}
```

::: {.solution}
- با توجه به بلند بودن کابل، وابستگی به $z$ وجود ندارد.
- با توجه به تقارن، وابستگی به $\phi$ وجود ندارد ($k=0$).

$$V(r)=C_1\ln r+C_2$$
$$V(b)=0,\qquad V(a)=V_0$$
$$C_1=-\frac{V_0}{\ln(b/a)},\qquad C_2=\frac{V_0\ln b}{\ln(b/a)}\qquad\Longrightarrow\qquad V(r)=\frac{V_0}{\ln(b/a)}\ln\left(\frac br\right)$$
:::
:::

::: {.example number="3-6"}
دو صفحه هادی نیمه بینهایت مطابق شکل زیر در پتانسیل های $V_0$ و صفر نگه داشته شده اند. با فرض اینکه طول این صفحات در امتداد محور $z$ بسیار بلند باشد، توزیع پتانسیل را در کل فضا بدست آورید.

```{.figure #m03-ex6 caption=""}
```

::: {.solution}
- با توجه به بلند بودن صفحات، وابستگی به $z$ وجود ندارد.
- وابستگی به $r$ وجود ندارد ($k=0$).

$$\Phi(\phi)=A_0\phi+B_0$$
$$V(\phi)=\begin{cases}0&\phi=0,2\pi\\V_0&\phi=\alpha\end{cases}$$

- $0\leq\phi\leq\alpha$

$$V(\phi)=\frac{V_0}{\alpha}\phi$$

- $\alpha\leq\phi\leq2\pi$

$$V(\phi)=\frac{V_0}{2\pi-\alpha}(2\pi-\phi)$$
:::
:::

::: {.example number="3-7"}
یک لوله هادی استوانه ای نازک بسیار بلند به شعاع $b$ به دو بخش تقسیم شده است. نیمه بالایی در پتانسیل $V_0$ و نیمه پایینی در پتانسیل $-V_0$ نگه داشته شده است. توزیع پتانسیل درون و بیرون لوله را بدست آورید.

```{.figure #m03-ex7 caption=""}
```

::: {.solution}
- با توجه به بلند بودن لوله وابستگی به $z$ وجود ندارد.

$$V_n(r,\phi)=r^n(A_n\sin n\phi+B_n\cos n\phi)+r^{-n}(A'_n\sin n\phi+B'_n\cos n\phi)$$
$$V(b,\phi)=\begin{cases}V_0&\text{for }0<\phi<\pi\\-V_0&\text{for }\pi<\phi<2\pi\end{cases}$$

- درون لوله ($r<b$)
    - با توجه به اینکه ناحیه مورد نظر شامل $r=0$ است، جملات شامل $r^{-n}$ نمی‌توانند وجود داشته باشند.
    - با توجه به اینکه $V(r,\phi)$ یک تابع فرد از $\phi$ است، بنابراین

$$V_n(r,\phi)=A_nr^n\sin n\phi$$

- عبارت فوق به تنهایی نمی تواند شرایط مرزی را برآورده کند. بنابراین

$$\begin{aligned}V(r,\phi)&=\sum_{n=1}^{\infty}V_n(r,\phi)\\&=\sum_{n=1}^{\infty}A_nr^n\sin n\phi\end{aligned}$$
$$\sum_{n=1}^{\infty}A_nb^n\sin n\phi=\begin{cases}V_0&\text{for }0<\phi<\pi\\-V_0&\text{for }\pi<\phi<2\pi\end{cases}$$

- رابطه فوق بسط سری فوریه یک تابع متناوب و فرد است که در بازه $0<\phi<\pi$ مقدار آن $V_0$ و در بازه $\pi<\phi<2\pi$ مقدار آن $-V_0$ می باشد.

$$A_n=\begin{cases}\dfrac{4V_0}{n\pi b^n}&\text{if }n\text{ is odd}\\[2mm]0&\text{if }n\text{ is even}\end{cases}\qquad\qquad V(r,\phi)=\frac{4V_0}{\pi}\sum_{n=\text{odd}}^{\infty}\frac1n\left(\frac rb\right)^n\sin n\phi,\qquad r<b$$

- بیرون لوله ($r>b$)
    - با توجه به اینکه ناحیه مورد نظر شامل $r\to\infty$ است، جملات شامل $r^n$ نمی‌توانند وجود داشته باشند.
    - $V(r,\phi)$ یک تابع فرد از $\phi$ است.
    - یک عبارت به تنهایی نمی تواند شرایط مرزی را برآورده کند. بنابراین

$$\begin{aligned}V(r,\phi)&=\sum_{n=1}^{\infty}V_n(r,\phi)\\&=\sum_{n=1}^{\infty}B'_nr^{-n}\sin n\phi\end{aligned}\qquad\begin{aligned}V(b,\phi)&=\sum_{n=1}^{\infty}B'_nb^{-n}\sin n\phi\\&=\begin{cases}V_0&\text{for }0<\phi<\pi\\-V_0&\text{for }\pi<\phi<2\pi\end{cases}\end{aligned}$$
$$B'_n=\begin{cases}\dfrac{4V_0b^n}{n\pi}&\text{if }n\text{ is odd}\\[2mm]0&\text{if }n\text{ is even}\end{cases}$$

::: {.important}
$$V(r,\phi)=\frac{4V_0}{\pi}\sum_{n=\text{odd}}^{\infty}\frac1n\left(\frac br\right)^n\sin n\phi,\qquad r>b$$
:::
:::
:::
