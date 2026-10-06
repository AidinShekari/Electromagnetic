# میدان‌های الکتریکی ساکن

## سرفصل‌ها

```{.figure #m02-course-outline caption=""}
```

## میدان‌های الکتریکی ساکن

- در الکتریسیته ساکن بارهای الکتریکی در حال سکون هستند و میدان‌های الکتریکی با زمان تغییر نمی‌کنند.
    - در این حالت میدان‌های مغناطیسی وجود ندارند.
- توسعه الکتریسیته ساکن در فیزیک مقدماتی عموماً با قانون تجربی کولمب در مورد نیروی بین دو بار آغاز می‌شود.
- در این درس به جای دنبال کردن پیشرفت تاریخی الکتریسیته ساکن، موضوع را با فرض دیورژانس و کرل شدت میدان الکتریکی در فضای آزاد معرفی می‌نماییم.

```{.figure #m02-map caption=""}
```

- فرضیات اصلی الکتریسیته ساکن که بر اساس آن‌ها می‌توان دیگر روابط و قوانین این حوزه را استخراج کرد کدامند؟
- چگونه با استفاده از فرضیات فوق قوانین کولمب و گوس استخراج می‌شوند؟
- میدان الکتریکی ناشی از یک بار نقطه‌ای، تعدادی بار نقطه‌ای گسسته و یک توزیع بار پیوسته چگونه محاسبه می‌شود؟

## فرضیات اصلی الکتریسیته ساکن در فضای آزاد

- **شدت میدان الکتریکی**
    - نیروی وارد بر یک بار کوچک آزمون هنگامیکه در میدان قرار داده می‌شود، تقسیم بر بار. $\ELto$ $\mathrm{N/C}$ (نیوتن بر کولمب) معادل $\mathrm{V/m}$ (ولت بر متر)

::: {.definition}
$$\vect{E}=\lim_{q\to0}\frac{\vect{F}}{q}\qquad(\mathrm{V/m})$$
:::

- شدت میدان الکتریکی متناسب و هم‌جهت با نیرو است.
- دو فرض اساسی الکتریسیته ساکن در فضای آزاد

::: {.important}
$$\nabla\cdot\vect{E}=\frac{\rho}{\epsilon_0}\qquad\qquad \nabla\times\vect{E}=0$$
:::

- $\rho$: چگالی حجمی بار $(\mathrm{C/m^3})$؛ $\epsilon_0$: گذردهی فضای آزاد $(\mathrm{F/m})$
- $\vect{E}$ سلونوئیدی نیست مگر اینکه $\rho=0$
- $\vect{E}$ غیرگردشی است

- شکل انتگرالی معادله اول $\ELto$ انتگرال‌گیری روی حجم دلخواه $V$

$$\int_V\nabla\cdot\vect{E}\,dv=\frac{1}{\epsilon_0}\int_V\rho\,dv$$

- $\int_V\rho\,dv$: کل بار موجود در حجم $V$ احاطه شده توسط سطح $S$
- با استفاده از قضیه دیورژانس:

::: {.important}
$$\oint_S\vect{E}\cdot d\vect{s}=\frac{Q}{\epsilon_0}$$
:::

- این رابطه شکلی از **قانون گوس** است
    - شار کل خروجی شدت میدان الکتریکی از هر سطح بسته برابر با کل بار داخل سطح تقسیم بر $\epsilon_0$ است.

- شکل انتگرالی معادلات دوم $\ELto$ انتگرال‌گیری روی سطح باز دلخواه $S$

$$\int_S(\nabla\times\vect{E})\cdot d\vect{s}=0$$

- با استفاده از قضیه استوکس:

::: {.important}
$$\oint_C\vect{E}\cdot\dif\vect{\ell}=0$$
:::

- انتگرال خطی عددی شدت میدان الکتریکی ساکن دور هر مسیر بسته صفر است.
- حاصلضرب عددی $\vect{E}\cdot\dif\vect{\ell}$ روی هر مسیری که انتگرال‌گیری شود، ولتاژ در امتداد آن مسیر است.
- این معادله بیانی از **قانون ولتاژ کرشهف** است
    - مجموع جبری افت ولتاژهای اطراف هر مسیر بسته برابر با صفر است.

- انتگرال‌های خطی میدان غیرگردشی $\vect{E}$ مستقل از مسیر بوده و فقط به نقاط ابتدایی و انتهایی بستگی دارد.

```{.figure #m02-two-paths caption=""}
```

$$\oint_C\vect{E}\cdot\dif\vect{\ell}=0$$
$$\int_{C_1}\vect{E}\cdot\dif\vect{\ell}+\int_{C_2}\vect{E}\cdot\dif\vect{\ell}=0$$
$$\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}+\int_{P_2}^{P_1}\vect{E}\cdot\dif\vect{\ell}=0$$
$$\int_{\substack{P_1\\\text{Along }C_1}}^{P_2}\vect{E}\cdot\dif\vect{\ell}=-\int_{\substack{P_2\\\text{Along }C_2}}^{P_1}\vect{E}\cdot\dif\vect{\ell}$$
$$\int_{\substack{P_1\\\text{Along }C_1}}^{P_2}\vect{E}\cdot\dif\vect{\ell}=\int_{\substack{P_1\\\text{Along }C_2}}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

## قانون کولمب

```{.figure #m02-map-coulomb caption=""}
```

- **شدت میدان الکتریکی ناشی از بار نقطه‌ای $q$ در فضای آزاد**
    - سطح کروی فرضی به شعاع $R$ و مرکز $q$ را در نظر می‌گیریم.
    - چون بار نقطه‌ای دارای هیچ جهت خاصی نیست، انتظار داریم که میدان در همه جا شعاعی بوده و شدت آن برروی سطح کره ثابت باشد.

```{.figure #m02-point-charge caption=""}
```

- شدت میدان الکتریکی روی سطح کره:

$$\vect{E}=E_R\uvec{R}$$
$$\oint_S\vect{E}\cdot d\vect{s}=\oint_S(\uvec{R}E_R)\cdot\uvec{R}\,ds=\frac{q}{\epsilon_0}$$
$$E_R\oint_S ds=E_R(4\pi R^2)=\frac{q}{\epsilon_0}$$

::: {.important}
$$\vect{E}=\uvec{R}E_R=\uvec{R}\frac{q}{4\pi\epsilon_0R^2}\qquad(\mathrm{V/m})$$
:::

- اگر بار در مرکز دستگاه مختصات نباشد

```{.figure #m02-offset-charge caption=""}
```

$$\vect{E}_P=\uvec{qP}\frac{q}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^2},\qquad \uvec{qP}=\frac{\vect{R}-\vect{R}'}{\abs{\vect{R}-\vect{R}'}}$$

::: {.important}
$$\vect{E}_P=\frac{q(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}\qquad(\mathrm{V/m})$$
:::

- هنگامیکه بار نقطه‌ای $q_2$ در میدان الکتریکی بار نقطه‌ای دیگر $q_1$ قرار می‌گیرد، نیروی وارد بر آن برابر است با

::: {.important title="بیان ریاضی قانون کولمب"}
$$\vect{F}_{12}=q_2\vect{E}_{12}=\uvec{R}\frac{q_1q_2}{4\pi\epsilon_0R^2}\qquad(\mathrm{N})$$
:::

```{.figure #m02-two-charges caption=""}
```

- **شدت میدان الکتریکی ناشی از مجموعه بارهای گسسته**

::: {.important}
$$\vect{E}=\frac{1}{4\pi\epsilon_0}\sum_{k=1}^{n}\frac{q_k(\vect{R}-\vect{R}'_k)}{\abs{\vect{R}-\vect{R}'_k}^3}\qquad(\mathrm{V/m})$$
:::

```{.figure #m02-discrete-charges caption=""}
```

- **شدت میدان الکتریکی ناشی از توزیع پیوسته بار**
    - میدان ناشی از بار دیفرانسیلی $dq$ برابر است با

$$d\vect{E}=\frac{dq(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- توزیع بار خطی

$$dq=\rho_\ell\,d\ell'\qquad\qquad \vect{E}=\int_{L'}\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- توزیع بار سطحی

$$dq=\rho_s\,ds'\qquad\qquad \vect{E}=\int_{S'}\frac{\rho_s\,ds'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- توزیع بار حجمی

$$dq=\rho_v\,dv'\qquad\qquad \vect{E}=\int_{V'}\frac{\rho_v\,dv'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- **مراحل محاسبه شدت میدان الکتریکی یک توزیع پیوسته بار**
    - تعیین دستگاه مختصات مناسب
    - تعیین صحیح المان دیفرانسیلی $d\ell'$، $ds'$ و $dv'$ (دقت شود در این روابط اندازه بردار های دیفرانسیل طول و سطح استفاده شده است)
    - تعیین صحیح بردار مکان نقطه مشاهده $(\vect{R})$
    - تعیین صحیح بردار مکان نقطه منبع $(\vect{R}')$
    - محاسبه انتگرال
        - دقت شود که نسبت به مختصات پریم‌دار انتگرال می‌گیریم.

::: {.example number="2-1"}
شدت میدان الکتریکی یک بار خطی مستقیم و به طول بینهایت را با چگالی یکنواخت $\rho_\ell$ تعیین کنید.

```{.figure #m02-ex1 caption=""}
```

::: {.solution}
$$\vect{E}=\int_{L'}\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- انتخاب دستگاه مختصات استوانه‌ای

$$d\ell'=dz'\qquad \vect{R}=r\uvec{r}\qquad \vect{R}'=z'\uvec{z}$$
$$\vect{E}=\frac{\rho_\ell}{4\pi\epsilon_0}\int_{-\infty}^{\infty}\frac{r\uvec{r}-z'\uvec{z}}{(r^2+z'^2)^{3/2}}\,dz'$$

- به صورت شهودی واضح است که میدان مولفه در راستای $z$ ندارد.

$$\vect{E}=\uvec{r}E_r=\uvec{r}\frac{\rho_\ell r}{4\pi\epsilon_0}\int_{-\infty}^{\infty}\frac{dz'}{(r^2+z'^2)^{3/2}}$$
$$\vect{E}=\uvec{r}\frac{\rho_\ell}{2\pi\epsilon_0r}\qquad(\mathrm{V/m})$$
:::
:::

::: {.example number="2-2"}
حلقه‌ای به شعاع $a$ و چگالی بار خطی $\rho_\ell$ داریم. مطلوبست محاسبه شدت میدان الکتریکی روی محور حلقه به فاصله $h$ از آن.

```{.figure #m02-ex2 caption=""}
```

::: {.solution}
$$\vect{E}=\int_{L'}\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- انتخاب دستگاه مختصات استوانه‌ای

$$d\ell'=a\,d\phi'\qquad \vect{R}=h\uvec{z}\qquad \vect{R}'=a\uvec{r'}$$
$$\vect{E}=\frac{\rho_\ell}{4\pi\epsilon_0}\int_0^{2\pi}\frac{h\uvec{z}-a\uvec{r'}}{(a^2+h^2)^{3/2}}\,a\,d\phi'$$

- به صورت شهودی واضح است که میدان مولفه در راستای $r$ ندارد.

$$\vect{E}=\frac{\rho_\ell ah}{4\pi\epsilon_0(a^2+h^2)^{3/2}}\uvec{z}\int_0^{2\pi}d\phi'=\frac{\rho_\ell ah}{2\epsilon_0(a^2+h^2)^{3/2}}\uvec{z}$$
:::
:::

::: {.example number="2-3"}
شدت میدان الکتریکی یک بار مسطح بینهایت با چگالی بار سطحی یکنواخت $\rho_s$ را تعیین کنید.

```{.figure #m02-ex3 caption=""}
```

::: {.solution}
$$\vect{E}=\int_{S'}\frac{\rho_s\,ds'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- انتخاب دستگاه مختصات استوانه‌ای

$$ds'=r'\,dr'\,d\phi'\qquad \vect{R}=h\uvec{z}\qquad \vect{R}'=r'\uvec{r'}$$
$$\vect{E}=\frac{\rho_s}{4\pi\epsilon_0}\int_0^{2\pi}\!\!\int_0^{\infty}\frac{h\uvec{z}-r'\uvec{r'}}{(h^2+r'^2)^{3/2}}\,r'\,dr'\,d\phi'$$

- به صورت شهودی واضح است که میدان مولفه در راستای $r$ ندارد.

$$\vect{E}=\frac{\rho_sh\uvec{z}}{4\pi\epsilon_0}\int_0^{2\pi}\!\!\int_0^{\infty}\frac{r'\,dr'\,d\phi'}{(h^2+r'^2)^{3/2}}=\frac{\rho_s}{2\epsilon_0}\uvec{z}$$
:::
:::

## قانون گوس

```{.figure #m02-map-gauss caption=""}
```

::: {.important}
$$\oint_S\vect{E}\cdot d\vect{s}=\frac{Q}{\epsilon_0}$$
:::

- $Q$: کل بار موجود در حجم $V$ احاطه شده توسط سطح $S$
- شار کل خروجی شدت میدان الکتریکی از هر سطح بسته برابر با کل بار داخل سطح تقسیم بر $\epsilon_0$ است.
- سطح $S$ می‌تواند هر سطح بسته اختیاری باشد که به دلیل راحتی انتخاب شده است.

::: {.remark}
قانون گوس همیشه برقرار است اما در استفاده از آن برای تعیین شدت میدان الکتریکی باید به نکته زیر دقت شود.

- اساس بکارگیری قانون گوس، برای تعیین شدت میدان الکتریکی، نخست در تشخیص شرایط تقارنی و دوم در انتخاب مناسب سطحی که روی آن مؤلفه عمودی $\vect{E}$ ناشی از یک توزیع بار مشخص ثابت باشد (سطح گوسی)، است.
:::

::: {.example number="2-4"}
با استفاده از قانون گوس، شدت میدان الکتریکی ناشی از یک بار خطی مستقیم و بینهایت بلند را با چگالی یکنواخت $\rho_\ell$ در فاصله $r$ از آن تعیین کنید.

```{.figure #m02-ex4 caption=""}
```

::: {.solution}
$$\vect{E}=\uvec{r}E_r$$

- انتخاب یک استوانه به طول $L$ و شعاع $r$ به عنوان سطح گوسی
    - برای سطح بالایی و پایینی: $\vect{E}\cdot d\vect{s}=0$
    - برای سطح جانبی: $d\vect{s}=\uvec{r}\,r\,d\phi\,dz$

$$\oint_S\vect{E}\cdot d\vect{s}=\int_0^L\!\!\int_0^{2\pi}E_r\,r\,d\phi\,dz=2\pi rLE_r$$
$$Q=\rho_\ell L\qquad 2\pi rLE_r=\frac{\rho_\ell L}{\epsilon_0}\qquad \vect{E}=\uvec{r}E_r=\uvec{r}\frac{\rho_\ell}{2\pi\epsilon_0r}$$
:::
:::

::: {.example number="2-5"}
شدت میدان الکتریکی ناشی از یک بار مسطح بینهایت با چگالی بار سطحی یکنواخت $\rho_s$ را تعیین کنید.

```{.figure #m02-ex5 caption=""}
```

::: {.solution}
$$\vect{E}=\pm E_z\uvec{z}$$

- انتخاب یک مکعب به عنوان سطح گوسی
- برای سطح بالایی

$$\vect{E}\cdot d\vect{s}=(\uvec{z}E_z)\cdot(\uvec{z}\,ds)=E_z\,ds$$

- برای سطح پایینی

$$\vect{E}\cdot d\vect{s}=(-\uvec{z}E_z)\cdot(-\uvec{z}\,ds)=E_z\,ds$$

- برای سطوح جانبی

$$\vect{E}\cdot d\vect{s}=0$$

- بنابراین

$$\oint_S\vect{E}\cdot d\vect{s}=2E_z\int_A ds=2E_zA$$
$$Q=\rho_sA\qquad 2E_zA=\frac{\rho_sA}{\epsilon_0}$$

::: {.important}
$$\vect{E}=\uvec{z}E_z=\uvec{z}\frac{\rho_s}{2\epsilon_0},\qquad z>0$$
$$\vect{E}=-\uvec{z}E_z=-\uvec{z}\frac{\rho_s}{2\epsilon_0},\qquad z<0$$
:::
:::
:::

::: {.example number="2-6"}
میدان $\vect{E}$ ناشی از یک ابر الکترونی با چگالی بار حجمی $\rho=-\rho_0$ در ناحیه $0\leq R\leq b$ و $\rho=0$ در ناحیه $R>b$ را تعیین کنید.

```{.figure #m02-ex6 caption=""}
```

::: {.solution}
$$\vect{E}=\uvec{R}E_R$$

- الف) $0\leq R\leq b$
    - انتخاب یک کره به عنوان سطح گوسی

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_i}\vect{E}\cdot d\vect{s}=E_R\int_{S_i}ds=E_R4\pi R^2$$
$$Q=\int_V\rho\,dv=-\rho_0\int_V dv=-\rho_0\frac{4\pi}{3}R^3\qquad \vect{E}=-\uvec{R}\frac{\rho_0}{3\epsilon_0}R$$

- ب) $R\geq b$
    - انتخاب یک کره به عنوان سطح گوسی

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_o}\vect{E}\cdot d\vect{s}=E_R\int_{S_o}ds=E_R4\pi R^2$$
$$Q=-\rho_0\frac{4\pi}{3}b^3\qquad \vect{E}=-\uvec{R}\frac{\rho_0b^3}{3\epsilon_0R^2}$$
:::
:::

::: {.example number="2-7"}
یک توزیع بار کروی به شعاع $b$ دارای چگالی زیر است. شدت میدان الکتریکی را در تمام نقاط فضا بدست آورید.
$$\rho_v=\begin{cases}\dfrac{\rho_0R}{b}&0\leq R\leq b\\[2mm]0&R>b\end{cases}$$

```{.figure #m02-ex7 caption=""}
```

::: {.solution}
$$\vect{E}=\uvec{R}E_R$$

- الف) $0\leq R\leq b$
    - انتخاب یک کره به عنوان سطح گوسی

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_i}\vect{E}\cdot d\vect{s}=E_R\int_{S_i}ds=E_R4\pi R^2$$
$$Q=\int_v\rho_v\,dv=\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^{R}\frac{\rho_0R}{b}R^2\sin\theta\,dR\,d\theta\,d\phi=\frac{\rho_0\pi R^4}{b}$$
$$\vect{E}=E_R\uvec{R}=\frac{\rho_0R^2}{4\epsilon_0b}\uvec{R}$$

- ب) $R\geq b$
    - انتخاب یک کره به عنوان سطح گوسی

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_o}\vect{E}\cdot d\vect{s}=E_R\int_{S_o}ds=E_R4\pi R^2\qquad Q=\rho_0\pi b^3$$
$$\vect{E}=E_R\uvec{R}=\frac{\rho_0b^3}{4\epsilon_0R^2}\uvec{R}$$
:::
:::

## پتانسیل الکتریکی

```{.figure #m02-map-potential caption=""}
```

- مفهوم اختلاف پتانسیل الکتریکی بین دو نقطه و پتانسیل الکتریکی یک نقطه چیست؟
- پتانسیل الکتریکی ناشی از یک بار نقطه‌ای، تعدادی بار نقطه‌ای گسسته و یک توزیع بار پیوسته چگونه محاسبه می‌شود؟
- چگونه می‌توان با استفاده از پتانسیل الکتریکی، شدت میدان الکتریکی را محاسبه کرد و مزیت این کار نسبت به محاسبه مستقیم شدت میدان الکتریکی چیست؟

- فرض کنید که می‌خواهیم بار نقطه‌ای $q$ را که در میدان الکتریکی $\vect{E}$ قرار دارد، به اندازه $d\ell$ حرکت دهیم.

```{.figure #m02-move-charge caption=""}
```

- نیروی وارد بر بار توسط میدان الکتریکی:
$$\vect{F}_E=q\vect{E}$$

- اندازه مؤلفه این نیرو در راستای $d\ell$:
$$F_{EL}=\vect{F}_E\cdot\uvec{\ell}=q\vect{E}\cdot\uvec{\ell}$$

- نیرویی که باید به بار اعمال شود:
$$F_{apply}=-F_{EL}=-q\vect{E}\cdot\uvec{\ell}$$

- کار انجام شده برای حرکت بار به اندازه $d\ell$:
$$dW=F_{apply}\,d\ell=-q\vect{E}\cdot\dif\vect{\ell}$$

- کار انجام شده برای حرکت بار از نقطه $P_1$ به نقطه $P_2$:
$$W=-q\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

$$\nabla\times\vect{E}=0\Rightarrow\vect{E}=-\nabla V$$
$$\nabla V\cdot\uvec{\ell}=\frac{dV}{d\ell}$$
$$q=+1\,\mathrm{C}\qquad W=\int_{P_1}^{P_2}\nabla V\cdot\dif\vect{\ell}\quad\Longrightarrow\quad W=\int_{P_1}^{P_2}dV=V_2-V_1$$

::: {.definition title="اختلاف پتانسیل الکتریکی"}
اختلاف پتانسیل الکتریکی بین دو نقطه، کار انجام شده بوسیله منبع بیرونی در حرکت بار مثبت واحد از یک نقطه به نقطه دیگر است.
$$V_2-V_1=-\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

- به مسیر انتگرال‌گیری وابسته نیست
:::

- معمولاً در بسیاری از موارد یک نقطه مرجع در بینهایت با پتانسیل صفر در نظر می‌گیرند و اختلاف پتانسیل نقاط مختلف نسبت به این نقطه مرجع را بیان می‌کنند.

::: {.important}
$$V_P=-\int_{\infty}^{P}\vect{E}\cdot\dif\vect{\ell}$$
:::

::: {.remark title="نکته ۱"}
علامت منفی در رابطه پتانسیل برای مطابقت با این بحث که حرکت در خلاف جهت میدان باعث افزایش پتانسیل الکتریکی می‌شود لازم است.
:::

::: {.remark title="نکته ۲"}
گرادیان $V$ عمود بر سطوح $V$ ثابت است و در نتیجه خطوط میدان الکتریکی عمود بر سطوح هم‌پتانسیل هستند.
:::

- **پتانسیل الکتریکی ناشی از بار نقطه‌ای $q$ به فاصله $R$ از آن**

```{.figure #m02-potential-point caption=""}
```

$$V=-\int_{\infty}^{R}\left(\frac{q}{4\pi\epsilon_0R^2}\uvec{R}\right)\cdot dR\,\uvec{R}=\frac{q}{4\pi\epsilon_0R}$$

- **پتانسیل الکتریکی ناشی از $n$ بار نقطه‌ای گسسته**

$$V=\frac{1}{4\pi\epsilon_0}\sum_{k=1}^{n}\frac{q_k}{\abs{\vect{R}-\vect{R}'_k}}$$

- $\vect{R}$: بردار مکان نقطه مشاهده؛ $\vect{R}'_k$: بردار مکان نقاط منبع

- **پتانسیل الکتریکی ناشی از توزیع پیوسته بار**
    - توزیع بار خطی
$$V=\frac{1}{4\pi\epsilon_0}\int_{L'}\frac{\rho_\ell\,d\ell'}{\abs{\vect{R}-\vect{R}'}}$$

    - توزیع بار سطحی
$$V=\frac{1}{4\pi\epsilon_0}\int_{S'}\frac{\rho_s\,ds'}{\abs{\vect{R}-\vect{R}'}}$$

    - توزیع بار حجمی
$$V=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho_v\,dv'}{\abs{\vect{R}-\vect{R}'}}$$

::: {.example number="2-8"}
پتانسیل الکتریکی و شدت میدان الکتریکی ناشی از یک دوقطبی الکتریکی را در یک نقطه دلخواه به فاصله بسیار دور از آن بدست آورید.

::: {.solution}
$$V=\frac{1}{4\pi\epsilon_0}\sum_{k=1}^{2}\frac{q_k}{\abs{\vect{R}-\vect{R}'_k}}=\frac{1}{4\pi\epsilon_0}\left[\frac{q}{\abs{\vect{R}-\vect{d}/2}}+\frac{-q}{\abs{\vect{R}+\vect{d}/2}}\right]$$

```{.figure #m02-ex8-dipole caption=""}
```

$$V=\frac{q}{4\pi\epsilon_0}\left(\frac{1}{R_+}-\frac{1}{R_-}\right)$$
$$\frac{1}{R_+}\cong\left(R-\frac{d}{2}\cos\theta\right)^{-1}\cong R^{-1}\left(1+\frac{d}{2R}\cos\theta\right)$$
$$\frac{1}{R_-}\cong\left(R+\frac{d}{2}\cos\theta\right)^{-1}\cong R^{-1}\left(1-\frac{d}{2R}\cos\theta\right)$$

- $\vect{p}=q\vect{d}$: بردار گشتاور دوقطبی الکتریکی

$$V=\frac{qd\cos\theta}{4\pi\epsilon_0R^2}\quad\overset{\vect{d}=d\uvec{z}}{\Longrightarrow}\quad V=\frac{q\vect{d}\cdot\uvec{R}}{4\pi\epsilon_0R^2}\quad\overset{\vect{p}=q\vect{d}}{\Longrightarrow}\quad V=\frac{\vect{p}\cdot\uvec{R}}{4\pi\epsilon_0R^2}$$
$$\begin{aligned}\vect{E}=-\nabla V&=-\uvec{R}\frac{\partial V}{\partial R}-\uvec{\theta}\frac{\partial V}{R\,\partial\theta}\\&=\frac{p}{4\pi\epsilon_0R^3}(\uvec{R}2\cos\theta+\uvec{\theta}\sin\theta)\end{aligned}$$

```{.figure #m02-ex8-field caption=""}
```
:::
:::

::: {.example number="2-9"}
پتانسیل الکتریکی و شدت میدان الکتریکی ناشی از یک دیسک باردار به شعاع $b$ و چگالی بار سطحی $\rho_s$ را بر روی محور آن بدست آورید.

```{.figure #m02-ex9 caption=""}
```

::: {.solution}
$$V=\frac{1}{4\pi\epsilon_0}\int_{S'}\frac{\rho_s\,ds'}{\abs{\vect{R}-\vect{R}'}}$$
$$ds'=r'\,dr'\,d\phi'\qquad \vect{R}=z\uvec{z}\qquad \vect{R}'=r'\uvec{r'}$$
$$V=\frac{\rho_s}{4\pi\epsilon_0}\int_0^{2\pi}\!\!\int_0^{b}\frac{r'\,dr'\,d\phi'}{\sqrt{z^2+r'^2}}=\frac{\rho_s}{2\epsilon_0}\left[\sqrt{z^2+b^2}-z\right]\qquad z>0$$
$$\vect{E}=-\nabla V=\uvec{z}\frac{\rho_s}{2\epsilon_0}\left[1-\frac{z}{\sqrt{z^2+b^2}}\right]\qquad z>0$$
:::
:::

::: {.example number="2-10"}
پتانسیل الکتریکی و شدت میدان الکتریکی ناشی از یک بار خطی به طول $L$ و چگالی بار $\rho_\ell$ را در امتداد آن بدست آورید.

```{.figure #m02-ex10 caption=""}
```

::: {.solution}
$$V=\frac{1}{4\pi\epsilon_0}\int_{L'}\frac{\rho_\ell\,d\ell'}{\abs{\vect{R}-\vect{R}'}}$$
$$d\ell'=dz'\qquad \vect{R}=z\uvec{z}\qquad \vect{R}'=z'\uvec{z}$$
$$V=\frac{\rho_\ell}{4\pi\epsilon_0}\int_{-L/2}^{L/2}\frac{dz'}{z-z'}=\frac{\rho_\ell}{4\pi\epsilon_0}\ln\left[\frac{z+L/2}{z-L/2}\right]\qquad z>L/2$$
$$\vect{E}=-\nabla V=-\uvec{z}\frac{dV}{dz}=\uvec{z}\frac{\rho_\ell L}{4\pi\epsilon_0\left[z^2-(L/2)^2\right]}\qquad z>L/2$$
:::
:::

::: {.example number="2-11"}
توزیع بار حجمی با چگالی $\rho=-\rho_0$ در ناحیه $0\leq R\leq b$ وجود دارد. پتانسیل الکتریکی در یک نقطه دلخواه درون این حجم چقدر است؟

```{.figure #m02-ex11 caption=""}
```

::: {.solution}
$$\vect{E}=-\uvec{R}\frac{\rho_0}{3\epsilon_0}R,\qquad 0\leq R\leq b$$
$$\vect{E}=-\uvec{R}\frac{\rho_0b^3}{3\epsilon_0R^2},\qquad R\geq b$$
$$\begin{aligned}V=-\int_{\infty}^{R}\vect{E}\cdot\dif\vect{\ell}&=-\int_{\infty}^{b}\frac{-\rho_0b^3}{3\epsilon_0R^2}\uvec{R}\cdot dR\,\uvec{R}-\int_{b}^{R}\frac{-\rho_0R}{3\epsilon_0}\uvec{R}\cdot dR\,\uvec{R}\\&=-\frac{\rho_0b^2}{3\epsilon_0}-\frac{\rho_0}{6\epsilon_0}\left(b^2-R^2\right)\end{aligned}$$
:::
:::

## رفتار میدان الکتریکی ساکن در محیط‌های مادی

```{.figure #m02-map-media caption=""}
```

- تقسیم بندی مواد براساس خواص الکتریکی
    - هادی‌ها
    - نیمه‌هادی‌ها
    - عایق‌ها (دی‌الکتریک‌ها)
- در هادی‌ها الکترون‌های لایه‌های بیرونی اتم‌ها با نیروی ضعیفی نگه داشته شده‌اند و به سادگی از یک اتم به اتم دیگر منتقل می‌شوند.
- اما الکترون‌ها در اتم عایق‌ها به شدت به مدار خود چسبیده‌اند و در شرایط عادی قادر به جدا شدن نمی‌باشند.
- خواص الکتریکی نیمه‌هادی‌ها بین خواص الکتریکی هادی‌ها و عایق‌ها قرار دارد.

- رفتار شدت میدان الکتریکی ساکن در حضور یک هادی چگونه است؟
- رفتار شدت میدان الکتریکی ساکن در حضور یک دی الکتریک چگونه است؟
- مفهوم چگالی شار الکتریکی چیست و چه رابطه ای با شدت میدان الکتریکی دارد؟
- مفهوم ضریب دی الکتریک چیست؟
- رفتار شدت میدان الکتریکی ساکن در مرز بین دو محیط متفاوت چگونه است؟

## هادی‌ها در میدان الکتریکی ساکن

- اگر بارهایی را درون یک هادی رها کنیم، میدانی در آن تشکیل می‌شود که باعث دور شدن بارها از هم و آمدن آن‌ها به سطح می‌شود.
    - در شرایط سکون بار و میدان الکتریکی درون یک هادی صفر است.
$$\rho=0\qquad \vect{E}=0$$

    - زمان لازم برای توزیع بارها به سطح هادی و ایجاد حالت تعادل به میزان رسانندگی هادی بستگی دارد.
- اگر در شرایط سکون میدان الکتریکی روی سطح هادی دارای مؤلفه مماسی باشد، تولید یک نیروی مماسی نموده، بارها را به حرکت درآورده و حالت تعادل بار وجود نخواهد داشت.
    - بنابراین تحت شرایط سکون، میدان الکتریکی روی سطح یک هادی همه جا عمود بر سطح است. به عبارت دیگر تحت شرایط سکون سطح هادی یک سطح هم‌پتانسیل است. در واقع چون در تمام نقاط درون هادی $\vect{E}=0$ است، کل هادی دارای پتانسیل الکتریکی یکسانی است.

- **شرایط مرزی در مرز بین هادی/فضای آزاد**

```{.figure #m02-conductor-boundary caption=""}
```

- مؤلفه عمودی:
$$\oint_S\vect{E}\cdot d\vect{s}=E_n\Delta S=\frac{\rho_s\Delta S}{\epsilon_0}\qquad\Longrightarrow\qquad E_n=\frac{\rho_s}{\epsilon_0}$$

- مؤلفه مماسی:
$$\oint\vect{E}\cdot d\vect{L}=0$$
$$E_t\Delta w-E_{N,\text{at }b}\tfrac12\Delta h+E_{N,\text{at }a}\tfrac12\Delta h=0\qquad\Longrightarrow\qquad E_t=0$$

::: {.example number="2-12"}
بار نقطه‌ای $+Q$ در مرکز یک پوسته کروی هادی به شعاع داخلی $R_i$ و شعاع خارجی $R_o$ قرار دارد. $\vect{E}$ و $V$ را در کل فضا بدست آورید.

```{.figure #m02-ex12 caption=""}
```

::: {.solution}
$$\vect{E}=E_R\uvec{R}$$

- به ازای $R>R_o$

$$\oint_S\vect{E}\cdot d\vect{s}=E_{R1}4\pi R^2=\frac{Q}{\epsilon_0}$$
$$E_{R1}=\frac{Q}{4\pi\epsilon_0R^2}\qquad V_1=-\int_{\infty}^{R}(E_{R1})\,dR=\frac{Q}{4\pi\epsilon_0R}$$

- به ازای $R_i<R<R_o$

$$E_{R2}=0\qquad V_2=V_1\Big|_{R=R_o}=\frac{Q}{4\pi\epsilon_0R_o}$$

- به ازای $R<R_i$

$$E_{R3}=\frac{Q}{4\pi\epsilon_0R^2}$$
$$V_3=-\int_{\infty}^{R_o}E_{R1}\,dR-\int_{R_o}^{R_i}E_{R2}\,dR-\int_{R_i}^{R}E_{R3}\,dR$$
$$V_3=\frac{Q}{4\pi\epsilon_0}\left(\frac1R+\frac{1}{R_o}-\frac{1}{R_i}\right)$$

```{.figure #m02-ex12-plots caption=""}
```
:::
:::

## دی‌الکتریک‌ها در میدان الکتریکی ساکن

- دی‌الکتریک‌های ایده‌آل دارای بار آزاد نیستند. در نتیجه مانند هادی‌ها چگالی بار و میدان الکتریکی داخلی آن‌ها برابر با صفر نیست.
- دی‌الکتریک‌ها دارای **بارهای مقید** بوده و اعمال میدان خارجی به دی‌الکتریک باعث ایجاد دو قطبی‌های الکتریکی شده و ماده دی‌الکتریک را قطبی می‌کند.
- دو قطبی‌های الکتریکی القا شده میدان الکتریکی را در داخل و خارج ماده دی‌الکتریک تغییر می‌دهند.

```{.figure #m02-polarization caption=""}
```

- **توزیع‌های بار معادل در دی‌الکتریک‌های قطبی شده**
    - برای تجزیه و تحلیل تأثیر ماکروسکوپی دوقطبی‌های القا شده، بردار قطبی‌شدگی $\vect{P}$ را به صورت زیر تعریف می‌کنیم

::: {.definition}
$$\vect{P}=\lim_{\Delta v\to0}\frac{\sum_{k=1}^{n\Delta v}\vect{p}_k}{\Delta v}\qquad(\mathrm{C/m^2})$$

- $n$: تعداد دوقطبی ها در واحد حجم؛ $\vect{p}_k$: گشتاور دوقطبی
:::

- اگر $d\vect{p}$ گشتاور دو قطبی در یک حجم کوچک $dv'$ باشد، آنگاه

$$d\vect{p}=\vect{P}\,dv'\qquad dV=\frac{\vect{P}\cdot\uvec{R}}{4\pi\epsilon_0R^2}\,dv'\qquad V=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\vect{P}\cdot\uvec{R}}{R^2}\,dv'$$
$$V=\frac{1}{4\pi\epsilon_0}\oint_{S'}\frac{\vect{P}\cdot\vect{a}'_n}{R}\,ds'+\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{(-\nabla'\cdot\vect{P})}{R}\,dv'$$

- پتانسیل الکتریکی و بنابراین شدت میدان الکتریکی ناشی از دی‌الکتریک قطبی شده می‌تواند از اثر توزیع‌های دو بار سطحی و حجمی به ترتیب با چگالی‌های زیر که آن‌ها را **چگالی بار قطبی‌شدگی** یا **چگالی بار مقید** می‌نامند، محاسبه شود

::: {.important}
$$\rho_{ps}=\vect{P}\cdot\uvec{n}\qquad\qquad \rho_p=-\nabla\cdot\vect{P}$$
$$V=\frac{1}{4\pi\epsilon_0}\oint_{S'}\frac{\rho_{ps}}{R}\,ds'+\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho_p}{R}\,dv'$$
:::

::: {.remark}
چون با یک جسم دی‌الکتریک خنثی از نظر الکتریکی سروکار داریم، بار کل جسم پس از قطبی شدن باید همچنان صفر باشد
$$\begin{aligned}\text{Total charge}&=\oint_S\rho_{ps}\,ds+\int_V\rho_p\,dv\\&=\oint_S\vect{P}\cdot\uvec{n}\,ds-\int_V\nabla\cdot\vect{P}\,dv=0\end{aligned}$$
:::

## چگالی شار الکتریکی

```{.figure #m02-map-flux caption=""}
```

- چون یک دی‌الکتریک موجب پیدایش چگالی بار حجمی معادل $\rho_p$ می‌شود، انتظار داریم که شدت میدان الکتریکی ناشی از یک توزیع بار مفروض در یک دی‌الکتریک با شدت میدان الکتریکی در فضای آزاد متفاوت باشد.

$$\nabla\cdot\vect{E}=\frac{1}{\epsilon_0}(\rho+\rho_p)$$
$$\nabla\cdot(\epsilon_0\vect{E}+\vect{P})=\rho$$

- چگالی شار الکتریکی یا جابجایی الکتریکیِ $\vect{D}$ به صورت زیر تعریف می‌شود

::: {.definition}
$$\vect{D}=\epsilon_0\vect{E}+\vect{P}\qquad(\mathrm{C/m^2})$$
:::

- با استفاده از بردار $\vect{D}$ می‌توان رابطه بین میدان الکتریکی و توزیع‌های بار آزاد را در هر محیط بدون لزوم درگیری با بردار قطبی‌شدگی $\vect{P}$ یا چگالی‌های بار قطبی‌شدگی نوشت.

::: {.important}
$$\nabla\cdot\vect{D}=\rho\qquad(\mathrm{C/m^3})$$
:::

- فرم انتگرالی

$$\int_V\nabla\cdot\vect{D}\,dv=\int_V\rho\,dv$$

::: {.important title="شکل دیگر قانون گوس"}
$$\oint_S\vect{D}\cdot d\vect{s}=Q\qquad(\mathrm{C})$$
:::

- معادلات اصلی حاکم بر الکتریسیته ساکن در هر محیط

::: {.important}
$$\begin{cases}\nabla\cdot\vect{D}=\rho\\\nabla\times\vect{E}=0\end{cases}$$
:::

## ضریب دی‌الکتریک

- رابطه بین بردار قطبی شدگی و شدت میدان الکتریکی

$$\vect{P}=\epsilon_0\chi_e\vect{E}$$

- $\chi_e$: پذیرندگی الکتریکی

- رابطه بین شدت میدان الکتریکی و چگالی شار الکتریکی

::: {.important}
$$\begin{aligned}\vect{D}&=\epsilon_0(1+\chi_e)\vect{E}\\&=\epsilon_0\epsilon_r\vect{E}=\epsilon\vect{E}\qquad(\mathrm{C/m^2})\end{aligned}$$
:::

$$\epsilon_r=1+\chi_e=\frac{\epsilon}{\epsilon_0}$$

- $\epsilon_r$: یک ثابت بدون بعد به نام گذردهی نسبی یا ضریب دی‌الکتریک

- یک محیط دی‌الکتریک **خطی** است اگر $\epsilon_r$ مستقل از $\vect{E}$، **همگن** است اگر $\epsilon_r$ مستقل از مختصات فضایی و همه سو یکسان است اگر $\epsilon_r$ اسکالر باشد.
    - هر محیط خطی، همگن و همه سو یکسان را یک محیط ساده می‌نامند.
    - در محیط‌های غیر همه سو یکسان ضریب دی‌الکتریک به صورت ماتریس است. در چنین محیط‌هایی $\vect{D}$ و $\vect{E}$ لزوماً هم جهت نیستند.

::: {.example number="2-13"}
بار نقطه‌ای $+Q$ در مرکز یک پوسته کروی دی‌الکتریک به شعاع داخلی $R_i$ و شعاع خارجی $R_o$ قرار دارد. ثابت دی‌الکتریک پوسته $\epsilon_r$ است. $\vect{E}$، $V$، $\vect{D}$ و $\vect{P}$ را در کل فضا بدست آورید.

```{.figure #m02-ex13 caption=""}
```

::: {.solution}
$$\vect{E}=E_R\uvec{R}$$

- به ازای $R>R_o$

$$E_{R1}=\frac{Q}{4\pi\epsilon_0R^2}\qquad V_1=\frac{Q}{4\pi\epsilon_0R}$$
$$D_{R1}=\epsilon_0E_{R1}=\frac{Q}{4\pi R^2}\qquad P_{R1}=0$$

- به ازای $R_i<R<R_o$

$$D_{R2}=\frac{Q}{4\pi R^2}$$
$$E_{R2}=\frac{Q}{4\pi\epsilon_0\epsilon_rR^2}=\frac{Q}{4\pi\epsilon R^2}$$
$$P_{R2}=\left(1-\frac{1}{\epsilon_r}\right)\frac{Q}{4\pi R^2}$$
$$\begin{aligned}V_2&=-\int_{\infty}^{R_o}E_{R1}\,dR-\int_{R_o}^{R}E_{R2}\,dR\\&=V_1\Big|_{R=R_o}-\frac{Q}{4\pi\epsilon}\int_{R_o}^{R}\frac{1}{R^2}\,dR\\&=\frac{Q}{4\pi\epsilon_0}\left[\left(1-\frac{1}{\epsilon_r}\right)\frac{1}{R_o}+\frac{1}{\epsilon_rR}\right]\end{aligned}$$

- به ازای $R<R_i$

$$E_{R3}=\frac{Q}{4\pi\epsilon_0R^2}\qquad D_{R3}=\frac{Q}{4\pi R^2}\qquad P_{R3}=0$$
$$\begin{aligned}V_3&=V_2\Big|_{R=R_i}-\int_{R_i}^{R}E_{R3}\,dR\\&=\frac{Q}{4\pi\epsilon_0}\left[\left(1-\frac{1}{\epsilon_r}\right)\frac{1}{R_o}-\left(1-\frac{1}{\epsilon_r}\right)\frac{1}{R_i}+\frac{1}{R}\right]\end{aligned}$$

$$\begin{aligned}\rho_{ps}\Big|_{R=R_i}&=\vect{P}\cdot(-\uvec{R})\Big|_{R=R_i}=-P_{R2}\Big|_{R=R_i}\\&=-\left(1-\frac{1}{\epsilon_r}\right)\frac{Q}{4\pi R_i^2}\end{aligned}$$
$$\begin{aligned}\rho_{ps}\Big|_{R=R_o}&=\vect{P}\cdot\uvec{R}\Big|_{R=R_o}=P_{R2}\Big|_{R=R_o}\\&=\left(1-\frac{1}{\epsilon_r}\right)\frac{Q}{4\pi R_o^2}\end{aligned}$$
$$\begin{aligned}\rho_p&=-\nabla\cdot\vect{P}\\&=-\frac{1}{R^2}\frac{\partial}{\partial R}(R^2P_{R2})=0\end{aligned}$$
:::
:::

## مقاومت دی‌الکتریک

- میدان الکتریکی خارجی باعث جابجایی‌های کوچک در بارهای مقید شده و دوقطبی‌های الکتریکی را بوجود می‌آورد.
- حال اگر میدان الکتریکی قوی باشد، باعث جدایی کامل الکترون‌ها از مولکول‌ها، شتاب گرفتن آن‌ها و تصادم آن‌ها با ساختار شبکه‌ای مولکولی می‌شود.
- در این حالت ممکن است ماده هادی شود و جریان‌های بزرگی بوجود آید.
    - این پدیده را **شکست دی‌الکتریک** گویند.
- حداکثر شدت میدان الکتریکی که یک ماده دی‌الکتریک می‌تواند بدون شکست تحمل کند، **مقاومت دی‌الکتریک** ماده نامیده می‌شود.
    - به عنوان مثال مقاومت دی الکتریک هوا $3\,\mathrm{kV/mm}$ است.

::: {.example number="2-14"}
هنگامیکه یک کابل هم محور برای حمل توان الکتریکی استفاده می شود، شعاع هادی داخلی توسط جریان بار و ابعاد کلی توسط ولتاژ و ماده عایق مورد استفاده تعیین می شوند. فرض کنید که شعاع هادی داخلی $0.4\,\mathrm{cm}$ و دو لایه شامل لاستیک با گذردهی نسبی $\epsilon_{rr}=3.2$ و پلی استایرن با گذردهی الکتریکی $\epsilon_{rp}=2.6$ به عنوان ماده عایق استفاده شده باشند. این کابل را به گونه ای طراحی کنید که قابلیت کار در ولتاژ $20\,\mathrm{kV}$ را داشته باشد. به منظور اجتناب از پدیده شکست ناشی از شرایط خارجی غیر عادی، حداکثر شدت میدان الکتریکی در مواد عایق نباید از ۲۵٪ مقاومت عایق ها تجاوز کند. (مقاومت دی الکتریک لاستیک $25\times10^6\,\mathrm{V/m}$ و مقاومت دی الکتریک پلی استیرین $20\times10^6\,\mathrm{V/m}$ است)

```{.figure #m02-ex14 caption=""}
```

::: {.solution}
- هدف تعیین ترتیب لایه های عایقی و مقادیر $r_o$ و $r_m$ است.
- با فرض اینکه چگالی بار آزاد روی سطح هادی داخلی $\rho_s$ باشد، با استفاده از قانون گوس داریم

$$D_r2\pi rL=\rho_s2\pi r_iL\qquad D_r=\rho_s\frac{r_i}{r}\qquad E_r=\frac{\rho_s}{\epsilon_0\epsilon_{r1,2}}\frac{r_i}{r}$$
$$\text{Rubber}\qquad \max\{E_{rr}\}=0.25\times25\times10^6\,\mathrm{V/m}=\frac{\rho_s}{\epsilon_0\epsilon_{rr}}\frac{r_i}{r_{r\min}}\qquad r_{r\min}=r_i\ \text{or}\ r_m$$
$$\text{Polystyrene}\qquad \max\{E_{rp}\}=0.25\times20\times10^6\,\mathrm{V/m}=\frac{\rho_s}{\epsilon_0\epsilon_{rp}}\frac{r_i}{r_{p\min}}\qquad r_{p\min}=r_i\ \text{or}\ r_m$$
$$\frac{25}{20}=\frac{\epsilon_{rp}}{\epsilon_{rr}}\times\frac{r_{p\min}}{r_{r\min}}\qquad r_{p\min}>r_{r\min}\Rightarrow\begin{cases}r_{r\min}=r_i\\r_{p\min}=r_m\end{cases}$$
$$\frac{25}{20}=\frac{2.6}{3.2}\times\frac{r_m}{0.4}\Rightarrow r_m=0.616\,\mathrm{cm}$$
$$\begin{aligned}-\int_{r_o}^{r_m}E_{rp}\,dr-\int_{r_m}^{r_i}E_{rr}\,dr&=\frac{\rho_sr_i}{\epsilon_0}\left(\frac{1}{\epsilon_{rp}}\ln\left(\frac{r_o}{r_m}\right)+\frac{1}{\epsilon_{rr}}\ln\left(\frac{r_m}{r_i}\right)\right)\\&=20000\,\mathrm{V}\end{aligned}$$
$$\frac{\rho_sr_i}{\epsilon_0}=0.25\times25\times10^6\epsilon_{rr}r_i=8\times10^4$$
$$\Longrightarrow\qquad r_o=0.832\,\mathrm{cm}$$
:::
:::

## شرایط مرزی میدان‌های الکتریکی ساکن

```{.figure #m02-map-boundary caption=""}
```

```{.figure #m02-boundary caption=""}
```

- مؤلفه مماسی:

$$\oint_{abcda}\vect{E}\cdot\dif\vect{\ell}=\vect{E}_1\cdot\Delta\vect{w}+\vect{E}_2\cdot(-\Delta\vect{w})=E_{1t}\Delta w-E_{2t}\Delta w=0$$

::: {.important}
$$E_{1t}=E_{2t}\qquad\qquad \frac{D_{1t}}{\epsilon_1}=\frac{D_{2t}}{\epsilon_2}$$
:::

- مؤلفه عمودی:

$$\begin{aligned}\oint_S\vect{D}\cdot d\vect{s}&=(\vect{D}_1\cdot\uvec{n2}+\vect{D}_2\cdot\uvec{n1})\Delta S\\&=\uvec{n2}\cdot(\vect{D}_1-\vect{D}_2)\Delta S\\&=\rho_s\Delta S\end{aligned}$$

::: {.important}
$$\uvec{n2}\cdot(\vect{D}_1-\vect{D}_2)=\rho_s\qquad\qquad \uvec{n2}\cdot(\epsilon_1\vect{E}_1-\epsilon_2\vect{E}_2)=\rho_s$$
:::

::: {.example number="2-15"}
دو محیط دی الکتریک با گذردهی الکتریکی $\epsilon_1$ و $\epsilon_2$ توسط یک مرز بدون بار مطابق شکل زیر از هم جدا شده اند. شدت میدان الکتریکی در محیط ۱ و در نقطه $P_1$ دارای اندازه $E_1$ بوده و زاویه $\alpha_1$ با جهت عمود می سازد. اندازه و جهت شدت میدان الکتریکی در نقطه $P_2$ در ناحیه ۲ را تعیین کنید.

```{.figure #m02-ex15 caption=""}
```

::: {.solution}
$$E_{1t}=E_{2t}\quad\Longrightarrow\quad E_2\sin\alpha_2=E_1\sin\alpha_1$$
$$\uvec{n2}\cdot(\epsilon_1\vect{E}_1-\epsilon_2\vect{E}_2)=\epsilon_1E_{1n}-\epsilon_2E_{2n}=0\quad\Longrightarrow\quad\epsilon_2E_2\cos\alpha_2=\epsilon_1E_1\cos\alpha_1$$

::: {.important}
$$\frac{\tan\alpha_2}{\tan\alpha_1}=\frac{\epsilon_2}{\epsilon_1}$$
:::

$$\begin{aligned}E_2&=\sqrt{E_{2t}^2+E_{2n}^2}=\sqrt{(E_2\sin\alpha_2)^2+(E_2\cos\alpha_2)^2}\\&=\left[(E_1\sin\alpha_1)^2+\left(\frac{\epsilon_1}{\epsilon_2}E_1\cos\alpha_1\right)^2\right]^{1/2}\end{aligned}$$

::: {.important}
$$E_2=E_1\left[\sin^2\alpha_1+\left(\frac{\epsilon_1}{\epsilon_2}\cos\alpha_1\right)^2\right]^{1/2}$$
:::
:::
:::

## ظرفیت و خازن‌ها

```{.figure #m02-map-cap caption=""}
```

- خازن چه المانی است و مفهوم ظرفیت چیست؟
- نحوه محاسبه ظرفیت خازنی ساختارهای مختلف به چه صورتی است؟
- چگونه می توان انرژی الکتریکی ذخیره شده در مجموعه ای بار یا کار لازم برای گرد آوردن مجموعه ای بار در کنار هم را بدست آورد؟
- چگونه می توان انرژی الکتریکی ذخیره شده در ساختارهای خازنی را محاسبه کرد؟

- فرض کنیم که بار $Q$ روی یک هادی دلخواه قرار داده شود. این بار روی سطح هادی توزیع شده و چگالی بار $\rho_s$ را تشکیل می‌دهد.
- افزایش کل بار با ضریب $k$ باعث افزایش چگالی بار $\rho_s$ با ضریب $k$ شده و در نتیجه پتانسیل ناشی از این بار نیز با ضریب $k$ افزایش می‌یابد.
    - بنابراین نسبت $Q$ به $V$ ثابت می‌ماند

::: {.important}
$$Q=CV$$
:::

- ثابت تناسب $(C)$ **ظرفیت جسم هادی مجزا** نامیده شده و عبارتست از مقدار بار الکتریکی که باید به جسم اضافه شود تا پتانسیل الکتریکی آن به اندازه واحد افزایش یابد.
    - واحد آن نیز کولمب بر ولت یا فاراد $(\mathrm{F})$ است.

- دو هادی که توسط فضای آزاد یا محیط دی‌الکتریک از هم جدا شده‌اند را خازن گویند.

```{.figure #m02-capacitor caption=""}
```

- ظرفیت یک خازن به صورت زیر تعریف می‌شود

::: {.definition}
$$C=\frac{Q}{V_{12}}\qquad(\mathrm{F})$$
:::

- ظرفیت یک خازن به شکل هندسی و گذردهی محیط بین دو هادی بستگی دارد.
- نحوه محاسبه ظرفیت خازن
    - انتخاب دستگاه مختصات مناسب
    - قرار دادن بارهای $+Q$ و $-Q$ روی هادی‌ها
    - یافتن $\vect{E}$ از روی $Q$
    - محاسبه اختلاف پتانسیل بین دو هادی از رابطه زیر از بار $-Q$ تا بار $+Q$
$$V=-\int_{P_{-Q}}^{P_{+Q}}\vect{E}\cdot\dif\vect{\ell}$$
    - یافتن ظرفیت خازن از رابطه $Q/V$

::: {.example number="2-16"}
یک خازن صفحه موازی شامل دو صفحه هادی موازی به مساحت $S$ و فاصله $d$ است. فضای بین صفحات توسط یک دی الکتریک با ضریب گذردهی الکتریکی ثابت $\epsilon$ پر شده است. ظرفیت این خازن را بدست آورید.

```{.figure #m02-ex16 caption=""}
```

::: {.solution}
- استفاده از دستگاه مختصات کارتزین
- قرار دادن بارهای $+Q$ و $-Q$ روی صفحات $\ELto$ $\rho_s=\dfrac{Q}{S}$
- محاسبه شدت میدان الکتریکی با استفاده از قانون گوس در فضای بین دو صفحه هادی با صرف نظر کردن از میدان های حاشیه ای

$$\vect{E}=-\uvec{y}\frac{\rho_s}{\epsilon}=-\uvec{y}\frac{Q}{\epsilon S}$$

- محاسبه اختلاف پتانسیل بین صفحات هادی برحسب $Q$

$$V_{12}=-\int_{y=0}^{y=d}\vect{E}\cdot\dif\vect{\ell}=-\int_0^d\left(-\uvec{y}\frac{Q}{\epsilon S}\right)\cdot(\uvec{y}\,dy)=\frac{Q}{\epsilon S}d$$

- تعیین ظرفیت خازن

$$C=\frac{Q}{V_{12}}=\epsilon\frac{S}{d}$$
:::
:::

::: {.example number="2-17"}
یک خازن استوانه ای شامل یک هادی داخلی به شعاع $a$ و هادی خارجی به شعاع $b$ است. فضای بین دو هادی توسط یک دی الکتریک با ضریب گذردهی الکتریکی ثابت $\epsilon$ پر شده و طول خازن برابر با $L$ است. ظرفیت این خازن را بدست آورید.

```{.figure #m02-ex17 caption=""}
```

::: {.solution}
- استفاده از دستگاه مختصات استوانه ای
- قرار دادن بارهای $+Q$ و $-Q$ به ترتیب روی هادی های داخلی و خارجی
- محاسبه شدت میدان الکتریکی با استفاده از قانون گوس در فضای بین دو هادی

$$\vect{E}=\uvec{r}E_r=\uvec{r}\frac{Q}{2\pi\epsilon Lr}$$

- محاسبه اختلاف پتانسیل بین صفحات هادی برحسب $Q$

$$\begin{aligned}V_{ab}&=-\int_{r=b}^{r=a}\vect{E}\cdot\dif\vect{\ell}=-\int_b^a\left(\uvec{r}\frac{Q}{2\pi\epsilon Lr}\right)\cdot(\uvec{r}\,dr)\\&=\frac{Q}{2\pi\epsilon L}\ln\left(\frac ba\right)\end{aligned}$$

- تعیین ظرفیت خازن

$$C=\frac{Q}{V_{ab}}=\frac{2\pi\epsilon L}{\ln\left(\dfrac ba\right)}$$
:::
:::

::: {.example number="2-18"}
یک خازن کروی شامل یک کره هادی داخلی به شعاع $R_i$ و یک کره هادی خارجی به شعاع $R_o$ است. فضای بین دو هادی توسط یک دی الکتریک با ضریب گذردهی الکتریکی ثابت $\epsilon$ پر شده است. ظرفیت این خازن را تعیین کنید.

```{.figure #m02-ex18 caption=""}
```

::: {.solution}
- استفاده از دستگاه مختصات کروی
- قرار دادن بارهای $+Q$ و $-Q$ به ترتیب روی هادی های داخلی و خارجی
- محاسبه شدت میدان الکتریکی با استفاده از قانون گوس در فضای بین دو هادی

$$\vect{E}=\uvec{R}E_R=\uvec{R}\frac{Q}{4\pi\epsilon R^2}$$

- محاسبه اختلاف پتانسیل بین صفحات هادی برحسب $Q$

$$V=-\int_{R_o}^{R_i}\vect{E}\cdot(\uvec{R}\,dR)=-\int_{R_o}^{R_i}\frac{Q}{4\pi\epsilon R^2}\,dR=\frac{Q}{4\pi\epsilon}\left(\frac{1}{R_i}-\frac{1}{R_o}\right)$$

- تعیین ظرفیت خازن

$$C=\frac QV=\frac{4\pi\epsilon}{\dfrac{1}{R_i}-\dfrac{1}{R_o}}$$
:::
:::

- **اتصال موازی خازن ها**

```{.figure #m02-parallel caption=""}
```

$$\begin{aligned}Q&=Q_1+Q_2+\cdots+Q_n\\&=C_1V+C_2V+\cdots+C_nV=C_{\parallel}V\end{aligned}$$

::: {.important}
$$C_{\parallel}=C_1+C_2+\cdots+C_n$$
:::

- **اتصال سری خازن ها**

```{.figure #m02-series caption=""}
```

$$V=\frac{Q}{C_{sr}}=\frac{Q}{C_1}+\frac{Q}{C_2}+\cdots+\frac{Q}{C_n}$$

::: {.important}
$$\frac{1}{C_{sr}}=\frac{1}{C_1}+\frac{1}{C_2}+\cdots+\frac{1}{C_n}$$
:::

::: {.example number="2-19"}
یک خازن استوانه ای به طول $L$ از سطوح هادی استوانه ای هم محور به شعاع های $r_i$ و $r_o$ تشکیل شده است. دو ماده دی الکتریک با ضرایب گذردهی الکتریکی $\epsilon_1$ و $\epsilon_2$ فضای بین هادی ها را مطابق شکل زیر پر کرده اند. ظرفیت این خازن را تعیین کنید.

```{.figure #m02-ex19 caption=""}
```

::: {.solution}
- **روش اول**
    - ظرفیت یک خازن استوانه ای $\ELto$ $C=\dfrac{2\pi\epsilon L}{\ln\left(\dfrac{r_o}{r_i}\right)}$
    - از آنجا که هر ماده دی الکتریک نیمی از فضا را پر می کند، ظرفیت هر نیمه برابر است با

$$C_1=\frac{\pi\epsilon_1L}{\ln\left(\dfrac{r_o}{r_i}\right)}\qquad\qquad C_2=\frac{\pi\epsilon_2L}{\ln\left(\dfrac{r_o}{r_i}\right)}$$

- از آنجا که دو خازن $C_1$ و $C_2$ موازی هستند، ظرفیت کل برابر است با

$$C=C_1+C_2=\frac{2\pi L}{\ln\left(\dfrac{r_o}{r_i}\right)}\left(\frac{\epsilon_1+\epsilon_2}{2}\right)$$

- **روش دوم**
    - استفاده از دستگاه مختصات استوانه ای
    - قرار دادن بارهای $+Q$ و $-Q$ به ترتیب روی هادی های داخلی و خارجی
    - محاسبه شدت میدان الکتریکی با استفاده از قانون گوس در فضای بین دو هادی

```{.figure #m02-ex19-gauss caption=""}
```

$$\left.\begin{aligned}E_{r1}&=\frac{Q_1}{\pi r\epsilon_1L}\\E_{r2}&=\frac{Q_2}{\pi r\epsilon_2L}\end{aligned}\right\}\ \overset{E_{r1}=E_{r2}}{\Longrightarrow}\ \left.\begin{aligned}\frac{Q_1}{\epsilon_1}&=\frac{Q_2}{\epsilon_2}\\Q_1+Q_2&=Q\end{aligned}\right\}\ \begin{cases}Q_1=\dfrac{Q\epsilon_1}{\epsilon_1+\epsilon_2}\\[3mm]Q_2=\dfrac{Q\epsilon_2}{\epsilon_1+\epsilon_2}\end{cases}$$

- محاسبه اختلاف پتانسیل بین صفحات هادی برحسب $Q$

$$V=-\int_{r_o}^{r_i}\frac{Q_1}{\pi r\epsilon_1L}\,dr=-\int_{r_o}^{r_i}\frac{Q}{\pi rL(\epsilon_1+\epsilon_2)}\,dr=\frac{Q}{\pi L(\epsilon_1+\epsilon_2)}\ln\left(\frac{r_o}{r_i}\right)$$

- تعیین ظرفیت خازن

$$C=\frac{2\pi L}{\ln\left(\dfrac{r_o}{r_i}\right)}\left(\frac{\epsilon_1+\epsilon_2}{2}\right)$$
:::
:::

::: {.example number="2-20"}
خازنی از دو پوسته کروی هادی هم مرکز به شعاع های $R_i$ و $R_o$ تشکیل شده است. فضای بین این دو پوسته با یک دی الکتریک با ضریب گذردهی نسبی $\epsilon_r$ از $R_i$ تا $b$ و یک دی الکتریک با ضریب گذردهی نسبی $2\epsilon_r$ از $b$ تا $R_o$ پر شده است. ظرفیت این خازن را تعیین کنید.

```{.figure #m02-ex20 caption=""}
```

::: {.solution}
- **روش اول**
    - ظرفیت یک خازن کروی $\ELto$ $C=\dfrac QV=\dfrac{4\pi\epsilon}{\dfrac{1}{R_i}-\dfrac{1}{R_o}}$
    - این خازن را می توان معادل دو خازن سری به صورت زیر در نظر گرفت

$$C_1=\frac{4\pi\epsilon_0\epsilon_r}{\dfrac{1}{R_i}-\dfrac1b}\qquad\qquad C_2=\frac{4\pi\epsilon_0(2\epsilon_r)}{\dfrac1b-\dfrac{1}{R_o}}$$

- بنابراین ظرفیت کل برابر است با

$$C=\frac{1}{1/C_1+1/C_2}=\frac{4\pi\epsilon_0\epsilon_r}{\dfrac{1}{R_i}-\dfrac{1}{2b}-\dfrac{1}{2R_o}}$$

- **روش دوم**
    - استفاده از دستگاه مختصات کروی
    - قرار دادن بارهای $+Q$ و $-Q$ به ترتیب روی هادی های داخلی و خارجی
    - محاسبه شدت میدان الکتریکی با استفاده از قانون گوس در فضای بین دو هادی

$$E_{R1}=\frac{Q}{4\pi\epsilon_0\epsilon_rR^2}\qquad\qquad E_{R2}=\frac{Q}{4\pi\epsilon_0(2\epsilon_r)R^2}$$

- محاسبه اختلاف پتانسیل بین صفحات هادی برحسب $Q$

$$V=-\int_{R_o}^{b}\frac{Q}{4\pi\epsilon_0(2\epsilon_r)R^2}\,dR-\int_{b}^{R_i}\frac{Q}{4\pi\epsilon_0\epsilon_rR^2}\,dR=\frac{Q}{4\pi\epsilon_0\epsilon_r}\left(\frac{1}{R_i}-\frac{1}{2b}-\frac{1}{2R_o}\right)$$

- تعیین ظرفیت خازن

$$C=\frac{4\pi\epsilon_0\epsilon_r}{\dfrac{1}{R_i}-\dfrac{1}{2b}-\dfrac{1}{2R_o}}$$
:::
:::

## انرژی الکتریکی ساکن

```{.figure #m02-map-energy caption=""}
```

- پتانسیل الکتریکیِ یک نقطه در حضور میدان الکتریکی، برابر با کار لازم برای آوردن یک بار مثبت واحد از بی‌نهایت (با پتانسیل مرجع صفر) به آن نقطه است.
- برای آوردن بار $Q_2$ از بی‌نهایت به فاصله $R_{12}$ از بار $Q_1$ مقدار کار لازم برابر است با

```{.figure #m02-energy-two caption=""}
```

$$W_2=Q_2V_2=Q_2\frac{Q_1}{4\pi\epsilon_0R_{12}}$$

- $V_2$: پتانسیل در محل بار $Q_2$

$$W_2=Q_1\frac{Q_2}{4\pi\epsilon_0R_{12}}=Q_1V_1$$
$$W_2=\tfrac12(Q_1V_1+Q_2V_2)$$

- این کار در مجموعه دو بار به صورت انرژی پتانسیل ذخیره می‌شود.

- حال فرض کنید که بار دیگر $Q_3$ از بی‌نهایت به نقطه‌ای به فاصله $R_{13}$ از بار $Q_1$ و $R_{23}$ از بار $Q_2$ آورده شود، کار اضافی مورد نیاز برابر خواهد بود با

```{.figure #m02-energy-three caption=""}
```

$$\Delta W=Q_3V_3=Q_3\left(\frac{Q_1}{4\pi\epsilon_0R_{13}}+\frac{Q_2}{4\pi\epsilon_0R_{23}}\right)$$

- $V_3$: پتانسیل در محل بار $Q_3$
- به این ترتیب انرژی پتانسیل ذخیره شده در مجموعه سه بار برابر است با

$$W_3=W_2+\Delta W=\frac{1}{4\pi\epsilon_0}\left(\frac{Q_1Q_2}{R_{12}}+\frac{Q_1Q_3}{R_{13}}+\frac{Q_2Q_3}{R_{23}}\right)$$
$$\begin{aligned}W_3=\frac12\bigg[&Q_1\left(\frac{Q_2}{4\pi\epsilon_0R_{12}}+\frac{Q_3}{4\pi\epsilon_0R_{13}}\right)+Q_2\left(\frac{Q_1}{4\pi\epsilon_0R_{12}}+\frac{Q_3}{4\pi\epsilon_0R_{23}}\right)\\&+Q_3\left(\frac{Q_1}{4\pi\epsilon_0R_{13}}+\frac{Q_2}{4\pi\epsilon_0R_{23}}\right)\bigg]=\tfrac12(Q_1V_1+Q_2V_2+Q_3V_3)\end{aligned}$$

- به این ترتیب انرژی پتانسیل $N$ بار نقطه‌ای گسسته ساکن برابر است با

::: {.important}
$$W_e=\frac12\sum_{k=1}^{N}Q_kV_k\qquad(\mathrm{J})$$
:::

- که $V_k$ پتانسیل الکتریکی در نقطه $Q_k$ ناشی از بارهای دیگر است.
- واحد $\mathrm{SI}$ انرژی، ژول است که واحد بزرگی است. در اینجا از واحد دیگری به نام الکترون ولت $(\mathrm{eV})$ استفاده می‌شود.
    - ۱ الکترون ولت، انرژی یا کار لازم برای حرکت دادن یک الکترون بر علیه اختلاف پتانسیل یک ولتی است.

$$1\,(\mathrm{eV})=(1.60\times10^{-19})\times1=1.60\times10^{-19}\qquad(\mathrm{J})$$

- در یک توزیع پیوسته بار با چگالی $\rho$ انرژی ذخیره شده برابر است با

::: {.important}
$$W_e=\tfrac12\int_{V'}\rho V\,dv\qquad(\mathrm{J})$$
:::

- که $V$ پتانسیل در نقطه‌ای است که چگالی بار حجمی در آن $\rho$ است و $V'$ حجم ناحیه‌ای است که $\rho$ در آن قرار دارد.

::: {.example number="2-21"}
انرژی مورد نیاز برای ایجاد یک کره یکنواخت باردار به شعاع $b$ و چگالی حجمی $\rho$ را بدست آورید.

::: {.solution}
$$W_e=\frac\rho2\int_{V'}V\,dv=\frac\rho2\int_0^bV\,4\pi R^2\,dR$$
$$\vect{E}_{R1}=\uvec{R}\frac{Q}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho b^3}{3\epsilon_0R^2},\qquad R\geq b$$
$$\vect{E}_{R2}=\uvec{R}\frac{Q_R}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho R}{3\epsilon_0},\qquad 0<R\leq b$$
$$\begin{aligned}V&=-\int_{\infty}^{R}\vect{E}\cdot d\vect{R}=-\left[\int_{\infty}^{b}E_{R1}\,dR+\int_b^RE_{R2}\,dR\right]\\&=-\left[\int_{\infty}^{b}\frac{\rho b^3}{3\epsilon_0R^2}\,dR+\int_b^R\frac{\rho R}{3\epsilon_0}\,dR\right]\\&=\frac{\rho}{3\epsilon_0}\left(b^2+\frac{b^2}{2}-\frac{R^2}{2}\right)=\frac{\rho}{3\epsilon_0}\left(\frac32b^2-\frac{R^2}{2}\right)\end{aligned}$$
$$W_e=\frac\rho2\int_0^b\frac{\rho}{3\epsilon_0}\left(\frac32b^2-\frac{R^2}{2}\right)4\pi R^2\,dR=\frac{4\pi\rho^2b^5}{15\epsilon_0}$$
:::
:::

- پیش از این انرژی الکتریکی ساکن یک توزیع بار را برحسب چگالی بار و پتانسیل بدست آوردیم.
- گاهی بهتر است این انرژی برحسب کمیات میدان بیان شود.
- می توان نشان داد

::: {.important}
$$W_e=\tfrac12\int_{V'}\vect{D}\cdot\vect{E}\,dv\qquad(\mathrm{J})$$
$$W_e=\tfrac12\int_{V'}\epsilon E^2\,dv\qquad(\mathrm{J})$$
$$W_e=\tfrac12\int_{V'}\frac{D^2}{\epsilon}\,dv\qquad(\mathrm{J})$$
:::

- $V'$: کل فضا

::: {.example number="2-22"}
مثال \ELnumc{2-21} را با استفاده از رابطه انرژی برحسب کمیت های میدان حل کنید.

::: {.solution}
$$\vect{E}_{R1}=\uvec{R}\frac{Q}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho b^3}{3\epsilon_0R^2},\qquad R\geq b$$
$$\vect{E}_{R2}=\uvec{R}\frac{Q_R}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho R}{3\epsilon_0},\qquad 0<R\leq b$$
$$\begin{aligned}W_e=\frac12\epsilon_0\int_{V'}\abs{\vect{E}}^2\,dv&=\frac12\epsilon_0\int_0^b\left(\frac{\rho R}{3\epsilon_0}\right)^24\pi R^2\,dR\\&\quad+\frac12\epsilon_0\int_b^{\infty}\left(\frac{\rho b^3}{3\epsilon_0R^2}\right)^24\pi R^2\,dR=\frac{4\pi\rho^2b^5}{15\epsilon_0}\end{aligned}$$
:::
:::

::: {.example number="2-23"}
در شکل زیر یک خازن صفحه موازی به مساحت $S$ و فاصله بین صفحات $d$ توسط ولتاژ $V$ شارژ شده است. ضریب گذردهی الکتریکی عایق $\epsilon$ است. انرژی ذخیره شده را بدست آورید.

```{.figure #m02-ex23 caption=""}
```

::: {.solution}
$$E=\frac Vd$$
$$W_e=\frac12\int_{V'}\epsilon\left(\frac Vd\right)^2dv=\frac12\epsilon\left(\frac Vd\right)^2(Sd)=\frac12\left(\epsilon\frac Sd\right)V^2$$

::: {.important}
$$W_e=\tfrac12CV^2\quad(\mathrm{J})\qquad\qquad W_e=\tfrac12QV\quad(\mathrm{J})\qquad\qquad W_e=\frac{Q^2}{2C}\quad(\mathrm{J})$$
:::

::: {.remark}
ثابت می‌شود که معادلات فوق برای هر خازن متشکل از دو هادی برقرار است.
:::
:::
:::

::: {.example number="2-24"}
با استفاده از رابطه انرژی، ظرفیت یک خازن استوانه ای به طول $L$ شامل هادی داخلی به شعاع $a$ و هادی خارجی به شعاع $b$ و ضریب گذردهی الکتریکی $\epsilon$ را بدست آورید.

::: {.solution}
$$\vect{E}=\uvec{r}E_r=\uvec{r}\frac{Q}{2\pi\epsilon Lr},\qquad a<r<b$$
$$\begin{aligned}W_e&=\frac12\int_a^b\epsilon\left(\frac{Q}{2\pi\epsilon Lr}\right)^2(L2\pi r\,dr)\\&=\frac{Q^2}{4\pi\epsilon L}\int_a^b\frac{dr}{r}=\frac{Q^2}{4\pi\epsilon L}\ln\frac ba\end{aligned}$$
$$\frac{Q^2}{2C}=\frac{Q^2}{4\pi\epsilon L}\ln\frac ba\qquad\Longrightarrow\qquad C=\frac{2\pi\epsilon L}{\ln\dfrac ba}$$
:::
:::

```{.figure #m02-map-end caption=""}
```
