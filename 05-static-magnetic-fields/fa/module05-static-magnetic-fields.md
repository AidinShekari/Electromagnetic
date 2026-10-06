# میدان‌های مغناطیسی ساکن

## سرفصل‌ها

```{.figure #m05-course-outline caption=""}
```

## میدان‌های مغناطیسی ساکن

- هنگامیکه بار آزمون کوچکی در میدان الکتریکی $\vect{E}$ قرار می‌گیرد، نیروی زیر به آن وارد می‌شود

$$\vect{F}_e=q\vect{E}\qquad(\mathrm{N})$$

- هنگامیکه این بار آزمون، در حال حرکت درون یک میدان مغناطیسی باشد، نیروی دیگری به آن وارد می‌شود که برابر است با

$$\vect{F}_m=q\vect{u}\times\vect{B}\qquad(\mathrm{N})$$

- $\vect{B}$: چگالی شار مغناطیسی با واحد وبر بر متر مربع یا تسلا
- پس نیروی الکترومغناطیسی کل وارد بر بار $q$ برابر است با

::: {.important title="معادله نیروی لورنتس"}
$$\vect{F}=q(\vect{E}+\vect{u}\times\vect{B})\qquad(\mathrm{N})$$
:::

```{.figure #m05-map caption=""}
```

- فرضیات اصلی مغناطیس ساکن که بر اساس آن‌ها می‌توان دیگر روابط و قوانین این حوزه را استخراج کرد کدامند؟
- چگونه بر اساس فرضیات فوق، **قانون مداری آمپر** استخراج می‌شود؟
- چگونه می‌توان با استفاده از قانون مداری آمپر، چگالی شار مغناطیسی ناشی از یک جریان را بدست آورد؟

## فرضیات اصلی مغناطیس ساکن در فضای آزاد

- دو فرض اساسی مغناطیس ساکن در فضای آزاد

::: {.important}
$$\nabla\cdot\vect{B}=0$$
$$\nabla\times\vect{B}=\mu_0\vect{J}$$
:::

- $\mu_0=4\pi\times10^{-7}\,\mathrm{(H/m)}$: ضریب نفوذپذیری فضای آزاد
- $\vect{J}$: چگالی حجمی جریان $\mathrm{(A/m^2)}$
- چون دیورژانس کرل هر میدان برداری صفر است، در نتیجه

$$\nabla\cdot\vect{J}=0$$

- برای چگالی بار الکتریکی هیچ مشابه مغناطیسی وجود ندارد.
- شکل انتگرالی رابطه اول $\ELto$ انتگرالگیری روی حجم دلخواه $V$ و استفاده از قضیه دیورژانس

::: {.important title="قانون بقای شار مغناطیسی"}
$$\oint_S\vect{B}\cdot d\vect{s}=0$$
:::

- این معادله را **قانون بقای شار مغناطیسی** می‌نامند.
    - هیچ منبع شار مغناطیسی وجود ندارد و خطوط شار مغناطیسی همیشه در خود بسته می‌شوند.
- شکل انتگرالی رابطه دوم $\ELto$ انتگرالگیری روی سطح باز دلخواه $S$ و استفاده از قضیه استوکس

$$\int_S(\nabla\times\vect{B})\cdot d\vect{s}=\mu_0\int_S\vect{J}\cdot d\vect{s}$$

::: {.important title="قانون مداری آمپر"}
$$\oint_C\vect{B}\cdot\dif\vect{\ell}=\mu_0I$$
:::

- $C$: مسیر محصور کننده سطح $S$ (مسیر $C$ و جریان $I$ از قانون دست راست تبعیت می‌کنند)
- $I$: جریان گذرنده از سطح $S$
- این معادله شکلی از **قانون مداری آمپر** است.
    - گردش چگالی شار مغناطیسی در فضای آزاد به دور هر مسیر بسته، برابر با حاصلضرب $\mu_0$ در کل جریان گذرنده از سطح محصور شده توسط این مسیر است.
- قانون مداری آمپر در تعیین چگالی شار مغناطیسی ناشی از جریان $I$ هنگامیکه مسیر بسته $C$ به دور جریان چنان وجود داشته باشد که $\vect{B}$ روی مسیر ثابت باشد، مفید است.

::: {.example number="5-1"}
یک هادی بسیار بلند مستقیم با سطح مقطع دایروی به شعاع $b$ حامل جریان $I$ است. چگالی شار مغناطیسی درون و بیرون هادی را بدست آورید.

```{.figure #m05-ex1 caption=""}
```

::: {.solution}
- اگر هادی در امتداد محور $z$ باشد، $\vect{B}$ در راستای $\phi$ بوده و مقدار آن در امتداد هر مسیر دایروی حول محور $z$ ثابت است.
    - درون هادی

$$\left.\begin{aligned}&\vect{B}_1=\uvec{\phi}B_{\phi1},\qquad\dif\vect{\ell}=\uvec{\phi}r_1\,d\phi\\&\oint_{C_1}\vect{B}_1\cdot\dif\vect{\ell}=\int_0^{2\pi}B_{\phi1}r_1\,d\phi=2\pi r_1B_{\phi1}\\&I_1=\frac{\pi r_1^2}{\pi b^2}I=\left(\frac{r_1}{b}\right)^2I\end{aligned}\right\}\quad\vect{B}_1=\uvec{\phi}B_{\phi1}=\uvec{\phi}\frac{\mu_0r_1I}{2\pi b^2}$$

- بیرون هادی

$$\vect{B}_2=\uvec{\phi}B_{\phi2},\qquad\dif\vect{\ell}=\uvec{\phi}r_2\,d\phi$$
$$\oint_{C_2}\vect{B}_2\cdot\dif\vect{\ell}=2\pi r_2B_{\phi2}$$
$$\vect{B}_2=\uvec{\phi}B_{\phi2}=\uvec{\phi}\frac{\mu_0I}{2\pi r_2}$$
:::
:::

::: {.example number="5-2"}
چگالی شار مغناطیسی درون یک سیم پیچ چنبره‌ای با هسته هوا و $N$ دور سیمِ حامل جریان $I$ را بدست آورید.

```{.figure #m05-ex2 caption=""}
```

::: {.solution}
- تقارن استوانه‌ای تضمین می‌کند که $\vect{B}$ فقط مولفه در راستای $\phi$ دارد و مقدار آن در امتداد هر مسیر دایروی حول محور سیم پیچ ثابت است.

$$\oint\vect{B}\cdot\dif\vect{\ell}=2\pi rB_\phi=\mu_0NI$$
$$\vect{B}=\uvec{\phi}B_\phi=\uvec{\phi}\frac{\mu_0NI}{2\pi r},\qquad(b-a)<r<(b+a)$$
:::
:::

::: {.example number="5-3"}
چگالی شار مغناطیسی درون یک سیم پیچ بسیار بلند با هسته هوا و $n$ دور سیم در واحد طول حامل جریان $I$ را بدست آورید.

```{.figure #m05-ex3 caption=""}
```

::: {.solution}
- خارج از سیم پیچ میدان مغناطیسی صفر است.
- با توجه به تقارن ساختار، $\vect{B}$ هم‌راستا با محور سیم پیچ بوده و مقدار آن در امتداد سیم پیچ ثابت است.

$$BL=\mu_0nLI$$
$$B=\mu_0nI$$
:::
:::

## پتانسیل مغناطیسی برداری

```{.figure #m05-map-vecpot caption=""}
```

- مفهوم پتانسیل مغناطیسی برداری چیست، کاربرد آن کجاست و چگونه محاسبه می‌شود؟
- رابطه قانون بیوساوار و نحوه استفاده از آن برای محاسبه چگالی شار مغناطیسی چگونه است؟

$$\nabla\cdot\vect{B}=0\quad\Longrightarrow\quad\boxed{\vect{B}=\nabla\times\vect{A}\qquad(\mathrm{T})}$$

- $\vect{A}$ را **پتانسیل مغناطیسی برداری** می‌نامند. واحد آن وبر بر متر است.
    - اگر بتوانیم در مورد یک توزیع جریان، $\vect{A}$ را بیابیم، آنگاه به سادگی $\vect{B}$ قابل محاسبه خواهد بود (دقیقاً مانند $V$ و $\vect{E}$).
- تعریف یک بردار به مشخص کردن کرل و دیورژانس آن نیاز دارد. برای مشخص کردن دیورژانس $\vect{A}$ به ترتیب زیر عمل می‌کنیم

$$\nabla\times\vect{B}=\mu_0\vect{J}\quad\Longrightarrow\quad\nabla\times\nabla\times\vect{A}=\mu_0\vect{J}$$

- **لاپلاسین یک کمیت برداری** را به صورت زیر تعریف می‌کنیم

$$\nabla^2\vect{A}=\nabla(\nabla\cdot\vect{A})-\nabla\times\nabla\times\vect{A}$$

- به عنوان مثال لاپلاسین $\vect{A}$ در دستگاه مختصات کارتزین به صورت زیر است

$$\nabla^2\vect{A}=\uvec{x}\nabla^2A_x+\uvec{y}\nabla^2A_y+\uvec{z}\nabla^2A_z$$

- بنابراین

$$\nabla(\nabla\cdot\vect{A})-\nabla^2\vect{A}=\mu_0\vect{J}$$

- برای ساده شدن رابطه فوق انتخاب می‌کنیم

$$\nabla\cdot\vect{A}=0\quad\Longrightarrow\quad\boxed{\nabla^2\vect{A}=-\mu_0\vect{J}}$$

- رابطه اخیر **معادله برداری پواسون** است.
- در مختصات کارتزین داریم

$$\nabla^2A_x=-\mu_0J_x,\qquad\nabla^2A_y=-\mu_0J_y,\qquad\nabla^2A_z=-\mu_0J_z$$

- هر کدام از این سه معادله از نظر ریاضی شبیه معادله پواسون در الکتریسیته ساکن هستند.
- پیش از این داشتیم

$$\nabla^2V=-\frac{\rho}{\epsilon_0}\quad\Longrightarrow\quad V=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho}{\lvert\vect{R}-\vect{R}'\rvert}\,dv'$$

- به طور مشابه خواهیم داشت

::: {.important}
$$\vect{A}=\frac{\mu_0}{4\pi}\int_{V'}\frac{\vect{J}}{\lvert\vect{R}-\vect{R}'\rvert}\,dv'$$
:::

- به این ترتیب می‌توان با استفاده از رابطه فوق، $\vect{A}$ را از روی چگالی جریان بدست آورد و سپس با گرفتن کرل از آن، $\vect{B}$ را محاسبه نمود.
- مفهوم فیزیکی پتانسیل مغناطیسی برداری

$$\Phi=\int_S\vect{B}\cdot d\vect{s}$$

- $\Phi$: شار مغناطیسی با واحد وبر

::: {.important}
$$\Phi=\int_S(\nabla\times\vect{A})\cdot d\vect{s}=\oint_C\vect{A}\cdot\dif\vect{\ell}\qquad(\mathrm{Wb})$$
:::

- انتگرال خطی $\vect{A}$ به دور هر مسیر بسته $C$، برابر با کل شار مغناطیسی گذرنده از سطح محصور شده توسط این مسیر است.

## قانون بیوساوار

```{.figure #m05-map-biot caption=""}
```

- در یک سیم نازک حامل جریان $I$ و با سطح مقطع $S$ داریم

$$\vect{J}\,dv'=JS\,d\ell'=I\,\dif\vect{\ell}'\quad\Longrightarrow\quad\vect{A}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}$$

- می‌توان نشان داد

$$\vect{B}=\nabla\times\vect{A}=\nabla\times\left[\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}\right]$$

::: {.important title="قانون بیوساوار"}
$$\vect{B}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'\times(\vect{R}-\vect{R}')}{\lvert\vect{R}-\vect{R}'\rvert^3}$$
:::

- معادله فوق را **قانون بیوساوار** گویند.
    - به طور کلی استفاده از قانون بیوساوار مشکل‌تر از قانون مداری آمپر است. اما اگر مسیر بسته‌ای که $\vect{B}$ روی آن ثابت باشد پیدا نشود، استفاده از قانون مداری آمپر برای تعیین $\vect{B}$ امکان‌پذیر نیست.

::: {.example number="5-4"}
جریان مستقیم $I$ در یک سیم مستقیم به طول $2L$ جاری است. چگالی شار مغناطیسی را در نقطه‌ای به فاصله $r$ از سیم در صفحه عمود منصف آن تعیین کنید.

```{.figure #m05-ex4 caption=""}
```

::: {.solution}
- جریان فقط در مدارهای بسته وجود دارد. بنابراین سیم موجود در این مثال باید بخشی از یک حلقه حامل جریان باشد. چون از بقیه مدار اطلاعی نداریم، بنابراین نمی‌توان از قانون مداری آمپر استفاده کرد.
- **روش اول حل**

$$\left.\begin{aligned}&\vect{A}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}\\&\dif\vect{\ell}'=dz'\,\uvec{z}\\&\vect{R}=r\uvec{r}\\&\vect{R}'=z'\uvec{z}\end{aligned}\right\}\quad\begin{aligned}\vect{A}&=\uvec{z}\frac{\mu_0I}{4\pi}\int_{-L}^{L}\frac{dz'}{\sqrt{z'^2+r^2}}\\&=\uvec{z}\frac{\mu_0I}{4\pi}\ln\frac{\sqrt{L^2+r^2}+L}{\sqrt{L^2+r^2}-L}\end{aligned}$$
$$\vect{B}=\nabla\times\vect{A}=\nabla\times(\uvec{z}A_z)=\uvec{r}\frac1r\frac{\partial A_z}{\partial\phi}-\uvec{\phi}\frac{\partial A_z}{\partial r}$$
$$\begin{aligned}\vect{B}&=-\uvec{\phi}\frac{\partial}{\partial r}\left[\frac{\mu_0I}{4\pi}\ln\frac{\sqrt{L^2+r^2}+L}{\sqrt{L^2+r^2}-L}\right]\\&=\uvec{\phi}\frac{\mu_0IL}{2\pi r\sqrt{L^2+r^2}}\end{aligned}$$

- **روش دوم حل**

$$\left.\begin{aligned}&\vect{B}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'\times(\vect{R}-\vect{R}')}{\lvert\vect{R}-\vect{R}'\rvert^3}\\&\vect{R}-\vect{R}'=r\uvec{r}-z'\uvec{z}\\&\dif\vect{\ell}'\times(\vect{R}-\vect{R}')=dz'\uvec{z}\times(r\uvec{r}-z'\uvec{z})=r\,dz'\,\uvec{\phi}\end{aligned}\right\}\quad\begin{aligned}\vect{B}=\int d\vect{B}&=\uvec{\phi}\frac{\mu_0I}{4\pi}\int_{-L}^{L}\frac{r\,dz'}{(z'^2+r^2)^{3/2}}\\&=\uvec{\phi}\frac{\mu_0IL}{2\pi r\sqrt{L^2+r^2}}\end{aligned}$$
:::
:::

::: {.example number="5-5"}
چگالی شار مغناطیسی در مرکز یک حلقه مربعی به ضلع $w$ و حامل جریان $I$ را بدست آورید.

```{.figure #m05-ex5 caption=""}
```

::: {.solution}
- فرض می‌کنیم که حلقه در صفحه $xy$ باشد. $\vect{B}$ در مرکز حلقه، چهار برابر چگالی شار مغناطیسی ناشی از یک ضلع به طول $w$ است. بنابراین
- اندازه چگالی شار مغناطیسی یک تکه سیم به طول $2L$ در فاصله $r$ از آن

$$B=\frac{\mu_0IL}{2\pi r\sqrt{L^2+r^2}}\qquad L=\frac w2,\quad r=\frac w2$$
$$\vect{B}=\uvec{z}\frac{\mu_0I}{\sqrt2\pi w}\times4=\uvec{z}\frac{2\sqrt2\mu_0I}{\pi w}$$
:::
:::

::: {.example number="5-6"}
چگالی شار مغناطیسی روی محور یک حلقه جریان دایروی به شعاع $b$ و حامل جریان $I$ را بدست آورید.

```{.figure #m05-ex6 caption=""}
```

::: {.solution}
$$\left.\begin{aligned}&\vect{B}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'\times(\vect{R}-\vect{R}')}{\lvert\vect{R}-\vect{R}'\rvert^3}\\&\dif\vect{\ell}'=b\,d\phi'\,\uvec{\phi'},\quad\vect{R}=z\uvec{z},\quad\vect{R}'=b\uvec{r'}\\&\vect{R}-\vect{R}'=z\uvec{z}-b\uvec{r'}\\&\begin{aligned}\dif\vect{\ell}'\times(\vect{R}-\vect{R}')&=b\,d\phi'\,\uvec{\phi'}\times(z\uvec{z}-b\uvec{r'})\\&=bz\,d\phi'\,\uvec{r'}+b^2d\phi'\,\uvec{z}\end{aligned}\end{aligned}\right\}\quad\vect{B}=\frac{\mu_0I}{4\pi}\int_0^{2\pi}\uvec{z}\frac{b^2\,d\phi'}{(z^2+b^2)^{3/2}}$$

- به صورت شهودی واضح است که مؤلفه $r$ چگالی شار مغناطیسی صفر است.

::: {.important}
$$\vect{B}=\uvec{z}\frac{\mu_0Ib^2}{2(z^2+b^2)^{3/2}}\qquad(\mathrm{T})$$
:::
:::
:::

::: {.example number="5-7"}
چگالی شار مغناطیسی ناشی از یک دوقطبی مغناطیسی به شعاع $b$ و حامل جریان $I$ را به فاصله بسیار دور از آن بدست آورید.

```{.figure #m05-ex7 caption=""}
```

::: {.solution}
$$\vect{A}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}$$

- با توجه به تقارن هندسه، میدان مغناطیسی مستقل از زاویه $\phi$ است. بنابراین جهت سادگی نقطه مشاهده را در صفحه $yz$ قرار می‌دهیم.

$$\dif\vect{\ell}'=b\,d\phi'\,\uvec{\phi'}=b\,d\phi'\left(-\uvec{x}\sin\phi'+\uvec{y}\cos\phi'\right)$$
$$\vect{A}=-\uvec{x}\frac{\mu_0I}{4\pi}\int_0^{2\pi}\frac{b\sin\phi'}{\lvert\vect{R}-\vect{R}'\rvert}\,d\phi'+\uvec{y}\frac{\mu_0I}{4\pi}\int_0^{2\pi}\frac{b\cos\phi'}{\lvert\vect{R}-\vect{R}'\rvert}\,d\phi'$$

- به صورت شهودی روشن است که مؤلفه $\vect{A}$ در راستای $y$ صفر است.

```{.figure #m05-ex7-top caption=""}
```

$$\begin{aligned}\vect{R}=R\uvec{R}&=R\left(\sin\theta\cos(\pi/2)\uvec{x}+\sin\theta\sin(\pi/2)\uvec{y}+\cos\theta\,\uvec{z}\right)\\&=R\left(\sin\theta\,\uvec{y}+\cos\theta\,\uvec{z}\right)\end{aligned}$$
$$\vect{R}'=b\uvec{r'}=b\left(\cos\phi'\,\uvec{x}+\sin\phi'\,\uvec{y}\right)$$
$$\vect{R}-\vect{R}'=-b\cos\phi'\,\uvec{x}+(R\sin\theta-b\sin\phi')\uvec{y}+R\cos\theta\,\uvec{z}$$
$$\begin{aligned}\lvert\vect{R}-\vect{R}'\rvert^2&=R^2+b^2-2bR\sin\theta\sin\phi'\\&=R^2\left(1+\frac{b^2}{R^2}-\frac{2b}{R}\sin\theta\sin\phi'\right)\end{aligned}$$
$$\begin{aligned}\frac{1}{\lvert\vect{R}-\vect{R}'\rvert}&=\frac1R\left(1+\frac{b^2}{R^2}-\frac{2b}{R}\sin\theta\sin\phi'\right)^{-1/2}\\&\cong\frac1R\left(1-\frac{2b}{R}\sin\theta\sin\phi'\right)^{-1/2}\cong\frac1R\left(1+\frac bR\sin\theta\sin\phi'\right)\end{aligned}$$
$$\begin{aligned}\vect{A}&=-\uvec{x}\frac{\mu_0Ib}{4\pi R}\int_0^{2\pi}\left(1+\frac bR\sin\theta\sin\phi'\right)\sin\phi'\,d\phi'\\&=-\uvec{x}\frac{\mu_0Ib^2}{4R^2}\sin\theta\end{aligned}$$

- حال در هر نقطه مشاهده دلخواهی بردار پتانسل مغناطیسی به صورت زیر خواهد شد

$$\vect{A}=\uvec{\phi}\frac{\mu_0Ib^2}{4R^2}\sin\theta\quad\Longrightarrow\quad\vect{A}=\uvec{\phi}\frac{\mu_0(I\pi b^2)}{4\pi R^2}\sin\theta$$

- بردار گشتاور دوقطبی مغناطیسی

$$\vect{m}=\uvec{z}I\pi b^2=\uvec{z}IS=\uvec{z}m$$

::: {.important}
$$\vect{A}=\frac{\mu_0\vect{m}\times\uvec{R}}{4\pi R^2}$$
:::

$$\vect{B}=\nabla\times\vect{A}\quad\Longrightarrow\quad\vect{B}=\frac{\mu_0Ib^2}{4R^3}\left(\uvec{R}2\cos\theta+\uvec{\theta}\sin\theta\right)$$

::: {.important}
$$\vect{B}=\frac{\mu_0m}{4\pi R^3}\left(\uvec{R}2\cos\theta+\uvec{\theta}\sin\theta\right)$$
:::

```{.figure #m05-dipoles caption=""}
```
:::
:::

## رفتار میدان مغناطیسی ساکن در محیط‌های مادی

```{.figure #m05-map-media caption=""}
```

- تمام مواد از اتم‌هایی با هسته با بار مثبت و تعدادی الکترون با بار منفی در حال گردش به دور آن تشکیل می‌شوند.
- حرکت الکترون‌ها باعث تولید جریان گردان و در نتیجه دوقطبی‌های مغناطیسی میکروسکوپی می‌شود.
- در غیاب میدان مغناطیسی خارجی، دو قطبی‌های مغناطیسی اتم‌های اکثر مواد (به جز آهنربای دائمی) دارای جهت‌های تصادفی هستند و هیچ گشتاور مغناطیسی خالصی ایجاد نمی‌شود. با اعمال میدان مغناطیسی خارجی، گشتاور مغناطیسی الکترون‌های چرخان هم‌امتداد می‌شوند.
- مواد مختلف در معرض میدان مغناطیسی چه رفتاری از خود نشان می‌دهند و چگونه می‌توان این رفتار را تحلیل کرد؟

### مغناطیس‌شدگی و چگالی جریان‌های معادل

```{.figure #m05-magnetization caption=""}
```

- بردار مغناطیس شدگی (و بردار قطبی شدگی در الکتریسیته ساکن)

$$\vect{M}=\lim_{\Delta v\to0}\frac{\sum_{k=1}^{n\Delta v}\vect{m}_k}{\Delta v}\quad(\mathrm{A/m})\qquad\qquad\vect{P}=\lim_{\Delta v\to0}\frac{\sum_{k=1}^{n\Delta v}\vect{p}_k}{\Delta v}\quad(\mathrm{C/m^2})$$

- پتانسیل مغناطیسی برداری ناشی از ماده مغناطیس شده (و پتانسیل الکتریکی ناشی از ماده قطبی شده)

$$\vect{A}=\frac{\mu_0}{4\pi}\int_{V'}\frac{\nabla'\times\vect{M}}{R}\,dv'+\frac{\mu_0}{4\pi}\oint_{S'}\frac{\vect{M}\times\uvec{n}'}{R}\,ds'$$
$$V=\frac{1}{4\pi\epsilon_0}\oint_{S'}\frac{\vect{P}\cdot\uvec{n}'}{R}\,ds'+\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{(-\nabla'\cdot\vect{P})}{R}\,dv'$$

- چگالی جریان‌های سطحی و حجمی مغناطیس‌شدگی معادل

::: {.important}
$$\vect{J}_{ms}=\vect{M}\times\uvec{n},\qquad\vect{J}_m=\nabla\times\vect{M}$$
:::

- چگالی بارهای سطحی و حجمی قطبی‌شدگی معادل

$$\rho_{ps}=\vect{P}\cdot\uvec{n},\qquad\rho_p=-\nabla\cdot\vect{P}$$

- مسئله یافتن چگالی شار مغناطیسی $\vect{B}$ ناشی از یک چگالی حجمی مشخص از گشتاور دو قطبی مغناطیسی $\vect{M}$، به پیدا کردن چگالی‌های جریان مغناطیس‌شدگی معادل و سپس تعیین $\vect{A}$ و به دنبال آن محاسبه $\vect{B}$ تبدیل می‌شود.

::: {.example number="5-8"}
چگالی شار مغناطیسی را روی محور یک استوانه مغناطیسی بدست آورید. این استوانه دارای شعاع $b$، طول $L$ و بردار مغناطیس شدگی $\vect{M}=\uvec{z}M_0$ است.

```{.figure #m05-ex8 caption=""}
```

::: {.solution}
$$\vect{J}_m=\nabla\times\vect{M}=0$$

- چگالی جریان سطحی معادل روی دیواره جانبی

$$\vect{J}_{ms}=\vect{M}\times\uvec{n}=\uvec{z}M_0\times\uvec{r}=\uvec{\phi}M_0$$

- چگالی جریان سطحی معادل روی سطوح بالایی و پایینی صفر است.

$$\left.\begin{aligned}&\vect{B}=\frac{\mu_0}{4\pi}\int_{S'}\frac{\vect{J}_{ms}\times(\vect{R}-\vect{R}')\,ds'}{\lvert\vect{R}-\vect{R}'\rvert^3}\\&ds'=b\,d\phi'\,dz'\\&\vect{R}=z\uvec{z}\\&\vect{R}'=b\uvec{r'}+z'\uvec{z}\\&\vect{R}-\vect{R}'=(z-z')\uvec{z}-b\uvec{r'}\\&\begin{aligned}\vect{J}_{ms}\times(\vect{R}-\vect{R}')&=M_0\uvec{\phi'}\times\left((z-z')\uvec{z}-b\uvec{r'}\right)\\&=M_0(z-z')\uvec{r'}+bM_0\uvec{z}\end{aligned}\end{aligned}\right\}$$

- به صورت شهودی واضح است که مؤلفه $r$ چگالی شار مغناطیسی صفر است.

$$\begin{aligned}\vect{B}=\int d\vect{B}&=\uvec{z}\int_0^L\frac{\mu_0M_0b^2\,dz'}{2\left[(z-z')^2+b^2\right]^{3/2}}\\&=\uvec{z}\frac{\mu_0M_0}{2}\left[\frac{z}{\sqrt{z^2+b^2}}-\frac{z-L}{\sqrt{(z-L)^2+b^2}}\right]\end{aligned}$$
:::
:::

## شدت میدان مغناطیسی و نفوذپذیری نسبی

```{.figure #m05-map-hmu caption=""}
```

### شدت میدان مغناطیسی

- چون اعمال یک میدان مغناطیسی خارجی باعث هم‌امتداد شدن گشتاورهای دوقطبی داخلی و القای گشتاور مغناطیسی در ماده مغناطیسی می‌شود، انتظار داریم که چگالی شار مغناطیسی حاصل شده در حضور ماده مغناطیسی با مقدار آن در فضای آزاد متفاوت باشد.
- با درنظر گرفتن چگالی جریان حجمی معادل در ماده داریم

$$\frac{1}{\mu_0}\nabla\times\vect{B}=\vect{J}+\vect{J}_m=\vect{J}+\nabla\times\vect{M}\quad\Longrightarrow\quad\nabla\times\left(\frac{\vect{B}}{\mu_0}-\vect{M}\right)=\vect{J}$$

- شدت میدان مغناطیسی را به صورت زیر تعریف می‌کنیم

::: {.important}
$$\vect{H}=\frac{\vect{B}}{\mu_0}-\vect{M}\qquad(\mathrm{A/m})$$
:::

- استفاده از بردار $\vect{H}$ ما را قادر می‌سازد که معادله کرل ارتباط دهنده میدان مغناطیسی و توزیع جریان‌های آزاد را در هر محیطی بدون نیاز به بکار بردن $\vect{M}$ یا $\vect{J}_m$ بنویسیم

::: {.important}
$$\nabla\times\vect{H}=\vect{J}\qquad(\mathrm{A/m^2})$$
:::

- $\vect{J}$: چگالی جریان آزاد
- فرم انتگرالی

$$\int_S(\nabla\times\vect{H})\cdot d\vect{s}=\int_S\vect{J}\cdot d\vect{s}\quad\Longrightarrow\quad\boxed{\oint_C\vect{H}\cdot\dif\vect{\ell}=I\qquad(\mathrm{A})}$$

- رابطه اخیر شکل دیگر قانون مداری آمپر است.
- معادلات اصلی حاکم بر مغناطیس ساکن در هر محیطی

::: {.important}
$$\left\{\begin{aligned}&\nabla\cdot\vect{B}=0\\&\nabla\times\vect{H}=\vect{J}\end{aligned}\right.$$
:::

### ضریب نفوذپذیری نسبی

- رابطه بین بردار مغناطیس شدگی و شدت میدان مغناطیسی

$$\vect{M}=\chi_m\vect{H}$$

- $\chi_m$: ضریب حساسیت مغناطیسی
- رابطه بین شدت میدان مغناطیسی و چگالی شار مغناطیسی

::: {.important}
$$\begin{aligned}\vect{B}&=\mu_0(1+\chi_m)\vect{H}\\&=\mu_0\mu_r\vect{H}=\mu\vect{H}\qquad(\mathrm{Wb/m^2})\end{aligned}$$
:::

$$\mu_r=1+\chi_m=\frac{\mu}{\mu_0}$$

- $\mu_r$: کمیت بدون بعد به نام نفوذپذیری نسبی محیط
- روابط میدان الکتریکی و مغناطیسی ساکن دوگان یکدیگرند

| Electrostatics | Magnetostatics |
|:---:|:---:|
| $\vect{E}$ | $\vect{B}$ |
| $\vect{D}$ | $\vect{H}$ |
| $\epsilon$ | $\dfrac1\mu$ |
| $\vect{P}$ | $-\vect{M}$ |
| $\rho$ | $\vect{J}$ |
| $V$ | $\vect{A}$ |
| $\cdot$ | $\times$ |
| $\times$ | $\cdot$ |

### رفتار مواد مغناطیسی

- مواد مغناطیسی را به طور تقریبی می‌توان بر اساس مقدار ضریب نفوذپذیری نسبی آن‌ها به سه گروه اصلی طبقه بندی کرد
    - **مواد دیامغناطیس**: $\mu_r<1$ ($\chi_m$ عدد منفی بسیار کوچکی است)
        - در این مواد گشتاور مغناطیسی خالص در غیاب میدان مغناطیسی اعمال شده خارجی صفر است. $\ELto$ مس، سرب، جیوه، نقره و طلا $\ELto$ $\chi_m\approx-10^{-5}$
    - **مواد پارامغناطیس**: $\mu_r>1$ ($\chi_m$ عدد مثبت بسیار کوچکی است)
        - در این مواد گشتاور مغناطیسی متوسط خالصی در غیاب میدان مغناطیسی اعمالی خارجی وجود دارد. $\ELto$ آلومینیوم، منیزیوم و تنگستن $\ELto$ $\chi_m\approx10^{-5}$
    - **مواد فرومغناطیس**: $\mu_r\gg1$ ($\chi_m$ عدد مثبت بزرگی است)
        - در این مواد گشتاور مغناطیسی از نظر اندازه چندین برابر مقدار نظیر در مواد پارامغناطیس است. $\ELto$ کوبالت، نیکل و آهن
        - رابطه بین $\vect{B}$ و $\vect{H}$ در یک ماده فرومغناطیس غیرخطی است.

```{.figure #m05-hysteresis caption="پدیده هیسترزیس یا پس‌ماند"}
```

## مدارهای مغناطیسی

```{.figure #m05-map-circ caption=""}
```

- مشابه بحث مدارهای الکتریکی، گاهی اوقات لازم است که در یک مدار مغناطیسی، شار مغناطیسی و شدت میدان مغناطیسی ناشی از سیم‌پیچ‌های حامل جریان محاسبه شود.
- برای تحلیل مدارهای مغناطیسی داریم

$$\nabla\cdot\vect{B}=0,\qquad\nabla\times\vect{H}=\vect{J}$$
$$\oint_C\vect{H}\cdot\dif\vect{\ell}=NI=\mathcal{V}_m$$

- $\mathcal{V}_m$: نیروی محرکه مغناطیسی با واحد $\mathrm{A}$. این کمیت مشابه نیروی محرکه الکتریکی در مدارات الکتریکی است.

::: {.example number="5-9"}
فرض کنید که $N$ دور سیم برروی یک هسته چنبره‌ای از ماده مغناطیسی با نفوذپذیری $\mu$ پیچیده شده باشد. هسته دارای شعاع متوسط $r_0$، سطح مقطع دایروی با شعاع $a$ و یک فاصله هوایی کوچک به طول $\ell_g$ است. جریان دائمی $I_0$ در سیم جاری است. مطلوبست

- الف. چگالی شار مغناطیسی در هسته مغناطیسی
- ب. شدت میدان مغناطیسی در هسته مغناطیسی
- ج. شدت میدان مغناطیسی در فاصله هوایی

```{.figure #m05-ex9 caption=""}
```

::: {.solution}
- **فرض اول**: از شار نشتی صرف نظر می‌کنیم

```{.figure #m05-ex9-gauss caption=""}
```

$$\nabla\cdot\vect{B}=0\quad\Longrightarrow\quad\oint_S\vect{B}\cdot d\vect{s}=0$$

- شار در هسته و فاصله هوایی یکسان است.
- **فرض دوم**: از اثرات حاشیه‌ای شار در فاصله هوایی صرف نظر می‌کنیم.
    - چگالی شار در هسته و فاصله هوایی یکسان است.

$$\vect{B}_f=\vect{B}_g=\uvec{\phi}B_f$$
$$\vect{H}_f=\uvec{\phi}\frac{B_f}{\mu},\qquad\vect{H}_g=\uvec{\phi}\frac{B_f}{\mu_0}$$
$$\oint_C\vect{H}\cdot\dif\vect{\ell}=NI_0\quad\Longrightarrow\quad\frac{B_f}{\mu}(2\pi r_0-\ell_g)+\frac{B_f}{\mu_0}\ell_g=NI_0$$

- الف.

$$\vect{B}_f=\uvec{\phi}\frac{\mu_0\mu NI_0}{\mu_0(2\pi r_0-\ell_g)+\mu\ell_g}$$

- ب.

$$\vect{H}_f=\uvec{\phi}\frac{\mu_0NI_0}{\mu_0(2\pi r_0-\ell_g)+\mu\ell_g}$$

- ج.

$$\vect{H}_g=\uvec{\phi}\frac{\mu NI_0}{\mu_0(2\pi r_0-\ell_g)+\mu\ell_g}$$
:::
:::

- اگر شعاع سطح مقطع هسته بسیار کوچکتر از شعاع متوسط چنبره باشد، چگالی شار مغناطیسی در هسته تقریباً ثابت بوده و داریم

$$\Phi\cong BS\quad\Longrightarrow\quad\Phi=\frac{NI_0}{(2\pi r_0-\ell_g)/\mu S+\ell_g/\mu_0S}\quad\Longrightarrow\quad\Phi=\frac{\mathcal{V}_m}{\mathcal{R}_f+\mathcal{R}_g}$$

::: {.important}
$$\mathcal{R}_f=\frac{2\pi r_0-\ell_g}{\mu S}=\frac{\ell_f}{\mu S},\qquad\mathcal{R}_g=\frac{\ell_g}{\mu_0S}$$
:::

- $\mathcal{R}_f$ و $\mathcal{R}_g$: رلوکتانس با واحد $1/\mathrm{H}$

- تشابه این مدار مغناطیسی با یک مدار الکتریکی به صورت زیر است

```{.figure #m05-circuits caption=""}
```

$$\Phi=\frac{\mathcal{V}_m}{\mathcal{R}_f+\mathcal{R}_g},\qquad I=\frac{\mathcal{V}}{R_f+R_g}$$

| Magnetic Circuits | Electric Circuits |
|---|---|
| mmf, $\mathcal{V}_m\,(=NI)$ | emf, $\mathcal{V}$ |
| magnetic flux, $\Phi$ | electric current, $I$ |
| reluctance, $\mathcal{R}$ | resistance, $R$ |
| permeability, $\mu$ | conductivity, $\sigma$ |

- مشابه قانون ولتاژ کرشهف در مدارات الکتریکی، در مدارات مغناطیسی داریم

::: {.important}
$$\sum_jN_jI_j=\sum_k\mathcal{R}_k\Phi_k$$
:::

- در نتیجه جمع جبری آمپردورها در پیرامون هر مسیر بسته یک مدار مغناطیسی، برابر با جمع جبری حاصلضرب رلوکتانس‌ها و شارهاست.
- مشابه قانون جریان کرشهف در مدارات الکتریکی، در مدارات مغناطیسی داریم

::: {.important}
$$\sum_j\Phi_j=0$$
:::

- که بیان می‌کند جمع جبری شارهای مغناطیسی خارج‌شونده از یک گره در هر مدار مغناطیسی صفر است.
- با وجود این تشابه ساده، تحلیل دقیق مدارهای مغناطیسی به دلایل زیر بسیار دشوار است
    - وجود شارهای نشتی
    - وجود اثرات لبه‌ای که باعث می‌شود خطوط شار مغناطیسی در شکاف هوایی پخش و برآمده شود.
    - وابسته بودن نفوذپذیری مواد فرومغناطیسی به شدت میدان مغناطیسی و به عبارتی غیرخطی بودن رابطه $\vect{B}$ و $\vect{H}$

::: {.example number="5-10"}
مدار مغناطیسی شکل زیر را در نظر بگیرید. جریان‌های دائمی $I_1$ و $I_2$ به ترتیب در سیم پیچ‌هایی با $N_1$ و $N_2$ دور جاری هستند. هسته دارای سطح مقطعی به مساحت $S_c$ و نفوذپذیری $\mu$ است. شار مغناطیسی را در بازوی وسط تعیین کنید.

```{.figure #m05-ex10 caption=""}
```

::: {.solution}
- مدار معادل

```{.figure #m05-ex10-circuit caption=""}
```

$$\mathcal{R}_1=\frac{\ell_1}{\mu S_c},\qquad\mathcal{R}_2=\frac{\ell_2}{\mu S_c},\qquad\mathcal{R}_3=\frac{\ell_3}{\mu S_c}$$
$$\begin{aligned}&\mathit{Loop}~1:&N_1I_1&=(\mathcal{R}_1+\mathcal{R}_3)\Phi_1+\mathcal{R}_1\Phi_2\\&\mathit{Loop}~2:&N_1I_1-N_2I_2&=\mathcal{R}_1\Phi_1+(\mathcal{R}_1+\mathcal{R}_2)\Phi_2\end{aligned}$$
$$\Phi_1=\frac{\mathcal{R}_2N_1I_1+\mathcal{R}_1N_2I_2}{\mathcal{R}_1\mathcal{R}_2+\mathcal{R}_1\mathcal{R}_3+\mathcal{R}_2\mathcal{R}_3}$$
:::
:::

## شرایط مرزی میدان‌های مغناطیسی ساکن

```{.figure #m05-map-bc caption=""}
```

- شرط مرزی مؤلفه‌های عمودی

$$\nabla\cdot\vect{B}=0\quad\Longrightarrow\quad\boxed{B_{1n}=B_{2n}\qquad(\mathrm{T})}$$

- در محیط‌های خطی

::: {.important}
$$\mu_1H_{1n}=\mu_2H_{2n}$$
:::

- شرط مرزی مؤلفه‌های مماسی

```{.figure #m05-bc caption=""}
```

$$\oint_C\vect{H}\cdot\dif\vect{\ell}=I$$
$$\oint_{abcda}\vect{H}\cdot\dif\vect{\ell}=\vect{H}_1\cdot\Delta\vect{w}+\vect{H}_2\cdot(-\Delta\vect{w})=J_{sn}\Delta w$$
$$H_{1t}-H_{2t}=J_{sn}\qquad(\mathrm{A/m})$$

::: {.important}
$$\uvec{n2}\times(\vect{H}_1-\vect{H}_2)=\vect{J}_s\qquad(\mathrm{A/m})$$
:::
