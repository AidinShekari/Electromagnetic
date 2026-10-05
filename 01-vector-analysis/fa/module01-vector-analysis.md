# آنالیز برداری

## سرفصل‌ها

```{.figure #m01-course-outline caption=""}
```

## آنالیز برداری

- **تحلیل یا آنالیز برداری**، یک ابزار ریاضی است که به کمک آن بیان و درک مفاهیم الکترومغناطیس ساده می‌شود.
- کمیت‌ها در الکترومغناطیس به دو دسته زیر تقسیم می‌شوند.
    - **عددی (scalar):** کمیتی است که به طور کامل با اندازه‌اش (مثبت یا منفی) مشخص می‌شود. مانند: بار، جریان الکتریکی، انرژی و…
    - **برداری (vector):** کمیتی که با اندازه و جهت توصیف می‌شود. مانند شدت میدان الکتریکی و مغناطیسی و…
- هر دوی کمیت‌های فوق می‌توانند تابعی از مکان و زمان باشند.

::: {.example number="1-1"}
- به نظر شما کمیت‌های زیر از چه نوعی هستند؟
    - دما
    - توان
    - نیرو
    - اختلاف پتانسیل
    - سرعت
- به غیر از موارد فوق، چه کمیت‌های اسکالر و برداری دیگری را در حوزه فیزیک می‌توانید نام ببرید؟
:::

```{.figure #m01-vector-analysis-map caption=""}
```

- چگونه می‌توان دو کمیت برداری را به صورت ترسیمی با هم جمع یا از هم کم کرد؟
- چگونه می‌توان بردارها را در هم ضرب کرد؟ مفهوم این ضرب چیست؟ کاربردهای آن کجاست؟

$$\vect{A}=2\uvec{x}+3\uvec{y}+\uvec{z}\qquad \vect{B}=\uvec{x}-2\uvec{y}+3\uvec{z}\qquad \vect{C}=-\uvec{x}+4\uvec{y}-\uvec{z}$$

- اندازه تصویر بردار $\vect{A}$ بر بردار $\vect{B}$ را بدست آورید.
- زاویه بین بردارهای $\vect{A}$ و $\vect{B}$ چقدر است؟
- مساحت مثلث تشکیل شده توسط دو بردار $\vect{A}$ و $\vect{B}$ چقدر می‌شود؟
- بردار واحد عمود بر صفحه شامل دو بردار $\vect{A}$ و $\vect{B}$ را بدست آورید.
- حجم متوازی‌السطوح حاصل از ۳ بردار $\vect{A}$، $\vect{B}$ و $\vect{C}$ چقدر است؟

## جبر برداری

- هر برداری دارای اندازه و جهت است.

$$\vect{A}=\uvec{A}A,\qquad \uvec{A}=\frac{\vect{A}}{\abs{\vect{A}}}=\frac{\vect{A}}{A}\quad(\text{بردار یکه})$$

```{.figure #m01-vector-magnitude caption=""}
```

::: {.remark}
برای هر کمیت برداری باید هم اندازه و هم جهت معلوم باشد. عدم مشخص کردن جهت یک کمیت برداری، به معنای نادیده گرفتن بخشی از اطلاعات آن کمیت است.
:::

## جمع بردارها

- جمع دو بردار به صورت ترسیمی
    - قاعده **متوازی‌الاضلاع**
    - قاعده **ابتدا به انتها**

```{.figure #m01-vector-sum caption=""}
```

- قوانین حاکم بر جمع بردارها
    - **قانون جابجایی**
$$\vect{A}+\vect{B}=\vect{B}+\vect{A}$$
    - **قانون انجمنی**
$$\vect{A}+(\vect{B}+\vect{C})=(\vect{A}+\vect{B})+\vect{C}$$

## تفریق بردارها

- تفریق برداری

$$\vect{A}-\vect{B}=\vect{A}+(-\vect{B})$$

```{.figure #m01-vector-difference caption=""}
```

## ضرب بردارها

```{.figure #m01-products-map caption=""}
```

- ضرب یک اسکالر در بردار:

$$k\vect{A}=\uvec{A}(kA)$$

## ضرب داخلی یا عددی

::: {.definition title="تعریف ریاضی"}
$$\vect{A}\cdot\vect{B}\triangleq AB\cos\theta_{AB}$$
- برابر است با حاصلضرب اندازه یک بردار در تصویر بردار دیگر بر بردار اول.
:::

```{.figure #m01-dot-product caption="$\\theta_{AB}$: زاویه کوچکتر بین دو بردار هنگامیکه ابتدای دو بردار به هم متصل می‌شود"}
```

- ویژگی‌های ضرب داخلی
    - نتیجه ضرب داخلی دو بردار، یک کمیت اسکالر است.
    - کمتر یا مساوی حاصلضرب اندازه‌های آن‌هاست.
    - بسته به زاویه بین آن‌ها می‌تواند کمیتی مثبت یا منفی باشد.
    - اگر بردارها عمود بر هم باشند، مساوی صفر است.
    - جابجاپذیر و توزیع‌پذیر است.
$$\vect{A}\cdot\vect{B}=\vect{B}\cdot\vect{A},\qquad \vect{A}\cdot(\vect{B}+\vect{C})=\vect{A}\cdot\vect{B}+\vect{A}\cdot\vect{C}$$
    - ضرب داخلی یک بردار در خودش
$$\vect{A}\cdot\vect{A}=A^2,\qquad A=+\sqrt{\vect{A}\cdot\vect{A}}$$

::: {.example number="1-2"}
با استفاده از مفهوم ضرب داخلی تصویر بردار $\vect{A}$ بر $\vect{B}$ را بدست آورید.

```{.figure #m01-ex2-statement caption=""}
```

::: {.solution}
```{.figure #m01-ex2-projection caption=""}
```

اندازه تصویر بردار $\vect{A}$ بر $\vect{B}$:
$$A\cos\theta_{AB}=\frac{\vect{A}\cdot\vect{B}}{B}$$
تصویر بردار $\vect{A}$ بر $\vect{B}$:
$$\frac{\vect{A}\cdot\vect{B}}{B}\uvec{B}=\left(\frac{\vect{A}\cdot\vect{B}}{B}\right)\frac{\vect{B}}{B}=\frac{\vect{A}\cdot\vect{B}}{B^2}\vect{B}$$
:::
:::

::: {.example number="1-3"}
قانون کسینوس‌ها در یک مثلث را با استفاده از مفهوم ضرب داخلی اثبات کنید.
$$C=\sqrt{A^2+B^2-2AB\cos\alpha}$$

```{.figure #m01-ex3-triangle caption=""}
```

::: {.solution}
```{.figure #m01-ex3-solution caption=""}
```

$$\vect{C}=\vect{A}+\vect{B}$$
$$\begin{aligned}C^2=\vect{C}\cdot\vect{C}&=(\vect{A}+\vect{B})\cdot(\vect{A}+\vect{B})\\&=\vect{A}\cdot\vect{A}+\vect{B}\cdot\vect{B}+2\vect{A}\cdot\vect{B}\\&=A^2+B^2+2AB\cos\theta_{AB}\end{aligned}$$
$$\cos\theta_{AB}=\cos(180^\circ-\alpha)=-\cos\alpha$$
$$C^2=A^2+B^2-2AB\cos\alpha$$
:::
:::

## ضرب خارجی یا برداری

::: {.definition}
$$\vect{A}\times\vect{B}\triangleq\uvec{n}\abs{AB\sin\theta_{AB}}$$
:::

- اندازه این حاصلضرب برابر با مساحت متوازی‌الاضلاع ساخته شده توسط بردارهای $\vect{A}$ و $\vect{B}$ و جهت آن عمود بر هر دو بردار است.

```{.figure #m01-cross-product caption=""}
```

- ویژگی‌های ضرب خارجی
    - نتیجه ضرب خارجی دو بردار یک کمیت برداری است.
    - جابجاپذیر نیست
$$\vect{B}\times\vect{A}=-\vect{A}\times\vect{B}$$
    - توزیع‌پذیر است
$$\vect{A}\times(\vect{B}+\vect{C})=\vect{A}\times\vect{B}+\vect{A}\times\vect{C}$$
    - انجمن‌پذیر نیست
$$\vect{A}\times(\vect{B}\times\vect{C})\neq(\vect{A}\times\vect{B})\times\vect{C}$$

::: {.example number="1-4"}
قانون سینوس‌ها در یک مثلث را با استفاده از مفهوم ضرب خارجی اثبات کنید.
$$\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}$$

```{.figure #m01-ex4-triangle caption=""}
```

::: {.solution}
مساحت مثلث:
$$\abs*{\tfrac12\vect{a}\times\vect{b}}=\abs*{\tfrac12\vect{b}\times\vect{c}}=\abs*{\tfrac12\vect{c}\times\vect{a}}$$
$$ab\sin C=bc\sin A=ca\sin B$$
$$\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}$$
:::
:::

## ضرب سه بردار

- **ضرب سه‌گانه عددی**

$$\vect{A}\cdot(\vect{B}\times\vect{C})=\vect{B}\cdot(\vect{C}\times\vect{A})=\vect{C}\cdot(\vect{A}\times\vect{B})$$

- دارای اندازه‌ای برابر با حجم متوازی‌السطوح تشکیل یافته از سه بردار $\vect{A}$، $\vect{B}$ و $\vect{C}$.
    - مساحت قاعده: $\abs{\vect{B}\times\vect{C}}=\abs{BC\sin\theta_1}$
    - اندازه ارتفاع: $\abs{A\cos\theta_2}$
    - حجم متوازی‌السطوح: $\abs{ABC\sin\theta_1\cos\theta_2}$

```{.figure #m01-triple-product caption=""}
```

- **ضرب سه‌گانه برداری**
    - معروف به قاعده back-cab

$$\vect{A}\times(\vect{B}\times\vect{C})=\vect{B}(\vect{A}\cdot\vect{C})-\vect{C}(\vect{A}\cdot\vect{B})$$

::: {.example number="1-5"}
عبارت $(\vect{A}\times\vect{B})\times\vect{C}$ با کدامیک از عبارت‌های زیر برابر است؟

- $\vect{B}(\vect{A}\cdot\vect{C})-\vect{C}(\vect{A}\cdot\vect{B})$
- $-\vect{B}(\vect{A}\cdot\vect{C})+\vect{C}(\vect{A}\cdot\vect{B})$
- $-\vect{A}(\vect{C}\cdot\vect{B})+\vect{B}(\vect{C}\cdot\vect{A})$
- $\vect{A}(\vect{C}\cdot\vect{B})-\vect{B}(\vect{C}\cdot\vect{A})$

::: {.solution}
$$\begin{aligned}(\vect{A}\times\vect{B})\times\vect{C}&=-\vect{C}\times(\vect{A}\times\vect{B})\\&=-\vect{A}(\vect{C}\cdot\vect{B})+\vect{B}(\vect{C}\cdot\vect{A})\end{aligned}$$
:::
:::

## دستگاه‌های مختصات متعامد

```{.figure #m01-vector-analysis-map-coord caption=""}
```

- صفحات اصلی در دستگاه‌های مختصات مختلف کدامند؟
- بردارهای یکه در دستگاه‌های مختصات مختلف چگونه تعریف می‌شوند؟
- نحوه محاسبه بردار مکان یک نقطه و بردار فاصله بین دو نقطه در دستگاه‌های مختصات مختلف چگونه است؟
- طول، سطح و حجم دیفرانسیلی را در دستگاه‌های مختصات مختلف، جهت استفاده در انتگرال‌گیری، تعیین کنید.
- نمایش بردار $\vect{A}=\uvec{r}(3\cos\phi)-\uvec{\phi}2r+\uvec{z}5$ در مختصات کارتزین را بدست آورید.
- موقعیت نقطه $P$ در مختصات کروی $(8,120^\circ,330^\circ)$ است. موقعیت این نقطه را در مختصات استوانه‌ای و کارتزین بیان کنید.

- برای توصیف تغییرات مکانی کمیت‌های فیزیکی باید بتوانیم تمام نقاط فضا را به صورت یکتا و مناسب توصیف کنیم.
    - این امر مستلزم بکارگیری یک دستگاه مختصات مناسب است.
- قوانین الکترومغناطیسی به دستگاه مختصات وابسته نیستند.
- جهت سادگی محاسبات از دستگاه مختصاتی که مناسب هندسه ساختار مسئله باشد، استفاده می‌شود.
- در فضای سه بعدی یک نقطه می‌تواند در محل تقاطع سه سطح قرار گیرد.
    - اگر این سه سطح دو به دو بر هم عمود باشند، یک دستگاه مختصات متعامد خواهیم داشت.
- سه دستگاه متعامد مورد استفاده در این درس
    - مختصات کارتزین یا دکارتی یا قائم
    - مختصات استوانه‌ای
    - مختصات کروی

## دستگاه مختصات کارتزین

```{.figure #m01-cartesian-planes caption=""}
```

- هر نقطه $P(x_1,y_1,z_1)$ محل تقاطع سه صفحه $x=x_1$، $y=y_1$ و $z=z_1$ است.
- بردار یکه $\uvec{x}$ $\ELto$ بردار واحد عمود بر صفحه $x$-ثابت و در جهت مثبت
- بردار یکه $\uvec{y}$ $\ELto$ بردار واحد عمود بر صفحه $y$-ثابت و در جهت مثبت
- بردار یکه $\uvec{z}$ $\ELto$ بردار واحد عمود بر صفحه $z$-ثابت و در جهت مثبت

- ضرب خارجی و داخلی بردارهای یکه

$$\uvec{x}\times\uvec{y}=\uvec{z},\qquad \uvec{y}\times\uvec{z}=\uvec{x},\qquad \uvec{z}\times\uvec{x}=\uvec{y}$$

```{.figure #m01-cartesian-cycle caption=""}
```

$$\uvec{x}\cdot\uvec{y}=\uvec{y}\cdot\uvec{z}=\uvec{z}\cdot\uvec{x}=0$$
$$\uvec{x}\cdot\uvec{x}=\uvec{y}\cdot\uvec{y}=\uvec{z}\cdot\uvec{z}=1$$

- نمایش بردار دلخواه $\vect{A}$ در مختصات کارتزین

::: {.important}
$$\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z$$
$$A=\sqrt{A_x^2+A_y^2+A_z^2}$$
:::

- **بردار مکان**
    - بردار مکان نقطه $P$، فاصله جهت‌دار از مبدأ به $P$ است.

$$\vect{R}_1=x_1\uvec{x}+y_1\uvec{y}+z_1\uvec{z},\qquad \vect{R}_2=x_2\uvec{x}+y_2\uvec{y}+z_2\uvec{z}$$

- **بردار فاصله**
    - بردار جابجایی از یک نقطه به نقطه دیگر است.

$$\vect{R}_{12}=\vect{R}_2-\vect{R}_1=(x_2-x_1)\uvec{x}+(y_2-y_1)\uvec{y}+(z_2-z_1)\uvec{z}$$

```{.figure #m01-position-vectors caption=""}
```

$$\vect{A}=A_x\uvec{x}+A_y\uvec{y}+A_z\uvec{z},\qquad \vect{B}=B_x\uvec{x}+B_y\uvec{y}+B_z\uvec{z}$$

- ضرب داخلی دو بردار $\vect{A}$ و $\vect{B}$

::: {.important}
$$\vect{A}\cdot\vect{B}=A_xB_x+A_yB_y+A_zB_z$$
:::

- ضرب خارجی دو بردار $\vect{A}$ و $\vect{B}$

$$\begin{aligned}\vect{A}\times\vect{B}={}&A_xB_x\uvec{x}\times\uvec{x}+A_xB_y\uvec{x}\times\uvec{y}+A_xB_z\uvec{x}\times\uvec{z}\\&+A_yB_x\uvec{y}\times\uvec{x}+A_yB_y\uvec{y}\times\uvec{y}+A_yB_z\uvec{y}\times\uvec{z}\\&+A_zB_x\uvec{z}\times\uvec{x}+A_zB_y\uvec{z}\times\uvec{y}+A_zB_z\uvec{z}\times\uvec{z}\\={}&(A_yB_z-A_zB_y)\uvec{x}+(A_zB_x-A_xB_z)\uvec{y}+(A_xB_y-A_yB_x)\uvec{z}\end{aligned}$$

::: {.important}
$$\vect{A}\times\vect{B}=\begin{vmatrix}\uvec{x}&\uvec{y}&\uvec{z}\\A_x&A_y&A_z\\B_x&B_y&B_z\end{vmatrix}$$
:::

- طول دیفرانسیلی $\ELto$ **بردار**

$$\dif\vect{\ell}=\uvec{x}\,dx+\uvec{y}\,dy+\uvec{z}\,dz$$

- سطح دیفرانسیلی $\ELto$ **بردار**

$$d\vect{S}=dS\,\uvec{n}$$
$$d\vect{S}=dy\,dz\,\uvec{x},\qquad d\vect{S}=dx\,dz\,\uvec{y},\qquad d\vect{S}=dx\,dy\,\uvec{z}$$

- حجم دیفرانسیلی $\ELto$ **اسکالر**

$$dv=dx\,dy\,dz$$

```{.figure #m01-cartesian-differentials caption=""}
```

::: {.example number="1-6"}
الف) برداری که نقطه ابتدای آن $P_1(1,3,2)$ و نقطه انتهای آن $P_2(3,-2,4)$ است را بدست آورید.

ب) طول این بردار چقدر است؟

::: {.solution}
```{.figure #m01-ex6 caption=""}
```

الف)
$$\begin{aligned}\overrightarrow{P_1P_2}&=\overrightarrow{OP_2}-\overrightarrow{OP_1}\\&=(\uvec{x}3-\uvec{y}2+\uvec{z}4)-(\uvec{x}+\uvec{y}3+\uvec{z}2)\\&=\uvec{x}2-\uvec{y}5+\uvec{z}2\end{aligned}$$
ب)
$$P_1P_2=\abs{\overrightarrow{P_1P_2}}=\sqrt{2^2+(-5)^2+2^2}=\sqrt{33}$$
:::
:::

::: {.example number="1-7"}
با فرض اینکه $\vect{A}=\uvec{x}5-\uvec{y}2+\uvec{z}$، آنگاه بردار یکه $\vect{B}$ را به گونه‌ای بدست آورید که

- الف. $\vect{B}\parallel\vect{A}$
- ب. $\vect{B}$ در صفحه $xy$ بوده و عمود بر $\vect{A}$ باشد

::: {.solution}
الف.
$$\vect{B}=\frac{\vect{A}}{A}=\frac{\uvec{x}5-\uvec{y}2+\uvec{z}}{\sqrt{5^2+2^2+1^2}}=\frac{\uvec{x}5-\uvec{y}2+\uvec{z}}{\sqrt{30}}$$
ب.
$$\begin{cases}B=\sqrt{B_x^2+B_y^2+B_z^2}=1\\B_z=0\\\vect{B}\cdot\vect{A}=5B_x-2B_y=0\end{cases}\quad\Rightarrow\quad\begin{cases}B_x=\dfrac{2}{\sqrt{29}}\\[2mm]B_y=\dfrac{5}{\sqrt{29}}\end{cases}$$
:::
:::

## دستگاه مختصات استوانه‌ای

```{.figure #m01-cylindrical-surfaces caption=""}
```

- هر نقطه $P(r_1,\phi_1,z_1)$ محل تقاطع استوانه $r=r_1$، نیم‌صفحه $\phi=\phi_1$ و صفحه $z=z_1$ است.
- بردار یکه $\uvec{r}$ $\ELto$ بردار واحد عمود بر استوانه $r$-ثابت و در جهت مثبت
- بردار یکه $\uvec{\phi}$ $\ELto$ بردار واحد عمود بر نیم‌صفحه $\phi$-ثابت و در جهت مثبت
- بردار یکه $\uvec{z}$ $\ELto$ بردار واحد عمود بر صفحه $z$-ثابت و در جهت مثبت

::: {.remark}
جهت بردارهای $\uvec{r}$ و $\uvec{\phi}$ در نقاط مختلف فضا تغییر می‌کند. این نکته در هنگام انتگرال‌گیری باید مورد دقت قرار گیرد.
:::

- ضرب خارجی و داخلی بردارهای یکه

$$\uvec{r}\times\uvec{\phi}=\uvec{z},\qquad \uvec{\phi}\times\uvec{z}=\uvec{r},\qquad \uvec{z}\times\uvec{r}=\uvec{\phi}$$

```{.figure #m01-cylindrical-cycle caption=""}
```

$$\uvec{r}\cdot\uvec{r}=\uvec{\phi}\cdot\uvec{\phi}=\uvec{z}\cdot\uvec{z}=1$$
$$\uvec{r}\cdot\uvec{\phi}=\uvec{\phi}\cdot\uvec{z}=\uvec{z}\cdot\uvec{r}=0$$

- نمایش بردار دلخواه $\vect{A}$ در مختصات استوانه‌ای

::: {.important}
$$\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z$$
$$A=\sqrt{A_r^2+A_\phi^2+A_z^2}$$
:::

- بردار مکان

```{.figure #m01-cylindrical-position caption=""}
```

$$\vect{R}=r\uvec{r}+z\uvec{z}$$

::: {.example number="1-8"}
مختصات استوانه‌ای نقطه دلخواه $P$ به صورت $(r,\phi,0)$ است. بردار واحد از نقطه $z=h$ روی محور $z$ به سمت نقطه $P$ را بیابید.

::: {.solution}
```{.figure #m01-ex8 caption=""}
```

$$\overrightarrow{QP}=\overrightarrow{OP}-\overrightarrow{OQ}=(\uvec{r}r)-(\uvec{z}h)$$
$$\uvec{QP}=\frac{\overrightarrow{QP}}{\abs{\overrightarrow{QP}}}=\frac{1}{\sqrt{r^2+h^2}}(\uvec{r}r-\uvec{z}h)$$
:::
:::

- طول دیفرانسیلی $\ELto$ **بردار**

$$\dif\vect{\ell}=\uvec{r}\,dr+\uvec{\phi}\,r\,d\phi+\uvec{z}\,dz$$

- سطح دیفرانسیلی $\ELto$ **بردار**

$$d\vect{S}=r\,d\phi\,dz\,\uvec{r},\qquad d\vect{S}=dr\,dz\,\uvec{\phi},\qquad d\vect{S}=r\,dr\,d\phi\,\uvec{z}$$

- حجم دیفرانسیلی $\ELto$ **اسکالر**

$$dv=r\,dr\,d\phi\,dz$$

```{.figure #m01-cylindrical-differentials caption=""}
```

- تبدیل نمایش بردار از مختصات استوانه‌ای به کارتزین

$$\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z$$

```{.figure #m01-cyl-cart-units caption=""}
```

$$\uvec{r}=\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y},\qquad \uvec{\phi}=-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y},\qquad \uvec{z}=\uvec{z}$$

$$\begin{aligned}\vect{A}&=(\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y})A_r\\&\quad+(-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y})A_\phi\\&\quad+\uvec{z}A_z\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{x}(\cos\phi\,A_r-\sin\phi\,A_\phi)\\&\quad+\uvec{y}(\sin\phi\,A_r+\cos\phi\,A_\phi)\\&\quad+\uvec{z}A_z\end{aligned}$$

- تبدیل نمایش بردار از مختصات کارتزین به استوانه‌ای

$$\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z$$

$$\uvec{x}=\cos\phi\,\uvec{r}-\sin\phi\,\uvec{\phi},\qquad \uvec{y}=\sin\phi\,\uvec{r}+\cos\phi\,\uvec{\phi},\qquad \uvec{z}=\uvec{z}$$

$$\begin{aligned}\vect{A}&=(\cos\phi\,\uvec{r}-\sin\phi\,\uvec{\phi})A_x\\&\quad+(\sin\phi\,\uvec{r}+\cos\phi\,\uvec{\phi})A_y\\&\quad+\uvec{z}A_z\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{r}(\cos\phi\,A_x+\sin\phi\,A_y)\\&\quad+\uvec{\phi}(-\sin\phi\,A_x+\cos\phi\,A_y)\\&\quad+\uvec{z}A_z\end{aligned}$$

- تبدیل نمایش بردار از مختصات استوانه‌ای به کارتزین

::: {.important}
$$\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}=\begin{bmatrix}\cos\phi&-\sin\phi&0\\\sin\phi&\cos\phi&0\\0&0&1\end{bmatrix}\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}$$
:::

- تبدیل نمایش بردار از مختصات کارتزین به استوانه‌ای

::: {.important}
$$\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}=\begin{bmatrix}\cos\phi&\sin\phi&0\\-\sin\phi&\cos\phi&0\\0&0&1\end{bmatrix}\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}$$
:::

- تبدیل از مختصات استوانه‌ای به کارتزین

$$x=r\cos\phi,\qquad y=r\sin\phi,\qquad z=z$$

- تبدیل از مختصات کارتزین به استوانه‌ای

$$r=\sqrt{x^2+y^2},\qquad \phi=\tan^{-1}\frac{y}{x},\qquad z=z$$

```{.figure #m01-cyl-cart-coords caption=""}
```

## دستگاه مختصات کروی

```{.figure #m01-spherical-surfaces caption=""}
```

- هر نقطه $P(R_1,\theta_1,\phi_1)$ محل تقاطع کره $R=R_1$، مخروط $\theta=\theta_1$ و نیم‌صفحه $\phi=\phi_1$
- بردار یکه $\uvec{R}$ $\ELto$ بردار واحد عمود بر کره $R$-ثابت و در جهت مثبت
- بردار یکه $\uvec{\theta}$ $\ELto$ بردار واحد عمود بر مخروط $\theta$-ثابت و در جهت مثبت
- بردار یکه $\uvec{\phi}$ $\ELto$ بردار واحد عمود بر نیم‌صفحه $\phi$-ثابت و در جهت مثبت

::: {.remark}
جهت بردارهای $\uvec{R}$، $\uvec{\theta}$ و $\uvec{\phi}$ در نقاط مختلف فضا تغییر می‌کند. این نکته در هنگام انتگرال‌گیری باید مورد دقت قرار گیرد.
:::

- ضرب خارجی و داخلی بردارهای یکه

$$\uvec{R}\times\uvec{\theta}=\uvec{\phi},\qquad \uvec{\theta}\times\uvec{\phi}=\uvec{R},\qquad \uvec{\phi}\times\uvec{R}=\uvec{\theta}$$

```{.figure #m01-spherical-cycle caption=""}
```

$$\uvec{R}\cdot\uvec{R}=\uvec{\theta}\cdot\uvec{\theta}=\uvec{\phi}\cdot\uvec{\phi}=1$$
$$\uvec{R}\cdot\uvec{\theta}=\uvec{\theta}\cdot\uvec{\phi}=\uvec{\phi}\cdot\uvec{R}=0$$

- نمایش بردار دلخواه $\vect{A}$ در مختصات کروی

::: {.important}
$$\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi$$
$$A=\sqrt{A_R^2+A_\theta^2+A_\phi^2}$$
:::

- بردار مکان

```{.figure #m01-spherical-position caption=""}
```

$$\vect{R}=R_1\uvec{R}$$

- طول دیفرانسیلی $\ELto$ **بردار**

$$\dif\vect{\ell}=\uvec{R}\,dR+\uvec{\theta}\,R\,d\theta+\uvec{\phi}\,R\sin\theta\,d\phi$$

- سطح دیفرانسیلی $\ELto$ **بردار**

$$d\vect{S}=R^2\sin\theta\,d\theta\,d\phi\,\uvec{R},\qquad d\vect{S}=R\sin\theta\,dR\,d\phi\,\uvec{\theta},\qquad d\vect{S}=R\,dR\,d\theta\,\uvec{\phi}$$

- حجم دیفرانسیلی $\ELto$ **اسکالر**

$$dv=R^2\sin\theta\,dR\,d\theta\,d\phi$$

```{.figure #m01-spherical-differentials caption=""}
```

- تبدیل نمایش بردار از مختصات کروی به استوانه‌ای

$$\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi\quad\Longrightarrow\quad\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z$$

```{.figure #m01-sph-cyl-units caption=""}
```

$$\uvec{R}=\sin\theta\,\uvec{r}+\cos\theta\,\uvec{z},\qquad \uvec{\theta}=\cos\theta\,\uvec{r}-\sin\theta\,\uvec{z},\qquad \uvec{\phi}=\uvec{\phi}$$

$$\begin{aligned}\vect{A}&=(\sin\theta\,\uvec{r}+\cos\theta\,\uvec{z})A_R\\&\quad+(\cos\theta\,\uvec{r}-\sin\theta\,\uvec{z})A_\theta\\&\quad+\uvec{\phi}A_\phi\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{r}(\sin\theta\,A_R+\cos\theta\,A_\theta)\\&\quad+\uvec{\phi}A_\phi\\&\quad+\uvec{z}(\cos\theta\,A_R-\sin\theta\,A_\theta)\end{aligned}$$

- تبدیل نمایش بردار از مختصات استوانه‌ای به کروی

$$\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi$$

$$\uvec{r}=\sin\theta\,\uvec{R}+\cos\theta\,\uvec{\theta},\qquad \uvec{\phi}=\uvec{\phi},\qquad \uvec{z}=\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta}$$

$$\begin{aligned}\vect{A}&=(\sin\theta\,\uvec{R}+\cos\theta\,\uvec{\theta})A_r\\&\quad+\uvec{\phi}A_\phi\\&\quad+(\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta})A_z\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{R}(\sin\theta\,A_r+\cos\theta\,A_z)\\&\quad+\uvec{\theta}(\cos\theta\,A_r-\sin\theta\,A_z)\\&\quad+\uvec{\phi}A_\phi\end{aligned}$$

- تبدیل نمایش بردار از مختصات کروی به استوانه‌ای

::: {.important}
$$\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}=\begin{bmatrix}\sin\theta&\cos\theta&0\\0&0&1\\\cos\theta&-\sin\theta&0\end{bmatrix}\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}$$
:::

- تبدیل نمایش بردار از مختصات استوانه‌ای به کروی

::: {.important}
$$\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}=\begin{bmatrix}\sin\theta&0&\cos\theta\\\cos\theta&0&-\sin\theta\\0&1&0\end{bmatrix}\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}$$
:::

- تبدیل نمایش بردار از مختصات کارتزین به کروی

$$\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi$$

$$\left\{\begin{aligned}\uvec{x}&=\cos\phi\,\uvec{r}-\sin\phi\,\uvec{\phi}\\\uvec{y}&=\sin\phi\,\uvec{r}+\cos\phi\,\uvec{\phi}\\\uvec{z}&=\uvec{z}\end{aligned}\right.\qquad\left\{\begin{aligned}\uvec{r}&=\sin\theta\,\uvec{R}+\cos\theta\,\uvec{\theta}\\\uvec{\phi}&=\uvec{\phi}\\\uvec{z}&=\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta}\end{aligned}\right.$$

$$\Longrightarrow\quad\left\{\begin{aligned}\uvec{x}&=\sin\theta\cos\phi\,\uvec{R}+\cos\theta\cos\phi\,\uvec{\theta}-\sin\phi\,\uvec{\phi}\\\uvec{y}&=\sin\theta\sin\phi\,\uvec{R}+\cos\theta\sin\phi\,\uvec{\theta}+\cos\phi\,\uvec{\phi}\\\uvec{z}&=\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta}\end{aligned}\right.$$

::: {.important}
$$\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}=\begin{bmatrix}\sin\theta\cos\phi&\sin\theta\sin\phi&\cos\theta\\\cos\theta\cos\phi&\cos\theta\sin\phi&-\sin\theta\\-\sin\phi&\cos\phi&0\end{bmatrix}\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}$$
:::

- تبدیل نمایش بردار از مختصات کروی به کارتزین

$$\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi\quad\Longrightarrow\quad\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z$$

$$\left\{\begin{aligned}\uvec{R}&=\sin\theta\,\uvec{r}+\cos\theta\,\uvec{z}\\\uvec{\theta}&=\cos\theta\,\uvec{r}-\sin\theta\,\uvec{z}\\\uvec{\phi}&=\uvec{\phi}\end{aligned}\right.\qquad\left\{\begin{aligned}\uvec{r}&=\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y}\\\uvec{\phi}&=-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y}\\\uvec{z}&=\uvec{z}\end{aligned}\right.$$

$$\Longrightarrow\quad\left\{\begin{aligned}\uvec{R}&=\sin\theta\cos\phi\,\uvec{x}+\sin\theta\sin\phi\,\uvec{y}+\cos\theta\,\uvec{z}\\\uvec{\theta}&=\cos\theta\cos\phi\,\uvec{x}+\cos\theta\sin\phi\,\uvec{y}-\sin\theta\,\uvec{z}\\\uvec{\phi}&=-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y}\end{aligned}\right.$$

::: {.important}
$$\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}=\begin{bmatrix}\sin\theta\cos\phi&\cos\theta\cos\phi&-\sin\phi\\\sin\theta\sin\phi&\cos\theta\sin\phi&\cos\phi\\\cos\theta&-\sin\theta&0\end{bmatrix}\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}$$
:::

- تبدیل از مختصات استوانه‌ای به کروی

$$R=\sqrt{r^2+z^2},\qquad \theta=\tan^{-1}\frac{r}{z},\qquad \phi=\phi$$

- تبدیل از مختصات کروی به استوانه‌ای

$$r=R\sin\theta,\qquad \phi=\phi,\qquad z=R\cos\theta$$

- تبدیل از مختصات کروی به کارتزین

$$x=R\sin\theta\cos\phi,\qquad y=R\sin\theta\sin\phi,\qquad z=R\cos\theta$$

- تبدیل از مختصات کارتزین به کروی

$$R=\sqrt{x^2+y^2+z^2},\qquad \theta=\tan^{-1}\frac{\sqrt{x^2+y^2}}{z},\qquad \phi=\tan^{-1}\frac{y}{x}$$

```{.figure #m01-sph-coords caption=""}
```

## انتگرال‌های شامل توابع برداری

```{.figure #m01-vector-analysis-map-calc caption=""}
```

- انواع انتگرال‌های شامل توابع برداری که با آن‌ها سروکار داریم

$$\int_C\vect{F}\,d\ell\qquad \iint_S\vect{F}\,ds\qquad \iiint_V\vect{F}\,dv$$
$$\int_C V\,\dif\vect{\ell}$$
$$\int_C\vect{F}\cdot\dif\vect{\ell}\qquad \iint_S\vect{A}\cdot d\vect{s}$$
$$\int_C\vect{F}\times\dif\vect{\ell}$$

::: {.remark}
نکات مهم در مورد انتگرال‌گیری شامل توابع برداری

- استفاده از دستگاه مختصات مناسب
- تعیین صحیح طول، سطح و حجم دیفرانسیلی
- دقت به تغییرات بردارهای یکه $\uvec{r}$، $\uvec{R}$، $\uvec{\theta}$ و $\uvec{\phi}$ در بازه انتگرال‌گیری
:::

- انتگرال از یک تابع برداری روی منحنی، سطح و حجم مشخص

$$\int_C\vect{F}\,d\ell\qquad \iint_S\vect{F}\,ds\qquad \iiint_V\vect{F}\,dv$$

- حاصل یک بردار است.
- کاربردهای مهم در الکترومغناطیس: محاسبه شدت میدان الکتریکی ناشی از یک توزیع بار خطی، سطحی و حجمی

$$\left\{\begin{aligned}\vect{E}&=\frac{1}{4\pi\varepsilon_0}\int_C\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}\\\vect{E}&=\frac{1}{4\pi\varepsilon_0}\iint_S\frac{\rho_s\,ds'(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}\\\vect{E}&=\frac{1}{4\pi\varepsilon_0}\iiint_V\frac{\rho_v\,dv'(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}\end{aligned}\right.$$

::: {.example number="1-9"}
انتگرال زیر را روی منحنی $C$ محاسبه کنید.
$$\int_C\vect{F}\,d\ell,\qquad \vect{F}=3\uvec{r}$$

```{.figure #m01-ex9 caption=""}
```

::: {.solution}
```{.figure #m01-ex9-solution caption=""}
```

$$d\ell=r\,d\phi=a\,d\phi$$
$$\int_C\vect{F}\,d\ell=\int_0^\pi 3\uvec{r}\,a\,d\phi=3a\int_0^\pi(\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y})\,d\phi=6a\uvec{y}$$
:::
:::

- انتگرال از یک تابع اسکالر روی مسیر مشخص

$$\int_C V\,\dif\vect{\ell}$$

- حاصل یک بردار است.
- کاربردهای مهم در الکترومغناطیس: محاسبه پتانسیل مغناطیسی ناشی از یک جریان خطی

$$\vect{A}=\frac{\mu_0I}{4\pi}\oint_C\frac{\dif\vect{\ell}'}{\abs{\vect{R}-\vect{R}'}}$$

::: {.example number="1-10"}
انتگرال زیر را در امتداد مسیرهای زیر محاسبه کنید

$$\int_O^P r^2\,\dif\vect{\ell},\qquad r^2=x^2+y^2$$

- مسیر $OP$
- مسیر $OP_1P$
- مسیر $OP_2P$

```{.figure #m01-ex10 caption=""}
```

::: {.solution}
- در امتداد مسیر $OP$

$$\begin{aligned}\int_O^P r^2\,\dif\vect{\ell}&=\uvec{r}\int_0^{\sqrt2}r^2\,dr=\uvec{r}\,\frac{2\sqrt2}{3}\\&=\frac{2\sqrt2}{3}(\uvec{x}\cos45^\circ+\uvec{y}\sin45^\circ)\\&=\uvec{x}\frac23+\uvec{y}\frac23\end{aligned}$$

- در امتداد مسیر $OP_1P$

$$\begin{aligned}\int_O^P(x^2+y^2)\,\dif\vect{\ell}&=\uvec{y}\int_O^{P_1}y^2\,dy+\uvec{x}\int_{P_1}^P(x^2+1)\,dx\\&=\uvec{y}\tfrac13y^3\Big|_0^1+\uvec{x}\left(\tfrac13x^3+x\right)\Big|_0^1\\&=\uvec{x}\frac43+\uvec{y}\frac13\end{aligned}$$

- در امتداد مسیر $OP_2P$

$$\begin{aligned}\int_O^P(x^2+y^2)\,\dif\vect{\ell}&=\uvec{x}\int_O^{P_2}x^2\,dx+\uvec{y}\int_{P_2}^P(1+y^2)\,dy\\&=\uvec{x}\tfrac13x^3\Big|_0^1+\uvec{y}\left(y+\tfrac13y^3\right)\Big|_0^1\\&=\uvec{x}\frac13+\uvec{y}\frac43\end{aligned}$$
:::
:::

- انتگرال خطی عددی

$$\int_C\vect{F}\cdot\dif\vect{\ell}$$

- حاصل یک اسکالر است.
- اگر $\vect{F}$ نیرو باشد
    - کار انجام شده بوسیله نیرو برای حرکت دادن جسمی از نقطه $P_1$ به نقطه $P_2$ در امتداد مسیر مشخص شده $C$
- کاربردهای مهم در الکترومغناطیس
    - محاسبه اختلاف پتانسیل الکتریکی بین نقاط $P_1$ و $P_2$:
$$V=-\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$
    - قانون مداری آمپر:
$$\mu_0I=-\oint_C\vect{B}\cdot\dif\vect{\ell}$$

::: {.example number="1-11"}
انتگرال زیر را در مسیر ربع دایره شکل روبرو محاسبه کنید.

$$\int_A^B\vect{F}\cdot\dif\vect{\ell},\qquad \vect{F}=\uvec{x}xy-\uvec{y}2x$$

```{.figure #m01-ex11 caption=""}
```

::: {.solution}
$$\begin{bmatrix}F_r\\F_\phi\\F_z\end{bmatrix}=\begin{bmatrix}\cos\phi&\sin\phi&0\\-\sin\phi&\cos\phi&0\\0&0&1\end{bmatrix}\begin{bmatrix}xy\\-2x\\0\end{bmatrix}$$
$$\vect{F}=\uvec{r}(xy\cos\phi-2x\sin\phi)-\uvec{\phi}(xy\sin\phi+2x\cos\phi)$$
$$\dif\vect{\ell}=\uvec{\phi}\,3\,d\phi\qquad \vect{F}\cdot\dif\vect{\ell}=-3(xy\sin\phi+2x\cos\phi)\,d\phi$$
$$x=3\cos\phi\qquad y=3\sin\phi$$
$$\int_A^B\vect{F}\cdot\dif\vect{\ell}=\int_0^{\pi/2}-3(9\sin^2\phi\cos\phi+6\cos^2\phi)\,d\phi=-9\left(1+\frac{\pi}{2}\right)$$
:::
:::

- انتگرال سطحی عددی

$$\iint_S\vect{A}\cdot d\vect{s}$$

- حاصل یک اسکالر است.
- حاصل انتگرال $\ELto$ شار میدان برداری $\vect{A}$ که از سطح $S$ می‌گذرد
- سطح دیفرانسیلی برداری

$$d\vect{s}=\uvec{n}\,ds$$

```{.figure #m01-surface-normals caption="جهت $\\mathbf{a}_n$ برای سطح بسته: عمود بر سطح به سمت خارج حجم؛ برای سطح باز: وابسته به حرکت روی حاشیه سطح باز و با استفاده از قانون دست راست"}
```

- کاربردهای مهم در الکترومغناطیس
    - قانون گوس در فضای آزاد:
$$\oiint_S\vect{E}\cdot d\vect{s}=\frac{Q}{\varepsilon_0}$$
    - محاسبه جریان الکتریکی:
$$\iint_S\vect{J}\cdot d\vect{s}=I$$

::: {.example number="1-12"}
انتگرال زیر را روی سطح بسته‌ای حول محور $z$ که با $z=\pm3$ و $r=2$ مشخص می‌شود، محاسبه کنید

$$\oint_S\vect{F}\cdot d\vect{s},\qquad \vect{F}=\uvec{r}\frac{k_1}{r}+\uvec{z}k_2z$$

```{.figure #m01-ex12 caption=""}
```

::: {.solution}
$$\oint_S\vect{F}\cdot d\vect{s}=\oint_S\vect{F}\cdot\uvec{n}\,ds=\int_{\substack{\text{top}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds+\int_{\substack{\text{bottom}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds+\int_{\substack{\text{side}\\\text{wall}}}\vect{F}\cdot\uvec{n}\,ds$$

- سطح بالایی

$$z=3,\quad \uvec{n}=\uvec{z},\quad \vect{F}\cdot\uvec{n}=k_2z=3k_2,\quad ds=r\,dr\,d\phi$$
$$\int_{\substack{\text{top}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds=\int_0^{2\pi}\!\!\int_0^2 3k_2\,r\,dr\,d\phi=12\pi k_2$$

- سطح پایینی

$$z=-3,\quad \uvec{n}=-\uvec{z},\quad \vect{F}\cdot\uvec{n}=-k_2z=3k_2,\quad ds=r\,dr\,d\phi$$
$$\int_{\substack{\text{bottom}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds=12\pi k_2$$

- دیواره جانبی

$$r=2,\quad \uvec{n}=\uvec{r},\quad \vect{F}\cdot\uvec{n}=\frac{k_1}{r}=\frac{k_1}{2},\quad ds=r\,d\phi\,dz=2\,d\phi\,dz$$
$$\int_{\substack{\text{side}\\\text{wall}}}\vect{F}\cdot\uvec{n}\,ds=\int_{-3}^3\!\int_0^{2\pi}k_1\,d\phi\,dz=12\pi k_1$$

$$\oint_S\vect{F}\cdot d\vect{s}=12\pi k_2+12\pi k_2+12\pi k_1=12\pi(k_1+2k_2)$$
:::
:::

- انتگرال خطی برداری

$$\int_C\vect{F}\times\dif\vect{\ell}$$

- حاصل یک بردار است.
- کاربردهای مهم در الکترومغناطیس
    - قانون بیوساوار:
$$\vect{B}=\frac{\mu_0I}{4\pi}\oint_C\frac{\dif\vect{\ell}\times(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}$$
    - محاسبه نیروی مغناطیسی وارد بر سیم حامل جریان در میدان مغناطیسی:
$$\vect{F}=I\oint_C\dif\vect{\ell}\times\vect{B}$$

::: {.example number="1-13"}
انتگرال زیر را در مسیر $C$ محاسبه کنید.

$$\int_C\vect{F}\times\dif\vect{\ell},\qquad \vect{F}=2\uvec{z}$$

```{.figure #m01-ex13 caption=""}
```

::: {.solution}
$$\dif\vect{\ell}=r\,d\phi\,\uvec{\phi}=a\,d\phi\,\uvec{\phi}$$
$$\begin{aligned}\int_C\vect{F}\times\dif\vect{\ell}&=\int_{2\pi}^0 2\uvec{z}\times a\,d\phi\,\uvec{\phi}=-2a\int_{2\pi}^0\uvec{r}\,d\phi\\&=-2a\int_{2\pi}^0(\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y})\,d\phi=0\end{aligned}$$
:::
:::

## عملیات مشتق‌گیری - گرادیان

- **مفاهیم پیش‌نیاز برای ورود به بحث گرادیان**
    - مفهوم مشتق از یک تابع تک‌متغیره
        - نرخ تغییرات تابع در نقطه مورد نظر
    - مفهوم مشتق جهت‌دار از یک تابع چندمتغیره
        - نرخ تغییرات تابع در نقطه مورد نظر و در یک جهت مشخص شده

```{.figure #m01-derivative-concepts caption=""}
```

::: {.definition title="گرادیان"}
گرادیانِ یک **کمیت اسکالر**، یک **کمیت برداری** است که در جهتی قرار می‌گیرد که کمیت اسکالر بیشترین افزایش را دارد و اندازه آن برابر با حداکثر نرخ افزایش کمیت اسکالر است.

$$\operatorname{grad}v=\nabla v=\uvec{n}\frac{dv}{dn}$$
:::

- مشتق جهت‌دار $v$ در جهت $\dif\vect{\ell}$:

$$\frac{dv}{d\ell}=\nabla v\cdot\uvec{\ell}$$

- گرادیان $v$ بر سطوح $v$ ثابت عمود است.

```{.figure #m01-gradient-map caption=""}
```

- رابطه گرادیان در مختصات کارتزین به صورت زیر است

::: {.important}
$$\nabla v=\frac{\partial v}{\partial x}\uvec{x}+\frac{\partial v}{\partial y}\uvec{y}+\frac{\partial v}{\partial z}\uvec{z}$$
:::

- رابطه کلی گرادیان

::: {.important}
$$\nabla V=\uvec{u_1}\frac{\partial V}{h_1\,\partial u_1}+\uvec{u_2}\frac{\partial V}{h_2\,\partial u_2}+\uvec{u_3}\frac{\partial V}{h_3\,\partial u_3}$$
:::

| ضرایب متری | کارتزین | استوانه‌ای | کروی |
|---|---|---|---|
| $h_1$ | $1$ | $1$ | $1$ |
| $h_2$ | $1$ | $r$ | $R$ |
| $h_3$ | $1$ | $1$ | $R\sin\theta$ |

- **مفهوم گرادیان**
    - نمایش یک تپه با کانتورهای ارتفاع $\ELto$ $h(x,y)$
    - اگر توپی در نقطه $P$ قرار داشته باشد، در چه جهتی حرکت می‌کند و مقدار نیروی وارد بر آن چقدر است؟
        - پاسخ متناسب با $-\nabla h$ است.

```{.figure #m01-gradient-hill caption=""}
```

::: {.example number="1-14"}
شدت میدان الکتریکی $\vect{E}$ به صورت منهای گرادیان پتانسیل الکتریکی عددی $V$ قابل دستیابی است. $\vect{E}$ را در نقطه $(1,1,0)$ بیابید اگر
$$V=E_0R\cos\theta$$

::: {.solution}
$$\vect{E}=-\nabla V$$
$$\begin{aligned}\vect{E}&=-\left[\uvec{R}\frac{\partial}{\partial R}+\uvec{\theta}\frac{\partial}{R\,\partial\theta}+\uvec{\phi}\frac{\partial}{R\sin\theta\,\partial\phi}\right]E_0R\cos\theta\\&=-(\uvec{R}\cos\theta-\uvec{\theta}\sin\theta)E_0\end{aligned}$$
$$\vect{E}=-\uvec{z}E_0$$
:::
:::

## عملیات مشتق‌گیری - دیورژانس

- **مفاهیم پیش‌نیاز برای ورود به بحث دیورژانس**
    - در مطالعه میدان‌های برداری، راحت‌تر است که تغییرات میدان را به صورت ترسیمی توسط خطوط شار نمایش دهیم. این‌ها خطوط یا منحنی‌های جهت‌داری هستند که در هر نقطه جهت میدان برداری را مشخص می‌کنند.

```{.figure #m01-flux-lines caption=""}
```

- شار یک میدان برداری مشابه جریان یک سیال مانند آب است.
- اگر $\vect{A}$ یک بردار چگالی شار باشد، کل شار خروجی از سطح $S$ برابر است با

$$\oint_S\vect{A}\cdot d\vect{s}$$

- در حجمی با یک سطح بسته، تنها وقتی شار اضافی ورودی یا خروجی وجود خواهد داشت که این حجم به ترتیب دارای یک چاه یا یک منبع باشد.
    - شار خالص خروجی از $v_a$ مثبت است: وجود منبع در حجم $v_a$
    - شار خالص خروجی از $v_b$ منفی است: وجود چاه در حجم $v_b$
    - شار خالص خروجی از $v_c$ صفر است.

```{.figure #m01-source-sink caption=""}
```

::: {.definition title="دیورژانس"}
دیورژانس **میدان برداری** $\vect{A}$ در یک نقطه عبارتست از شار خالص خروجی $\vect{A}$ در واحد حجم وقتی که این حجم حول نقطه به سمت صفر میل می‌کند

$$\operatorname{div}\vect{A}\triangleq\lim_{\Delta v\to0}\frac{\oint_S\vect{A}\cdot d\vect{s}}{\Delta v}$$
:::

- در مختصات کارتزین رابطه دیورژانس به صورت زیر است

::: {.important}
$$\operatorname{div}\vect{A}=\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}\qquad\qquad \nabla\cdot\vect{A}\equiv\operatorname{div}\vect{A}$$
:::

- رابطه کلی دیورژانس

::: {.important}
$$\nabla\cdot\vect{A}=\frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial u_1}(h_2h_3A_1)+\frac{\partial}{\partial u_2}(h_1h_3A_2)+\frac{\partial}{\partial u_3}(h_1h_2A_3)\right]$$
:::

::: {.example number="1-15"}
چگالی شار مغناطیسی $\vect{B}$ در بیرون یک سیم طویل حامل جریان به صورت دایره‌ای و متناسب با معکوس فاصله از محور سیم است. دیورژانس $\vect{B}$ را بیابید.

::: {.solution}
- با فرض منطبق بودن سیم بر محور $z$

$$\vect{B}=\uvec{\phi}\frac{k}{r}$$
$$\nabla\cdot\vect{B}=\frac1r\frac{\partial}{\partial r}(rB_r)+\frac1r\frac{\partial B_\phi}{\partial\phi}+\frac{\partial B_z}{\partial z}$$
$$\nabla\cdot\vect{B}=0$$

```{.figure #m01-ex15 caption=""}
```
:::
:::

## عملیات مشتق‌گیری - کرل

- **مفاهیم پیش‌نیاز برای ورود به بحث کرل**
    - گردش یک میدان برداری به دور یک مسیر بسته

$$\text{Circulation of }\vect{A}\text{ around contour }C\triangleq\oint_C\vect{A}\cdot\dif\vect{\ell}$$

- معنای فیزیکی گردش به نوع میدانی که بردار $\vect{A}$ نمایش می‌دهد بستگی دارد.
    - اگر $\vect{A}$ نیروی وارد بر یک جسم باشد، گردش $\vect{A}$ کار انجام شده توسط نیرو برای حرکت جسم به دور مسیر است.

::: {.definition title="کرل"}
کرل **میدان برداری** $\vect{A}$ در یک نقطه **برداری** است که اندازه آن حداکثر گردش خالص $\vect{A}$ در واحد سطح است وقتی که سطح حول نقطه به سمت صفر میل می‌کند و جهت آن جهت عمود سطح است زمانی که سطح طوری جهت داده شده باشد که گردش خالص را حداکثر کند.

$$\operatorname{curl}\vect{A}\equiv\nabla\times\vect{A}\triangleq\lim_{\Delta s\to0}\frac{1}{\Delta s}\left[\uvec{n}\oint_C\vect{A}\cdot\dif\vect{\ell}\right]_{\max}$$
:::

- در مختصات کارتزین رابطه کرل به صورت زیر است

::: {.important}
$$\nabla\times\vect{A}=\begin{vmatrix}\uvec{x}&\uvec{y}&\uvec{z}\\[1mm]\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\[3mm]A_x&A_y&A_z\end{vmatrix}$$
:::

- رابطه کلی کرل

::: {.important}
$$\nabla\times\vect{A}=\frac{1}{h_1h_2h_3}\begin{vmatrix}\uvec{u_1}h_1&\uvec{u_2}h_2&\uvec{u_3}h_3\\[1mm]\dfrac{\partial}{\partial u_1}&\dfrac{\partial}{\partial u_2}&\dfrac{\partial}{\partial u_3}\\[3mm]h_1A_1&h_2A_2&h_3A_3\end{vmatrix}$$
:::

- **مفهوم کرل**
    - چرخش یک چرخ پره‌دار درون جریان آب با بردار سرعت $u$
        - حداکثر سرعت زاویه‌ای چرخ پره‌دار متناسب با اندازه کرل بردار سرعت است.
        - محور چرخ با استفاده از قانون دست راست در جهت کرل قرار می‌گیرد.

```{.figure #m01-paddle-wheel caption=""}
```

::: {.example number="1-16"}
کرل بردار زیر را محاسبه کنید
$$\vect{A}=\uvec{\phi}\left(\frac{k}{r}\right)$$

::: {.solution}
$$\nabla\times\vect{A}=\frac1r\begin{vmatrix}\uvec{r}&\uvec{\phi}r&\uvec{z}\\[1mm]\dfrac{\partial}{\partial r}&\dfrac{\partial}{\partial\phi}&\dfrac{\partial}{\partial z}\\[3mm]0&k&0\end{vmatrix}=0$$

```{.figure #m01-ex16 caption=""}
```
:::
:::

## قضایای مهم برداری

```{.figure #m01-vector-analysis-map-thm caption=""}
```

::: {.theorem title="قضیه دیورژانس"}
انتگرال حجمی دیورژانس یک میدان برداری با شار کل خروجی بردار از سطح در برگیرنده حجم برابر است.
$$\int_V\nabla\cdot\vect{A}\,dv=\oint_S\vect{A}\cdot d\vect{s}$$
:::

```{.figure #m01-divergence-theorem caption=""}
```

::: {.theorem title="قضیه استوکس"}
انتگرال سطحی کرل یک میدان برداری، روی یک سطح باز برابر انتگرال خطی بسته بردار روی مسیری است که سطح را در بر می‌گیرد.
$$\int_S(\nabla\times\vect{A})\cdot d\vect{s}=\oint_C\vect{A}\cdot\dif\vect{\ell}$$
:::

```{.figure #m01-stokes-theorem caption=""}
```

::: {.theorem title="قضیه هلم‌هولتز"}
یک میدان برداری تا حد یک ثابت افزودنی تعیین می‌شود اگر هم دیورژانس و هم کرل آن مشخص باشد.
:::

::: {.example number="1-17"}
اعتبار قضیه دیورژانس را در مورد ناحیه پوسته‌ای محصور به سطوح کروی $R=R_1$ و $R=R_2$ $(R_2>R_1)$ به مرکز مبدأ مختصات برای میدان برداری زیر تحقیق نمایید.
$$\vect{F}=\uvec{R}kR$$

```{.figure #m01-ex17 caption=""}
```

::: {.solution}
$$\int_V\nabla\cdot\vect{A}\,dv=\oint_S\vect{A}\cdot d\vect{s}$$

- برای سطح بیرونی

$$R=R_2,\qquad d\vect{s}=\uvec{R}R_2^2\sin\theta\,d\theta\,d\phi$$
$$\int_{\substack{\text{outer}\\\text{surface}}}\vect{F}\cdot d\vect{s}=\int_0^{2\pi}\!\!\int_0^\pi(kR_2)R_2^2\sin\theta\,d\theta\,d\phi=4\pi kR_2^3$$

- برای سطح داخلی

$$R=R_1,\qquad d\vect{s}=-\uvec{R}R_1^2\sin\theta\,d\theta\,d\phi$$
$$\int_{\substack{\text{inner}\\\text{surface}}}\vect{F}\cdot d\vect{s}=-\int_0^{2\pi}\!\!\int_0^\pi(kR_1)R_1^2\sin\theta\,d\theta\,d\phi=-4\pi kR_1^3$$

$$\oint_S\vect{F}\cdot d\vect{s}=4\pi k(R_2^3-R_1^3)$$
$$\nabla\cdot\vect{F}=\frac{1}{R^2}\frac{\partial}{\partial R}(R^2F_R)=\frac{1}{R^2}\frac{\partial}{\partial R}(kR^3)=3k$$
$$\int_V\nabla\cdot\vect{F}\,dv=(\nabla\cdot\vect{F})V=4\pi k(R_2^3-R_1^3)$$
:::
:::

::: {.example number="1-18"}
اعتبار قضیه استوکس را روی یک چهارم قرص مدوری به شعاع ۳ در ربع اول برای میدان برداری زیر تحقیق نمایید.
$$\vect{F}=\uvec{x}xy-\uvec{y}2x$$

```{.figure #m01-ex18 caption=""}
```

::: {.solution}
$$\int_S(\nabla\times\vect{A})\cdot d\vect{s}=\oint_C\vect{A}\cdot\dif\vect{\ell}$$
$$\nabla\times\vect{F}=\begin{vmatrix}\uvec{x}&\uvec{y}&\uvec{z}\\[1mm]\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\[3mm]xy&-2x&0\end{vmatrix}=-\uvec{z}(2+x)$$
$$\int_S(\nabla\times\vect{F})\cdot d\vect{s}=\int_0^{\pi/2}\!\!\int_0^3-\uvec{z}(2+r\cos\phi)\cdot r\,dr\,d\phi\,\uvec{z}=-9\left(1+\frac{\pi}{2}\right)$$

- از $B$ تا $O$

$$x=0,\ \text{and}\ \vect{F}\cdot\dif\vect{\ell}=\vect{F}\cdot(\uvec{y}\,dy)=2x\,dy=0$$

- از $O$ تا $A$

$$y=0,\ \text{and}\ \vect{F}\cdot\dif\vect{\ell}=\vect{F}\cdot(\uvec{x}\,dx)=xy\,dx=0$$

$$\oint_{ABOA}\vect{F}\cdot\dif\vect{\ell}=\int_A^B\vect{F}\cdot\dif\vect{\ell}=-9\left(1+\frac{\pi}{2}\right)$$

(در مثال \ELnumc{1-11} بررسی شده بود)
:::
:::

## اتحادهای مهم برداری

::: {.important title="اتحاد I"}
کرل گرادیان هر کمیت عددی برابر با صفر است
$$\nabla\times(\nabla V)\equiv0$$
:::

- یک میدان برداری بدون کرل را یک میدان **غیرگردشی** یا **ابقایی** گویند.
- اگر یک کمیت برداری بدون کرل باشد، آنگاه می‌توان آن را به صورت گرادیان یک کمیت عددی بیان کرد.

::: {.important title="اتحاد II"}
دیورژانس کرل هر میدان برداری برابر با صفر است.
$$\nabla\cdot(\nabla\times\vect{A})\equiv0$$
:::

- یک میدان برداری بدون دیورژانس را یک میدان **سلونوئیدی** گویند.
- اگر یک کمیت برداری بدون دیورژانس باشد، آنگاه می‌توان آن را به صورت کرل یک کمیت برداری بیان کرد.
