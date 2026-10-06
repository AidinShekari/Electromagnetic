# Review notes

Places where the typeset notes differ from the instructor's slides, or where they add a caveat.
The slides remain the source of truth. Each entry names the slide (file and page of
`source/Ch1_N.pdf`), what the slide shows, what the notes show, and why.

## Corrections (unambiguous transcription or typesetting slips only)

| Where | Slide shows | Notes show | Why |
|---|---|---|---|
| Ch1_3 p. 12 (spherical coordinates) | "representation of an arbitrary vector **A** in *cylindrical* coordinates" above $\mathbf A=\mathbf a_RA_R+\mathbf a_\theta A_\theta+\mathbf a_\phi A_\phi$ | "… in *spherical* coordinates" | the formula and the slide are about spherical coordinates (the cylindrical slide, Ch1_3 p. 3, has its own) |
| Ch1_3 pp. 7, 8, 18, 19 | a stray accent: $\mathbf a_z'A_z$ | $\mathbf a_zA_z$ | a mark left over in the picture of the formula; the same expression elsewhere has no prime |
| Ch1_1 p. 7 | $A=2a_x+3a_y+a_z$, … with non-bold unit vectors | bold $\mathbf a_x$, … | the slides write unit vectors in bold everywhere else (e.g. Ch1_2 p. 16) |
| throughout | $\mathbf{A.B}$ (a full stop for the dot product) in some slides | $\mathbf A\cdot\mathbf B$ | the same product is written with a centred dot elsewhere |
| throughout | both $\phi$ and $\varphi$ for the azimuth | $\phi$ | one symbol for one quantity |
| Ch2_3 pp. 4–9 (examples 2-4 to 2-7) | the titles read «مثال ۳-۴», «۳-۵», «۳-۶», «۳-۷» | 2-4, 2-5, 2-6, 2-7 | chapter 2: the examples before are 2-1 to 2-3 (Ch2_2) and the ones after are 2-8 to 2-12 (Ch2_4, Ch2_5); the first digit is a slip |
| Ch2_1 p. 12 | the annotation reads «شدن میدان الکتریکی روی سطح کره» | «شدت میدان الکتریکی …» | a typing slip (شدن for شدت, "intensity") |
| Ch2_1 p. 12 | $E_R(4\pi R^2):=\dfrac{q}{\epsilon_0}$ | $=$ | an equation, not a definition; the lines above and below use $=$ |
| Ch2_4 p. 13 (example 2-10) | $V=\dfrac{1}{4\pi\varepsilon_0}\int_{S'}\dfrac{\rho_\ell\,d\ell'}{\lvert\mathbf R-\mathbf R'\rvert}$ | $\int_{L'}$ | a line charge: the general formula on Ch2_4 p. 8 integrates over $L'$ |
| Ch2_7 p. 19 (example 2-20) | $\int\frac{Q}{4\pi\varepsilon_0(2\varepsilon_r)R^2}\,dr$ (both integrals) | $dR$ | the variable of integration is $R$ (the limits are $R_o$, $b$, $R_i$) |
| Ch2_7 pp. 8, 10, 12, 16, 19 | «محاسبه اختلاف پتانسیل بین صفحات هادی» also for the cylindrical and spherical capacitors | kept in Persian; the English edition says "between the conductors" for those | the wording of the parallel-plate case carried over |
| Ch5_3 p. 12 (example 5-8) | $\mathbf J_m=\mathbf M\times\mathbf a_n=\mathbf a_\phi M_0$ for the side wall | $\mathbf J_{ms}$ | the line is the surface current density, as the text above it says and as $\mathbf J_{ms}$ is used on p. 13 |
| Ch5_4 p. 13 (example 5-9, part c) | $\mu_0(2\pi r_o-\ell_a)+\mu\ell_a$ in the denominator of $\mathbf H_g$ | $\ell_g$ | the air gap is $\ell_g$ everywhere else (parts a and b, Ch5_5 p. 2) |
| Ch5_6 p. 7 | $L=\Lambda/l$ | $L=\Lambda/I$ | the inductance is the flux linkage per unit current (the same slide assumes the current $I$; Ch5_6 p. 5) |
| Ch5_7 p. 11 (example 5-15) | $L'=\mu_0n^2I^2$ (H/m) | $L'=\mu_0n^2S$ | follows from $\tfrac12\mu_0n^2I^2S=\tfrac12LI^2$ on the same line, and agrees with example 5-12 |
| Ch5_8 p. 8 | $\mathbf T=\mathbf m\times\mathbf B_{11}=\mathbf m\times(\mathbf B_{11}+\mathbf B_\perp)$ | $\mathbf B_\parallel$ | the subscript is the parallel sign $\parallel$ used everywhere else on the slide |
| Ch6 p. 10 (example 6-1) | $v=-N\,d\varphi/dt$ | $d\Phi/dt$ | the flux is $\Phi$ on the line above |

## Presentation (no change to the content)

| Where | Note |
|---|---|
| example numbers | kept as on the slides (مثال ۱-۱ … ۱-۱۸, Example 1-1 … 1-18); other blocks are not numbered because the slides do not number them |
| figure captions | only figures that carry text on the slide have a caption; the others are neither captioned nor numbered |
| slide titles "?" (Ch1_1 p. 7, Ch1_2 p. 13) | the questions are kept as a list, without the "?" heading |
| repeated outline slides (Ch1_1 p. 6, Ch1_2 p. 12, Ch1_4 p. 2, Ch1_5 p. 15) | each is kept where it occurs, with the same highlighted group |
| Ch1_2 p. 7, right-hand rule | the drawing of a hand is shown as a turning arrow from **A** to **B** about $\mathbf a_n$ |
| Ch1_5 pp. 3, 5, 10, 14 | the computer-generated plots (a coloured scalar field with its gradient, a rendered hill with contours, two field screenshots) are reproduced from the slides as images; every other figure is redrawn in TikZ |
| Ch1_1 p. 2, course outline | the slide's root box reads "الکترومغناطیس مهندسی" (Engineering Electromagnetics) and is kept so; the title of the book is "الکترومغناطیس" as specified for the collection |
| Persian edition, compound numbers | written in the order of the slides: the groups run right to left (example 1-18 is printed ۱۸-۱, section 1.2 is ۲.۱) |
| Ch2_4 p. 11 (example 2-8) | the field lines and equipotentials of the dipole are computed from the two charges ($\pm q$ at $z=\pm d/2$) by `tools/genfigs.py`; they follow the slide's sketch |
| Ch2_5 p. 9 (example 2-12) | the graphs of $E_R$ and $V$ are drawn with $R_i=1$, $R_o=1.6$ and $Q/4\pi\epsilon_0=1$ to show the shapes; the slide gives no values |
| Ch2 figures with a hand-drawn molecule picture (Ch2_5 p. 10) | redrawn in TikZ with the same elements: the atom in the field, the equivalent dipole, the polarized slab with its surface charges |
| Ch3_2 p. 7 (method of images) | the field lines of $Q$ and its image $-Q$ are computed from the two charges by `tools/genfigs.py`; they follow the slide's sketch |
| Ch3_3 (table of the solutions of $X''+k_x^2X=0$) | the table is set left to right in both editions, as on the slide |
| Ch5_3 p. 6 (electric and magnetic dipoles) | the field lines are computed by `tools/genfigs.py`: the electric dipole from the two charges, the magnetic dipole from a small current loop; they follow the slide's sketch |
| Ch5_3 p. 10 (magnetization) | the side-by-side comparison of $\mathbf M$ and $\mathbf P$ is written as pairs of formulas; the hand-drawn dielectric is redrawn as a slab of dipoles |
| Ch5_4 p. 8 (hysteresis loop) | the $B$–$H$ curves are model functions that show the shape; the slide gives no values |
| Ch5_4 pp. 11–12, Ch5_5 p. 2 (toroid with an air gap) | the photograph-like core is redrawn in TikZ seen from above, with the same labels ($r_0$, $\ell_g$, $I_0$, leakage flux, the surface $S$) |
| Ch5_6 p. 9 (example 5-11) | the perspective drawing of the toroidal coil is shown by its cross-section with all the dimensions of the slide ($a$, $b$, $h$, $r$, $dr$) |
| Ch5_6 p. 4, Ch5_7 p. 4 | the flux is written $\Phi$ throughout (the slides use $\varphi$ on some lines) |
| Ch5_8 p. 7 | the two explanations printed under the drawings are given as text after the figure |

## Statements kept as written but worth a second look

| Where | Remark |
|---|---|
| Ch1_4 p. 9 | Ampère's circuital law is written $\mu_0I=-\oint_C\mathbf B\cdot d\boldsymbol\ell$. The usual form has no minus sign. It is kept as on the slide. |
| Ch1_5 pp. 17, 19 | The theorems are quoted with $\mathbf A$ while the examples use the field $\mathbf F$. |
| Ch1_5 p. 6 (example 1-14) | The point $(1,1,0)$ is given, but the result $\mathbf E=-\mathbf a_zE_0$ does not depend on it. |
| Ch1_2 p. 13 | The vector $A=\mathbf a_r(3\cos\varphi)-\mathbf a_\varphi2r+\mathbf a_z5$ is printed with a non-bold $A$. The notes print it in bold, like every other vector. |
| Ch2_5 p. 10 | «در نتیجه مانند هادی‌ها چگالی بار و میدان الکتریکی داخلی آن‌ها برابر با صفر نیست» is kept as written; the English edition gives the evident meaning ("…are not zero, as they are in conductors"). |
| Ch2_4 p. 5 | For $q=+1\,\mathrm C$ the work is written $W=\int\nabla V\cdot d\mathbf l$, consistent with $W=-q\int\mathbf E\cdot d\mathbf l$ and $\mathbf E=-\nabla V$. |
