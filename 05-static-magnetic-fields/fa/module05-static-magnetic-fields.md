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

## اندوکتانس و سلف‌ها

```{.figure #m05-map-induct caption=""}
```

- سلف چه المانی است و مفهوم اندوکتانس چیست؟
- نحوه محاسبه اندوکتانس ساختارهای مختلف به چه صورتی است؟

```{.figure #m05-two-loops caption=""}
```

- دو حلقه بسته را در نظر می‌گیریم. اگر جریان $I_1$ در $C_1$ برقرار شود، میدان مغناطیسی $\vect{B}_1$ تولید خواهد شد. قدری از شار مغناطیسی ناشی از $\vect{B}_1$ با $C_2$ پیوند خواهد داشت. این شار متقابل عبارتست از

$$\Phi_{12}=\int_{S_2}\vect{B}_1\cdot d\vect{s}_2\qquad(\mathrm{Wb})$$

- در حالتی که $C_2$ دارای $N_2$ دور باشد، پیوند شار برابر است با

$$\Lambda_{12}=N_2\Phi_{12}\qquad(\mathrm{Wb})$$

- از قانون بیوساوار می‌دانیم که $\vect{B}_1$ و درنتیجه $\Phi_{12}$ متناسب با $I_1$ است. بنابراین

$$\Lambda_{12}=L_{12}I_1\qquad(\mathrm{Wb})\quad\Longrightarrow\quad\boxed{L_{12}=\frac{\Lambda_{12}}{I_1}\qquad(\mathrm{H})}$$

- ثابت تناسب $L_{12}$ **اندوکتانس متقابل** بین حلقه‌های $C_1$ و $C_2$ نامیده می‌شود و واحد آن هانری $(\mathrm{H})$ است. اندوکتانس متقابل بین دو مدار، پیوند شار مغناطیسی یک مدار در واحد جریان مدار دیگر است.
- کل پیوند شار با $C_1$ ناشی از $I_1$ برابر است با

$$\Lambda_{11}=N_1\Phi_{11}\quad\Longrightarrow\quad\boxed{L_{11}=\frac{\Lambda_{11}}{I_1}}$$

- **اندوکتانس خودی** یک حلقه، پیوند شار مغناطیسی حلقه در واحد جریان خود حلقه است.
- اندوکتانس خودی یک مدار و اندوکتانس متقابل بین دو مدار، به شکل هندسی و نفوذپذیری محیط بستگی دارند. در یک محیط خطی، اندوکتانس خودی و متقابل به جریان مدار وابسته نیستند.
- یک هادی که به صورت مناسبی برای فراهم آوردن مقدار معینی اندوکتانس خودی شکل داده شده باشد را سلف می‌نامیم.
- مانند یک خازن که می‌تواند انرژی الکتریکی را ذخیره کند، سلف می‌تواند انرژی مغناطیسی را در خود حفظ کند.
- مراحل تعیین **اندوکتانس خودی** یک سلف به ترتیب زیر است
    - تعیین دستگاه مختصات مناسب
    - فرض جریان $I$ در سیم
    - محاسبه $\vect{B}$ از روی $I$
    - یافتن پیوند شار با هریک از دورها

$$\Phi=\int_S\vect{B}\cdot d\vect{s}$$

- $S$: سطحی که روی آن $\vect{B}$ وجود داشته و با جریان مفروض پیوند دارد
    - محاسبه پیوند شار
    - محاسبه $L$

$$L=\Lambda/I$$

- مراحل تعیین **اندوکتانس متقابل** بین دو مدار به ترتیب زیر است
    - تعیین دستگاه مختصات مناسب
    - فرض جریان $I_1$ در سیم
    - محاسبه $\vect{B}_1$ از روی $I_1$
    - یافتن شار متقابل

$$\Phi_{12}=\int_{S_2}\vect{B}_1\cdot d\vect{s}_2$$

- محاسبه پیوند شار

$$\Lambda_{12}=N_2\Phi_{12}$$

- محاسبه $L_{12}$

$$L_{12}=\frac{\Lambda_{12}}{I_1}\qquad(\mathrm{H})$$

- می‌توان نشان داد

::: {.important}
$$L_{12}=L_{21}$$
:::

::: {.example number="5-11"}
فرض کنید $N$ دور سیم به طور فشرده روی یک قاب چنبره‌ای با سطح مقطع مستطیلی مطابق شکل زیر پیچیده شده باشد. با فرض اینکه نفوذپذیری محیط $\mu_0$ است، اندوکتانس خودی سیم پیچ چنبره‌ای را پیدا کنید.

```{.figure #m05-ex11 caption=""}
```

::: {.solution}
- انتخاب دستگاه مختصات استوانه‌ای
- فرض جریان $I$ در سیم پیچ
- محاسبه $\vect{B}$ با استفاده از قانون مداری آمپر

$$\vect{B}=\uvec{\phi}B_\phi,\qquad\dif\vect{\ell}=\uvec{\phi}r\,d\phi$$
$$\oint_C\vect{B}\cdot\dif\vect{\ell}=\int_0^{2\pi}B_\phi r\,d\phi=2\pi rB_\phi$$
$$2\pi rB_\phi=\mu_0NI\quad\Longrightarrow\quad B_\phi=\frac{\mu_0NI}{2\pi r}$$

- محاسبه $\Phi$ و $\Lambda$

$$\begin{aligned}\Phi=\int_S\vect{B}\cdot d\vect{s}&=\int_S\left(\uvec{\phi}\frac{\mu_0NI}{2\pi r}\right)\cdot(\uvec{\phi}h\,dr)\\&=\frac{\mu_0NIh}{2\pi}\int_a^b\frac{dr}{r}=\frac{\mu_0NIh}{2\pi}\ln\frac ba\end{aligned}\quad\Longrightarrow\quad\Lambda=\frac{\mu_0N^2Ih}{2\pi}\ln\frac ba$$

- محاسبه $L$

$$L=\frac\Lambda I=\frac{\mu_0N^2h}{2\pi}\ln\frac ba$$
:::
:::

::: {.example number="5-12"}
اندوکتانس در واحد طول یک سیم لوله بسیار بلند با هسته هوایی و دارای $n$ دور در واحد طول را پیدا کنید.

::: {.solution}
$$B=\mu_0nI$$
$$\Phi=BS=\mu_0nSI$$
$$\Lambda'=n\Phi=\mu_0n^2SI$$
$$L'=\mu_0n^2S\qquad(\mathrm{H/m})$$
:::
:::

::: {.example number="5-13"}
اندوکتانس متقابل بین یک حلقه هادی مثلثی و یک سیم مستقیم بسیار بلند را بدست آورید.

```{.figure #m05-ex13 caption=""}
```

::: {.solution}
- فرض جریان $I_2$ در سیم بلند و یافتن $\vect{B}$ ناشی از آن

$$\vect{B}_2=\uvec{\phi}\frac{\mu_0I_2}{2\pi r}$$

- یافتن پیوند شار

$$\begin{aligned}\Lambda_{21}&=\int_{S_1}\vect{B}_2\cdot d\vect{s}_1\\&=\int_d^{d+b}\int_0^{[(d+b)-r]\tan60^\circ}\frac{\mu_0I_2}{2\pi r}\,dz\,dr\end{aligned}$$
$$\begin{aligned}\Lambda_{21}&=-\frac{\sqrt3\mu_0I_2}{2\pi}\int_d^{d+b}\frac1r\left[r-(d+b)\right]dr\\&=\frac{\sqrt3\mu_0I_2}{2\pi}\left[(d+b)\ln\left(1+\frac bd\right)-b\right]\end{aligned}$$

::: {.important}
$$L_{21}=\frac{\Lambda_{21}}{I_2}=\frac{\sqrt3\mu_0}{2\pi}\left[(d+b)\ln\left(1+\frac bd\right)-b\right]\qquad(\mathrm{H})$$
:::
:::
:::

## انرژی و نیروهای مغناطیس ساکن

```{.figure #m05-map-energy caption=""}
```

### انرژی مغناطیسی

- برای در جای خود قرار دادن دسته‌ای از بارها، به انجام کار نیاز بوده و این کار به صورت **انرژی الکتریکی** ذخیره می‌شود.
- به طور مشابه انتظار داریم که به هنگام ایجاد جریان در حلقه‌های هادی نیز لازم باشد کاری انجام و این کار به صورت **انرژی مغناطیسی** ذخیره شود.
- حلقه بسته‌ای را با اندوکتانس خودی $L_1$ و جریان اولیه $i_1=0$ در نظر بگیرید.
    - یک مولد به این حلقه وصل می‌شود و جریان $i_1$ را از صفر به $I_1$ افزایش می‌دهد.
    - در این فرآیند یک شار مغناطیسی متغیر از حلقه عبور خواهد کرد. بنابراین مطابق با قانون القای فارادی یک نیروی محرکه الکتریکی در حلقه القا می‌شود

$$v_1=\frac{d\Phi_1}{dt}=L_1\frac{di_1}{dt}$$

- مطابق با قانون لنز این نیروی محرکه الکتریکی با تغییرات شار و جریان مخالفت می‌کند. بنابراین برای غلبه بر آن باید کار انجام شود. این کار به صورت انرژی مغناطیسی ذخیره می‌شود

$$W_1=\int v_1i_1\,dt=L_1\int_0^{I_1}i_1\,di_1=\frac12L_1I_1^2$$

- اکنون دو حلقه بسته را در نظر بگیرید که حامل جریان‌های $i_1$ و $i_2$ هستند. مقدار اولیه جریان‌ها صفر بوده و به ترتیب تا $I_1$ و $I_2$ افزایش می‌یابند.
    - برای یافتن مقدار کار لازم (یا انرژی مغناطیسی ذخیره شده) ابتدا فرض می‌شود که $i_2=0$ و $i_1$ را از صفر به $I_1$ افزایش می‌دهیم. این افزایش به کار $W_1$ نیاز دارد.
    - حال $i_1$ را در مقدار $I_1$ ثابت نگه داشته و $i_2$ را از صفر تا $I_2$ افزایش می‌دهیم. دو کار باید انجام شود.
        - کار $W_{22}$ برای افزایش $i_2$ از صفر به $I_2$

$$W_{22}=\frac12L_2I_2^2$$

- به دلیل تزویج متقابل بخشی از شار مغناطیسی ناشی از $i_2$ با حلقه اول پیوند می‌خورد. بنابراین مطابق با قانون القای فارادی یک نیروی محرکه الکتریکی در حلقه اول القا می‌شود.

$$v_{21}=\frac{d\Phi_{21}}{dt}=L_{21}\frac{di_2}{dt}$$

- مطابق با قانون لنز این نیروی محرکه با تغییر در جریان حلقه اول، با تغییرات شار پیوندی با حلقه اول مخالفت می‌کند. بنابراین برای غلبه بر آن باید کار انجام داد

$$W_{21}=\int v_{21}I_1\,dt=L_{21}I_1\int_0^{I_2}di_2=L_{21}I_1I_2$$

- کل کار انجام شده یا کل انرژی مغناطیسی ذخیره شده برابر است با

$$\begin{aligned}W_2&=\frac12L_1I_1^2+L_{21}I_1I_2+\frac12L_2I_2^2\\&=\frac12\sum_{j=1}^2\sum_{k=1}^2L_{jk}I_jI_k\end{aligned}$$

- در حالت کلی برای $N$ حلقه جریان داریم

$$W_m=\frac12\sum_{j=1}^N\sum_{k=1}^NL_{jk}I_jI_k\qquad(\mathrm{J})$$

- شار پیوندی با $k$امین حلقه

$$\Phi_k=\sum_{j=1}^NL_{jk}I_j$$

::: {.important}
$$W_m=\frac12\sum_{k=1}^NI_k\Phi_k\qquad(\mathrm{J})$$
:::

- می‌توان نشان داد که انرژی مغناطیسی ذخیره شده برای توزیع پیوسته جریان در یک حجم به صورت زیر است.

::: {.important}
$$W_m=\frac12\int_{V'}\vect{A}\cdot\vect{J}\,dv'\qquad(\mathrm{J})$$
:::

- $V'$: محیط دارای $\vect{J}$ که می‌تواند به کل فضا گسترش یابد
- می‌توان نشان داد که انرژی مغناطیسی ذخیره شده برحسب کمیت‌های میدان به صورت زیر است

::: {.important}
$$W_m=\frac12\int_{V'}\vect{H}\cdot\vect{B}\,dv'\qquad(\mathrm{J})$$
$$W_m=\frac12\int_{V'}\frac{B^2}{\mu}\,dv'\qquad(\mathrm{J})$$
$$W_m=\frac12\int_{V'}\mu H^2\,dv'\qquad(\mathrm{J})$$
:::

- $V'$: کل فضا

::: {.remark}
اغلب تعیین اندوکتانس خودی از روی انرژی مغناطیسی ذخیره شده بر حسب $\vect{H}$ یا $\vect{B}$ آسانتر از استفاده از پیوند شار است

$$W_m=\frac12\sum_{j=1}^N\sum_{k=1}^NL_{jk}I_jI_k$$

- برای یک سلف حامل جریان $I$ و اندوکتانس $L$

$$W_m=\frac12LI^2$$
$$L=\frac{2W_m}{I^2}\qquad(\mathrm{H})$$
:::

::: {.example number="5-14"}
با استفاده از انرژی مغناطیسی ذخیره شده، اندوکتانس یک خط انتقال هم محور هوائی که دارای هادی داخلی توپر به شعاع $a$ و هادی خارجی بسیار نازک به شعاع داخلی $b$ است را در واحد طول تعیین کنید.

::: {.solution}
- انرژی ذخیره شده در واحد طول هادی داخلی

$$B_{\phi1}=\frac{\mu_0Ir}{2\pi a^2}\quad\Longrightarrow\quad\begin{aligned}W'_{m1}&=\frac{1}{2\mu_0}\int_0^a\!\!\int_0^{2\pi}B_{\phi1}^2\,r\,dr\,d\phi\\&=\frac{\mu_0I^2}{4\pi a^4}\int_0^ar^3\,dr=\frac{\mu_0I^2}{16\pi}\qquad(\mathrm{J/m})\end{aligned}$$

- انرژی ذخیره شده در واحد طول در ناحیه بین دو هادی

$$B_{\phi2}=\frac{\mu_0I}{2\pi r}\quad\Longrightarrow\quad\begin{aligned}W'_{m2}&=\frac{1}{2\mu_0}\int_a^b\!\!\int_0^{2\pi}B_{\phi2}^2\,r\,dr\,d\phi\\&=\frac{\mu_0I^2}{4\pi}\int_a^b\frac1r\,dr=\frac{\mu_0I^2}{4\pi}\ln\frac ba\qquad(\mathrm{J/m})\end{aligned}$$

- بنابراین

$$\begin{aligned}L'&=\frac{2}{I^2}\left(W'_{m1}+W'_{m2}\right)\\&=\frac{\mu_0}{8\pi}+\frac{\mu_0}{2\pi}\ln\frac ba\qquad(\mathrm{H/m})\end{aligned}$$
:::
:::

::: {.example number="5-15"}
برای یک سیملوله بسیار بلند با سطح مقطع $S$ و $n$ دور در واحد طول و هسته هوایی، اندوکتانس در واحد طول را بدست آورید.

::: {.solution}
$$B=\mu_0nI\quad\Longrightarrow\quad W_m=\frac12\int_{V'}\frac{B^2}{\mu}\,dv'=\frac{1}{2\mu_0}\int\mu_0^2n^2I^2\,dv$$
$$=\frac12\mu_0n^2I^2S=\frac12LI^2\quad\Rightarrow\quad L'=\mu_0n^2S\qquad\mathrm{H/m}$$
:::
:::

### نیروها و گشتاورهای مغناطیسی

- وقتی بار $q$ با سرعت $\vect{u}$ در میدان مغناطیسی با چگالی شار $\vect{B}$ حرکت می‌کند، نیروی مغناطیسی $\vect{F}_m$ بر آن وارد می‌شود.

$$\vect{F}_m=q\vect{u}\times\vect{B}\qquad(\mathrm{N})$$

- مباحث مورد بررسی
    - اثر هال $(\text{Hall Effect})$
    - نیرو و گشتاور در هادی‌های حامل جریان

### اثر هال

- ماده‌ای هادی با سطح مقطع مستطیلی به ابعاد $d\times b$ در میدان مغناطیسی یکنواخت $\vect{B}=\uvec{z}B_0$ را در نظر بگیرید. جریان مستقیم یکنواختی در جهت $y$ عبور می‌کند.

```{.figure #m05-hall caption=""}
```

$$\vect{J}=\uvec{y}J_0=Nq\vect{u}$$

- حامل‌های بار الکترون‌ها هستند و $q$ منفی است

$$\vect{u}=-\uvec{y}u_0$$

- نیروی مغناطیسی مایل است الکترون‌ها را در جهت $+x$ حرکت دهد و یک میدان الکتریکی عرضی بوجود آورد. این فرآیند ادامه خواهد یافت تا میدان عرضی برای متوقف کردن رانش الکترون‌ها کافی باشد.
- در حالت دائمی نیروی خالص وارد بر حامل‌های بار صفر است.

$$\vect{E}_h+\vect{u}\times\vect{B}=0\quad\Longrightarrow\quad\vect{E}_h=-\vect{u}\times\vect{B}\quad\Longrightarrow\quad\begin{aligned}\vect{E}_h&=-(-\uvec{y}u_0)\times\uvec{z}B_0\\&=\uvec{x}u_0B_0\end{aligned}$$

- $\vect{E}_h$: میدان هال
- ولتاژ هال

$$V_h=-\int_0^dE_h\,dx=u_0B_0d$$

- ضریب هال

$$E_x/J_yB_z=1/Nq$$

- این پدیده را **اثر هال** گویند.
- از اثر هال برای اندازه گیری میدان مغناطیسی استفاده می‌شود.

### نیروها و گشتاورها در هادی‌های حامل جریان

- نیروی مغناطیسی وارد بر جز دیفرانسیلی یک مدار بسته به مسیر $C$، سطح مقطع $S$ و حامل جریان $I$ در میدان مغناطیسی به چگالی $\vect{B}$

```{.figure #m05-force-element caption=""}
```

$$d\vect{F}_m=q\vect{u}\times\vect{B}$$
$$\begin{aligned}d\vect{F}_m&=-NeS\lvert d\ell\rvert\vect{u}\times\vect{B}\\&=+NeS\lvert\vect{u}\rvert\,\dif\vect{\ell}\times\vect{B}\end{aligned}$$

- $N$: تعداد الکترون‌ها در واحد حجم و $e$: مقدار بار الکترون
- جهت $\dif\vect{\ell}$ خلاف جهت $\vect{u}$ است و $NeS\lvert\vect{u}\rvert=I$

::: {.important}
$$d\vect{F}_m=I\,\dif\vect{\ell}\times\vect{B}\qquad(\mathrm{N})$$
:::

- نیروی مغناطیسی وارد بر یک مدار بسته به مسیر $C$، سطح مقطع $S$ و حامل جریان $I$ در میدان مغناطیسی به چگالی $\vect{B}$

::: {.important}
$$\vect{F}_m=I\oint_C\dif\vect{\ell}\times\vect{B}\qquad(\mathrm{N})$$
:::

- $\dif\vect{\ell}$: در جهت جریان

::: {.example number="5-16"}
نیروی وارد بر واحد طول بین دو سیم هادی موازی بسیار بلند حامل جریان‌های هم جهت $I_1$ و $I_2$ مطابق شکل زیر را تعیین کنید.

```{.figure #m05-ex16 caption=""}
```

::: {.solution}
$$\vect{F}'_{12}=I_2\oint_{C_2}\dif\vect{\ell}_2\times\vect{B}_{12}=I_2\int_0^1dz\,\uvec{z}\times\left(-\uvec{x}\frac{\mu_0I_1}{2\pi d}\right)$$

::: {.important title="نیروی جاذبه"}
$$\vect{F}'_{12}=-\uvec{y}\frac{\mu_0I_1I_2}{2\pi d}\qquad(\mathrm{N/m})$$
:::
:::
:::

- حلقه مدوری به شعاع $b$ و حامل جریان $I$ در میدان مغناطیسی یکنواختی با چگالی شار $\vect{B}$ در نظر می‌گیریم

$$\vect{B}=\vect{B}_\perp+\vect{B}_\parallel$$

```{.figure #m05-loop-fields caption=""}
```

- $\vect{B}_\perp$ هیچ نیروی خالصی برای حرکت حلقه ایجاد نمی‌کند و صرفاً تمایل به گسترش حلقه (یا اگر جریان برعکس شود) تمایل به انقباض حلقه دارد.
- اگرچه نیروی خالص وارد بر حلقه ناشی از $\vect{B}_\parallel$ صفر است، گشتاوری وجود دارد که سعی می‌کند حلقه را حول محور $x$ چنان بچرخاند که میدان مغناطیسی ناشی از $I$ و میدان خارجی $\vect{B}_\parallel$ هم امتداد شوند.

$$\begin{aligned}d\vect{T}&=\uvec{x}(dF)2b\sin\phi\\&=\uvec{x}(I\,d\ell\,B_\parallel\sin\phi)2b\sin\phi\\&=\uvec{x}2Ib^2B_\parallel\sin^2\phi\,d\phi\end{aligned}$$
$$\begin{aligned}\vect{T}=\int d\vect{T}&=\uvec{x}2Ib^2B_\parallel\int_0^\pi\sin^2\phi\,d\phi\\&=\uvec{x}I(\pi b^2)B_\parallel\end{aligned}$$
$$\vect{m}=\uvec{n}I(\pi b^2)=\uvec{n}IS$$
$$\vect{T}=\vect{m}\times\vect{B}_\parallel=\vect{m}\times(\vect{B}_\parallel+\vect{B}_\perp)$$

::: {.important}
$$\vect{T}=\vect{m}\times\vect{B}\qquad(\mathrm{N\cdot m})$$
:::

- می‌توان نشان داد که رابطه فوق برای حلقه مسطح با هر شکل دلخواهی، مادامی که در یک میدان مغناطیسی یکنواخت قرار دارد، معتبر است

::: {.example number="5-17"}
یک حلقه مستطیل شکل در صفحه $xy$ با اضلاع $b_1$ و $b_2$ جریان $I$ را حمل می‌کند و در میدان مغناطیسی یکنواخت $\vect{B}=\uvec{x}B_x+\uvec{y}B_y+\uvec{z}B_z$ قرار دارد. نیرو و گشتاور وارد بر حلقه را تعیین کنید.

```{.figure #m05-ex17-perp caption=""}
```

::: {.solution}
$$\vect{B}_\perp=\uvec{z}B_z,\qquad\vect{B}_\parallel=\uvec{x}B_x+\uvec{y}B_y$$

- مولفه عمود بر صفحه، نیروی $Ib_1B_z$ را به اضلاع (۱) و (۳) و نیروی $Ib_2B_z$ را به اضلاع (۲) و (۴) به سمت مرکز وارد می‌کند. $\ELto$ گشتاوری تولید نمی‌شود.
- نیروهای وارد بر حلقه توسط مولفه موازی با صفحه

```{.figure #m05-ex17-par caption=""}
```

$$\begin{aligned}\vect{F}_1&=Ib_1\uvec{x}\times(\uvec{x}B_x+\uvec{y}B_y)\\&=\uvec{z}Ib_1B_y=-\vect{F}_3\end{aligned}$$
$$\begin{aligned}\vect{F}_2&=Ib_2(-\uvec{y})\times(\uvec{x}B_x+\uvec{y}B_y)\\&=\uvec{z}Ib_2B_x=-\vect{F}_4\end{aligned}$$
$$\left.\begin{aligned}&\vect{T}_{13}=\uvec{x}Ib_1b_2B_y\\&\vect{T}_{24}=-\uvec{y}Ib_1b_2B_x\end{aligned}\right\}\quad\begin{aligned}&\vect{T}=\vect{T}_{13}+\vect{T}_{24}=Ib_1b_2(\uvec{x}B_y-\uvec{y}B_x)\qquad(\mathrm{N\cdot m})\\&\vect{T}=\vect{m}\times(\uvec{x}B_x+\uvec{y}B_y)=\vect{m}\times\vect{B}\end{aligned}$$
:::
:::
