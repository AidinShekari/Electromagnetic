# Static Magnetic Fields

## Course Outline

```{.figure #m05-course-outline caption=""}
```

## Static Magnetic Fields

- When a small test charge is placed in an electric field $\vect{E}$, the following force acts on it

$$\vect{F}_e=q\vect{E}\qquad(\mathrm{N})$$

- When this test charge moves in a magnetic field, another force acts on it, equal to

$$\vect{F}_m=q\vect{u}\times\vect{B}\qquad(\mathrm{N})$$

- $\vect{B}$: the magnetic flux density, in webers per square metre or teslas
- So the total electromagnetic force on the charge $q$ is

::: {.important title="Lorentz's force equation"}
$$\vect{F}=q(\vect{E}+\vect{u}\times\vect{B})\qquad(\mathrm{N})$$
:::

```{.figure #m05-map caption=""}
```

- What are the fundamental postulates of magnetostatics, from which the other relations and laws of the field can be derived?
- How is **Ampère's circuital law** derived from these postulates?
- How can the magnetic flux density of a current be found with Ampère's circuital law?

## Fundamental Postulates of Magnetostatics in Free Space

- The two fundamental postulates of magnetostatics in free space

::: {.important}
$$\nabla\cdot\vect{B}=0$$
$$\nabla\times\vect{B}=\mu_0\vect{J}$$
:::

- $\mu_0=4\pi\times10^{-7}\,\mathrm{(H/m)}$: the permeability of free space
- $\vect{J}$: the volume current density $\mathrm{(A/m^2)}$
- Since the divergence of the curl of any vector field is zero, it follows that

$$\nabla\cdot\vect{J}=0$$

- There is no magnetic analogue of the electric charge density.
- The integral form of the first relation $\ELto$ integrate over an arbitrary volume $V$ and apply the divergence theorem

::: {.important title="Law of conservation of magnetic flux"}
$$\oint_S\vect{B}\cdot d\vect{s}=0$$
:::

- This equation is called the **law of conservation of magnetic flux**.
    - There are no magnetic flow sources, and the magnetic flux lines always close upon themselves.
- The integral form of the second relation $\ELto$ integrate over an arbitrary open surface $S$ and apply Stokes's theorem

$$\int_S(\nabla\times\vect{B})\cdot d\vect{s}=\mu_0\int_S\vect{J}\cdot d\vect{s}$$

::: {.important title="Ampère's circuital law"}
$$\oint_C\vect{B}\cdot\dif\vect{\ell}=\mu_0I$$
:::

- $C$: the contour bounding the surface $S$ (the contour $C$ and the current $I$ follow the right-hand rule)
- $I$: the current passing through the surface $S$
- This equation is a form of **Ampère's circuital law**.
    - The circulation of the magnetic flux density in free space around any closed path is equal to $\mu_0$ times the total current flowing through the surface bounded by the path.
- Ampère's circuital law is useful for finding the magnetic flux density caused by a current $I$ when there is a closed path $C$ around the current such that $\vect{B}$ is constant on the path.

::: {.example number="5-1"}
An infinitely long, straight conductor with a circular cross-section of radius $b$ carries a current $I$. Determine the magnetic flux density both inside and outside the conductor.

```{.figure #m05-ex1 caption=""}
```

::: {.solution}
- If the conductor lies along the $z$-axis, $\vect{B}$ is in the $\phi$ direction and its magnitude is constant along any circular path about the $z$-axis.
    - Inside the conductor

$$\left.\begin{aligned}&\vect{B}_1=\uvec{\phi}B_{\phi1},\qquad\dif\vect{\ell}=\uvec{\phi}r_1\,d\phi\\&\oint_{C_1}\vect{B}_1\cdot\dif\vect{\ell}=\int_0^{2\pi}B_{\phi1}r_1\,d\phi=2\pi r_1B_{\phi1}\\&I_1=\frac{\pi r_1^2}{\pi b^2}I=\left(\frac{r_1}{b}\right)^2I\end{aligned}\right\}\quad\vect{B}_1=\uvec{\phi}B_{\phi1}=\uvec{\phi}\frac{\mu_0r_1I}{2\pi b^2}$$

- Outside the conductor

$$\vect{B}_2=\uvec{\phi}B_{\phi2},\qquad\dif\vect{\ell}=\uvec{\phi}r_2\,d\phi$$
$$\oint_{C_2}\vect{B}_2\cdot\dif\vect{\ell}=2\pi r_2B_{\phi2}$$
$$\vect{B}_2=\uvec{\phi}B_{\phi2}=\uvec{\phi}\frac{\mu_0I}{2\pi r_2}$$
:::
:::

::: {.example number="5-2"}
Determine the magnetic flux density inside a closely wound toroidal coil with an air core, having $N$ turns of wire carrying a current $I$.

```{.figure #m05-ex2 caption=""}
```

::: {.solution}
- Cylindrical symmetry ensures that $\vect{B}$ has only a $\phi$ component and that its magnitude is constant along any circular path about the axis of the coil.

$$\oint\vect{B}\cdot\dif\vect{\ell}=2\pi rB_\phi=\mu_0NI$$
$$\vect{B}=\uvec{\phi}B_\phi=\uvec{\phi}\frac{\mu_0NI}{2\pi r},\qquad(b-a)<r<(b+a)$$
:::
:::

::: {.example number="5-3"}
Determine the magnetic flux density inside an infinitely long solenoid with an air core, having $n$ turns of wire per unit length carrying a current $I$.

```{.figure #m05-ex3 caption=""}
```

::: {.solution}
- Outside the solenoid the magnetic field is zero.
- By the symmetry of the structure, $\vect{B}$ is parallel to the axis of the solenoid and its magnitude is constant along the solenoid.

$$BL=\mu_0nLI$$
$$B=\mu_0nI$$
:::
:::

## Vector Magnetic Potential

```{.figure #m05-map-vecpot caption=""}
```

- What is the vector magnetic potential, where is it used, and how is it calculated?
- What is the Biot–Savart law, and how is it used to calculate the magnetic flux density?

$$\nabla\cdot\vect{B}=0\quad\Longrightarrow\quad\boxed{\vect{B}=\nabla\times\vect{A}\qquad(\mathrm{T})}$$

- $\vect{A}$ is called the **vector magnetic potential**. Its unit is the weber per metre.
    - If $\vect{A}$ can be found for a current distribution, $\vect{B}$ follows easily (exactly as with $V$ and $\vect{E}$).
- A vector is defined by its curl and its divergence. To specify the divergence of $\vect{A}$ we proceed as follows

$$\nabla\times\vect{B}=\mu_0\vect{J}\quad\Longrightarrow\quad\nabla\times\nabla\times\vect{A}=\mu_0\vect{J}$$

- We define the **Laplacian of a vector quantity** as

$$\nabla^2\vect{A}=\nabla(\nabla\cdot\vect{A})-\nabla\times\nabla\times\vect{A}$$

- For example, the Laplacian of $\vect{A}$ in Cartesian coordinates is

$$\nabla^2\vect{A}=\uvec{x}\nabla^2A_x+\uvec{y}\nabla^2A_y+\uvec{z}\nabla^2A_z$$

- Therefore

$$\nabla(\nabla\cdot\vect{A})-\nabla^2\vect{A}=\mu_0\vect{J}$$

- To simplify this relation we choose

$$\nabla\cdot\vect{A}=0\quad\Longrightarrow\quad\boxed{\nabla^2\vect{A}=-\mu_0\vect{J}}$$

- This last relation is the **vector Poisson's equation**.
- In Cartesian coordinates

$$\nabla^2A_x=-\mu_0J_x,\qquad\nabla^2A_y=-\mu_0J_y,\qquad\nabla^2A_z=-\mu_0J_z$$

- Each of these three equations is mathematically the same as Poisson's equation in electrostatics.
- Earlier we had

$$\nabla^2V=-\frac{\rho}{\epsilon_0}\quad\Longrightarrow\quad V=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho}{\lvert\vect{R}-\vect{R}'\rvert}\,dv'$$

- In the same way we obtain

::: {.important}
$$\vect{A}=\frac{\mu_0}{4\pi}\int_{V'}\frac{\vect{J}}{\lvert\vect{R}-\vect{R}'\rvert}\,dv'$$
:::

- So $\vect{A}$ can be found from the current density with this relation, and $\vect{B}$ then follows by taking its curl.
- The physical meaning of the vector magnetic potential

$$\Phi=\int_S\vect{B}\cdot d\vect{s}$$

- $\Phi$: the magnetic flux, in webers

::: {.important}
$$\Phi=\int_S(\nabla\times\vect{A})\cdot d\vect{s}=\oint_C\vect{A}\cdot\dif\vect{\ell}\qquad(\mathrm{Wb})$$
:::

- The line integral of $\vect{A}$ around any closed path $C$ equals the total magnetic flux passing through the surface bounded by the path.

## The Biot–Savart Law

```{.figure #m05-map-biot caption=""}
```

- For a thin wire carrying a current $I$, with cross-section $S$, we have

$$\vect{J}\,dv'=JS\,d\ell'=I\,\dif\vect{\ell}'\quad\Longrightarrow\quad\vect{A}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}$$

- It can be shown that

$$\vect{B}=\nabla\times\vect{A}=\nabla\times\left[\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}\right]$$

::: {.important title="Biot–Savart law"}
$$\vect{B}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'\times(\vect{R}-\vect{R}')}{\lvert\vect{R}-\vect{R}'\rvert^3}$$
:::

- This equation is called the **Biot–Savart law**.
    - In general the Biot–Savart law is more difficult to use than Ampère's circuital law. But when no closed path can be found on which $\vect{B}$ is constant, Ampère's circuital law cannot be used to determine $\vect{B}$.

::: {.example number="5-4"}
A direct current $I$ flows in a straight wire of length $2L$. Find the magnetic flux density at a point at a distance $r$ from the wire in the bisecting plane.

```{.figure #m05-ex4 caption=""}
```

::: {.solution}
- Currents exist only in closed circuits. The wire in this example must therefore be part of a current-carrying loop. Since we know nothing about the rest of the circuit, Ampère's circuital law cannot be used.
- **First method**

$$\left.\begin{aligned}&\vect{A}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}\\&\dif\vect{\ell}'=dz'\,\uvec{z}\\&\vect{R}=r\uvec{r}\\&\vect{R}'=z'\uvec{z}\end{aligned}\right\}\quad\begin{aligned}\vect{A}&=\uvec{z}\frac{\mu_0I}{4\pi}\int_{-L}^{L}\frac{dz'}{\sqrt{z'^2+r^2}}\\&=\uvec{z}\frac{\mu_0I}{4\pi}\ln\frac{\sqrt{L^2+r^2}+L}{\sqrt{L^2+r^2}-L}\end{aligned}$$
$$\vect{B}=\nabla\times\vect{A}=\nabla\times(\uvec{z}A_z)=\uvec{r}\frac1r\frac{\partial A_z}{\partial\phi}-\uvec{\phi}\frac{\partial A_z}{\partial r}$$
$$\begin{aligned}\vect{B}&=-\uvec{\phi}\frac{\partial}{\partial r}\left[\frac{\mu_0I}{4\pi}\ln\frac{\sqrt{L^2+r^2}+L}{\sqrt{L^2+r^2}-L}\right]\\&=\uvec{\phi}\frac{\mu_0IL}{2\pi r\sqrt{L^2+r^2}}\end{aligned}$$

- **Second method**

$$\left.\begin{aligned}&\vect{B}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'\times(\vect{R}-\vect{R}')}{\lvert\vect{R}-\vect{R}'\rvert^3}\\&\vect{R}-\vect{R}'=r\uvec{r}-z'\uvec{z}\\&\dif\vect{\ell}'\times(\vect{R}-\vect{R}')=dz'\uvec{z}\times(r\uvec{r}-z'\uvec{z})=r\,dz'\,\uvec{\phi}\end{aligned}\right\}\quad\begin{aligned}\vect{B}=\int d\vect{B}&=\uvec{\phi}\frac{\mu_0I}{4\pi}\int_{-L}^{L}\frac{r\,dz'}{(z'^2+r^2)^{3/2}}\\&=\uvec{\phi}\frac{\mu_0IL}{2\pi r\sqrt{L^2+r^2}}\end{aligned}$$
:::
:::

::: {.example number="5-5"}
Find the magnetic flux density at the centre of a square loop of side $w$ carrying a current $I$.

```{.figure #m05-ex5 caption=""}
```

::: {.solution}
- Assume the loop lies in the $xy$-plane. $\vect{B}$ at the centre of the loop is four times the magnetic flux density caused by one side of length $w$. Therefore
- The magnitude of the magnetic flux density of a straight wire of length $2L$ at a distance $r$ from it

$$B=\frac{\mu_0IL}{2\pi r\sqrt{L^2+r^2}}\qquad L=\frac w2,\quad r=\frac w2$$
$$\vect{B}=\uvec{z}\frac{\mu_0I}{\sqrt2\pi w}\times4=\uvec{z}\frac{2\sqrt2\mu_0I}{\pi w}$$
:::
:::

::: {.example number="5-6"}
Find the magnetic flux density on the axis of a circular loop of radius $b$ carrying a current $I$.

```{.figure #m05-ex6 caption=""}
```

::: {.solution}
$$\left.\begin{aligned}&\vect{B}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'\times(\vect{R}-\vect{R}')}{\lvert\vect{R}-\vect{R}'\rvert^3}\\&\dif\vect{\ell}'=b\,d\phi'\,\uvec{\phi'},\quad\vect{R}=z\uvec{z},\quad\vect{R}'=b\uvec{r'}\\&\vect{R}-\vect{R}'=z\uvec{z}-b\uvec{r'}\\&\begin{aligned}\dif\vect{\ell}'\times(\vect{R}-\vect{R}')&=b\,d\phi'\,\uvec{\phi'}\times(z\uvec{z}-b\uvec{r'})\\&=bz\,d\phi'\,\uvec{r'}+b^2d\phi'\,\uvec{z}\end{aligned}\end{aligned}\right\}\quad\vect{B}=\frac{\mu_0I}{4\pi}\int_0^{2\pi}\uvec{z}\frac{b^2\,d\phi'}{(z^2+b^2)^{3/2}}$$

- It is evident from the geometry that the $r$-component of the magnetic flux density is zero.

::: {.important}
$$\vect{B}=\uvec{z}\frac{\mu_0Ib^2}{2(z^2+b^2)^{3/2}}\qquad(\mathrm{T})$$
:::
:::
:::

::: {.example number="5-7"}
Find the magnetic flux density at a distant point of a magnetic dipole of radius $b$ carrying a current $I$.

```{.figure #m05-ex7 caption=""}
```

::: {.solution}
$$\vect{A}=\frac{\mu_0I}{4\pi}\oint_{C'}\frac{\dif\vect{\ell}'}{\lvert\vect{R}-\vect{R}'\rvert}$$

- Because of the symmetry of the geometry, the magnetic field is independent of the angle $\phi$. For simplicity, the field point is therefore placed in the $yz$-plane.

$$\dif\vect{\ell}'=b\,d\phi'\,\uvec{\phi'}=b\,d\phi'\left(-\uvec{x}\sin\phi'+\uvec{y}\cos\phi'\right)$$
$$\vect{A}=-\uvec{x}\frac{\mu_0I}{4\pi}\int_0^{2\pi}\frac{b\sin\phi'}{\lvert\vect{R}-\vect{R}'\rvert}\,d\phi'+\uvec{y}\frac{\mu_0I}{4\pi}\int_0^{2\pi}\frac{b\cos\phi'}{\lvert\vect{R}-\vect{R}'\rvert}\,d\phi'$$

- It is evident from the geometry that the $y$-component of $\vect{A}$ is zero.

```{.figure #m05-ex7-top caption=""}
```

$$\begin{aligned}\vect{R}=R\uvec{R}&=R\left(\sin\theta\cos(\pi/2)\uvec{x}+\sin\theta\sin(\pi/2)\uvec{y}+\cos\theta\,\uvec{z}\right)\\&=R\left(\sin\theta\,\uvec{y}+\cos\theta\,\uvec{z}\right)\end{aligned}$$
$$\vect{R}'=b\uvec{r'}=b\left(\cos\phi'\,\uvec{x}+\sin\phi'\,\uvec{y}\right)$$
$$\vect{R}-\vect{R}'=-b\cos\phi'\,\uvec{x}+(R\sin\theta-b\sin\phi')\uvec{y}+R\cos\theta\,\uvec{z}$$
$$\begin{aligned}\lvert\vect{R}-\vect{R}'\rvert^2&=R^2+b^2-2bR\sin\theta\sin\phi'\\&=R^2\left(1+\frac{b^2}{R^2}-\frac{2b}{R}\sin\theta\sin\phi'\right)\end{aligned}$$
$$\begin{aligned}\frac{1}{\lvert\vect{R}-\vect{R}'\rvert}&=\frac1R\left(1+\frac{b^2}{R^2}-\frac{2b}{R}\sin\theta\sin\phi'\right)^{-1/2}\\&\cong\frac1R\left(1-\frac{2b}{R}\sin\theta\sin\phi'\right)^{-1/2}\cong\frac1R\left(1+\frac bR\sin\theta\sin\phi'\right)\end{aligned}$$
$$\begin{aligned}\vect{A}&=-\uvec{x}\frac{\mu_0Ib}{4\pi R}\int_0^{2\pi}\left(1+\frac bR\sin\theta\sin\phi'\right)\sin\phi'\,d\phi'\\&=-\uvec{x}\frac{\mu_0Ib^2}{4R^2}\sin\theta\end{aligned}$$

- At an arbitrary field point, the vector magnetic potential is then

$$\vect{A}=\uvec{\phi}\frac{\mu_0Ib^2}{4R^2}\sin\theta\quad\Longrightarrow\quad\vect{A}=\uvec{\phi}\frac{\mu_0(I\pi b^2)}{4\pi R^2}\sin\theta$$

- The magnetic dipole moment vector

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

## The Static Magnetic Field in Material Media

```{.figure #m05-map-media caption=""}
```

- All materials consist of atoms with a positively charged nucleus and a number of negatively charged electrons orbiting around it.
- The motion of the electrons produces circulating currents and hence microscopic magnetic dipoles.
- In the absence of an external magnetic field, the magnetic dipoles of the atoms of most materials (except permanent magnets) have random orientations, and no net magnetic moment results. When an external magnetic field is applied, the magnetic moments of the orbiting electrons align.
- How do different materials behave when exposed to a magnetic field, and how can this behaviour be analysed?

### Magnetization and Equivalent Current Densities

```{.figure #m05-magnetization caption=""}
```

- The magnetization vector (and the polarization vector in electrostatics)

$$\vect{M}=\lim_{\Delta v\to0}\frac{\sum_{k=1}^{n\Delta v}\vect{m}_k}{\Delta v}\quad(\mathrm{A/m})\qquad\qquad\vect{P}=\lim_{\Delta v\to0}\frac{\sum_{k=1}^{n\Delta v}\vect{p}_k}{\Delta v}\quad(\mathrm{C/m^2})$$

- The vector magnetic potential of a magnetized material (and the electric potential of a polarized material)

$$\vect{A}=\frac{\mu_0}{4\pi}\int_{V'}\frac{\nabla'\times\vect{M}}{R}\,dv'+\frac{\mu_0}{4\pi}\oint_{S'}\frac{\vect{M}\times\uvec{n}'}{R}\,ds'$$
$$V=\frac{1}{4\pi\epsilon_0}\oint_{S'}\frac{\vect{P}\cdot\uvec{n}'}{R}\,ds'+\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{(-\nabla'\cdot\vect{P})}{R}\,dv'$$

- The equivalent magnetization surface and volume current densities

::: {.important}
$$\vect{J}_{ms}=\vect{M}\times\uvec{n},\qquad\vect{J}_m=\nabla\times\vect{M}$$
:::

- The equivalent polarization surface and volume charge densities

$$\rho_{ps}=\vect{P}\cdot\uvec{n},\qquad\rho_p=-\nabla\cdot\vect{P}$$

- The problem of finding the magnetic flux density $\vect{B}$ caused by a given volume density of magnetic dipole moment $\vect{M}$ becomes one of finding the equivalent magnetization current densities, then $\vect{A}$, and then $\vect{B}$.

::: {.example number="5-8"}
Determine the magnetic flux density on the axis of a magnetized cylinder. The cylinder has a radius $b$, a length $L$ and a magnetization vector $\vect{M}=\uvec{z}M_0$.

```{.figure #m05-ex8 caption=""}
```

::: {.solution}
$$\vect{J}_m=\nabla\times\vect{M}=0$$

- The equivalent surface current density on the side wall

$$\vect{J}_{ms}=\vect{M}\times\uvec{n}=\uvec{z}M_0\times\uvec{r}=\uvec{\phi}M_0$$

- The equivalent surface current density on the top and bottom faces is zero.

$$\left.\begin{aligned}&\vect{B}=\frac{\mu_0}{4\pi}\int_{S'}\frac{\vect{J}_{ms}\times(\vect{R}-\vect{R}')\,ds'}{\lvert\vect{R}-\vect{R}'\rvert^3}\\&ds'=b\,d\phi'\,dz'\\&\vect{R}=z\uvec{z}\\&\vect{R}'=b\uvec{r'}+z'\uvec{z}\\&\vect{R}-\vect{R}'=(z-z')\uvec{z}-b\uvec{r'}\\&\begin{aligned}\vect{J}_{ms}\times(\vect{R}-\vect{R}')&=M_0\uvec{\phi'}\times\left((z-z')\uvec{z}-b\uvec{r'}\right)\\&=M_0(z-z')\uvec{r'}+bM_0\uvec{z}\end{aligned}\end{aligned}\right\}$$

- It is evident from the geometry that the $r$-component of the magnetic flux density is zero.

$$\begin{aligned}\vect{B}=\int d\vect{B}&=\uvec{z}\int_0^L\frac{\mu_0M_0b^2\,dz'}{2\left[(z-z')^2+b^2\right]^{3/2}}\\&=\uvec{z}\frac{\mu_0M_0}{2}\left[\frac{z}{\sqrt{z^2+b^2}}-\frac{z-L}{\sqrt{(z-L)^2+b^2}}\right]\end{aligned}$$
:::
:::

## Magnetic Field Intensity and Relative Permeability

```{.figure #m05-map-hmu caption=""}
```

### Magnetic Field Intensity

- Since an external magnetic field aligns the internal dipole moments and induces a magnetic moment in a magnetic material, we expect the resulting magnetic flux density in the presence of the magnetic material to differ from its value in free space.
- Taking the equivalent volume current density in the material into account, we have

$$\frac{1}{\mu_0}\nabla\times\vect{B}=\vect{J}+\vect{J}_m=\vect{J}+\nabla\times\vect{M}\quad\Longrightarrow\quad\nabla\times\left(\frac{\vect{B}}{\mu_0}-\vect{M}\right)=\vect{J}$$

- We define the magnetic field intensity as

::: {.important}
$$\vect{H}=\frac{\vect{B}}{\mu_0}-\vect{M}\qquad(\mathrm{A/m})$$
:::

- The vector $\vect{H}$ lets us write the curl equation relating the magnetic field and the distribution of free currents in any medium without using $\vect{M}$ or $\vect{J}_m$

::: {.important}
$$\nabla\times\vect{H}=\vect{J}\qquad(\mathrm{A/m^2})$$
:::

- $\vect{J}$: the density of the free current
- The integral form

$$\int_S(\nabla\times\vect{H})\cdot d\vect{s}=\int_S\vect{J}\cdot d\vect{s}\quad\Longrightarrow\quad\boxed{\oint_C\vect{H}\cdot\dif\vect{\ell}=I\qquad(\mathrm{A})}$$

- This last relation is another form of Ampère's circuital law.
- The two fundamental governing equations for magnetostatics in any medium

::: {.important}
$$\left\{\begin{aligned}&\nabla\cdot\vect{B}=0\\&\nabla\times\vect{H}=\vect{J}\end{aligned}\right.$$
:::

### Relative Permeability

- The relation between the magnetization vector and the magnetic field intensity

$$\vect{M}=\chi_m\vect{H}$$

- $\chi_m$: the magnetic susceptibility
- The relation between the magnetic field intensity and the magnetic flux density

::: {.important}
$$\begin{aligned}\vect{B}&=\mu_0(1+\chi_m)\vect{H}\\&=\mu_0\mu_r\vect{H}=\mu\vect{H}\qquad(\mathrm{Wb/m^2})\end{aligned}$$
:::

$$\mu_r=1+\chi_m=\frac{\mu}{\mu_0}$$

- $\mu_r$: a dimensionless quantity called the relative permeability of the medium
- The relations of electrostatics and of magnetostatics are dual to each other

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

### Behaviour of Magnetic Materials

- Magnetic materials can be roughly classified into three main groups according to their relative permeability
    - **Diamagnetic materials**: $\mu_r<1$ ($\chi_m$ is a very small negative number)
        - In these materials the net magnetic moment is zero in the absence of an applied external magnetic field. $\ELto$ copper, lead, mercury, silver and gold $\ELto$ $\chi_m\approx-10^{-5}$
    - **Paramagnetic materials**: $\mu_r>1$ ($\chi_m$ is a very small positive number)
        - In these materials there is a net average magnetic moment in the absence of an applied external magnetic field. $\ELto$ aluminium, magnesium and tungsten $\ELto$ $\chi_m\approx10^{-5}$
    - **Ferromagnetic materials**: $\mu_r\gg1$ ($\chi_m$ is a large positive number)
        - In these materials the magnetic moment is many times larger than in paramagnetic materials. $\ELto$ cobalt, nickel and iron
        - The relation between $\vect{B}$ and $\vect{H}$ in a ferromagnetic material is nonlinear.

```{.figure #m05-hysteresis caption="The hysteresis phenomenon"}
```

## Magnetic Circuits

```{.figure #m05-map-circ caption=""}
```

- As with electric circuits, it is sometimes necessary to calculate the magnetic flux and the magnetic field intensity produced in a magnetic circuit by current-carrying windings.
- To analyse magnetic circuits we have

$$\nabla\cdot\vect{B}=0,\qquad\nabla\times\vect{H}=\vect{J}$$
$$\oint_C\vect{H}\cdot\dif\vect{\ell}=NI=\mathcal{V}_m$$

- $\mathcal{V}_m$: the magnetomotive force, in $\mathrm{A}$. It is the analogue of the electromotive force in electric circuits.

::: {.example number="5-9"}
Assume that $N$ turns of wire are wound around a toroidal core of a magnetic material with permeability $\mu$. The core has a mean radius $r_0$, a circular cross-section of radius $a$ and a narrow air gap of length $\ell_g$. A steady current $I_0$ flows in the wire. Determine

- (a) the magnetic flux density in the magnetic core,
- (b) the magnetic field intensity in the magnetic core,
- (c) the magnetic field intensity in the air gap.

```{.figure #m05-ex9 caption=""}
```

::: {.solution}
- **First assumption**: the leakage flux is neglected

```{.figure #m05-ex9-gauss caption=""}
```

$$\nabla\cdot\vect{B}=0\quad\Longrightarrow\quad\oint_S\vect{B}\cdot d\vect{s}=0$$

- The flux in the core and in the air gap is the same.
- **Second assumption**: the fringing of the flux in the air gap is neglected.
    - The flux density in the core and in the air gap is the same.

$$\vect{B}_f=\vect{B}_g=\uvec{\phi}B_f$$
$$\vect{H}_f=\uvec{\phi}\frac{B_f}{\mu},\qquad\vect{H}_g=\uvec{\phi}\frac{B_f}{\mu_0}$$
$$\oint_C\vect{H}\cdot\dif\vect{\ell}=NI_0\quad\Longrightarrow\quad\frac{B_f}{\mu}(2\pi r_0-\ell_g)+\frac{B_f}{\mu_0}\ell_g=NI_0$$

- (a)

$$\vect{B}_f=\uvec{\phi}\frac{\mu_0\mu NI_0}{\mu_0(2\pi r_0-\ell_g)+\mu\ell_g}$$

- (b)

$$\vect{H}_f=\uvec{\phi}\frac{\mu_0NI_0}{\mu_0(2\pi r_0-\ell_g)+\mu\ell_g}$$

- (c)

$$\vect{H}_g=\uvec{\phi}\frac{\mu NI_0}{\mu_0(2\pi r_0-\ell_g)+\mu\ell_g}$$
:::
:::

- If the radius of the cross-section of the core is much smaller than the mean radius of the toroid, the magnetic flux density in the core is approximately constant, and

$$\Phi\cong BS\quad\Longrightarrow\quad\Phi=\frac{NI_0}{(2\pi r_0-\ell_g)/\mu S+\ell_g/\mu_0S}\quad\Longrightarrow\quad\Phi=\frac{\mathcal{V}_m}{\mathcal{R}_f+\mathcal{R}_g}$$

::: {.important}
$$\mathcal{R}_f=\frac{2\pi r_0-\ell_g}{\mu S}=\frac{\ell_f}{\mu S},\qquad\mathcal{R}_g=\frac{\ell_g}{\mu_0S}$$
:::

- $\mathcal{R}_f$ and $\mathcal{R}_g$: reluctances, in $1/\mathrm{H}$

- This magnetic circuit is analogous to an electric circuit as follows

```{.figure #m05-circuits caption=""}
```

$$\Phi=\frac{\mathcal{V}_m}{\mathcal{R}_f+\mathcal{R}_g},\qquad I=\frac{\mathcal{V}}{R_f+R_g}$$

| Magnetic Circuits | Electric Circuits |
|---|---|
| mmf, $\mathcal{V}_m\,(=NI)$ | emf, $\mathcal{V}$ |
| magnetic flux, $\Phi$ | electric current, $I$ |
| reluctance, $\mathcal{R}$ | resistance, $R$ |
| permeability, $\mu$ | conductivity, $\sigma$ |

- In analogy to Kirchhoff's voltage law in electric circuits, in magnetic circuits we have

::: {.important}
$$\sum_jN_jI_j=\sum_k\mathcal{R}_k\Phi_k$$
:::

- So around any closed path in a magnetic circuit, the algebraic sum of the ampere-turns equals the algebraic sum of the products of the reluctances and the fluxes.
- In analogy to Kirchhoff's current law in electric circuits, in magnetic circuits we have

::: {.important}
$$\sum_j\Phi_j=0$$
:::

- which states that the algebraic sum of all the magnetic fluxes flowing out of a junction in a magnetic circuit is zero.
- Despite this simple analogy, an exact analysis of magnetic circuits is very difficult, for the following reasons
    - the leakage fluxes,
    - the fringing effects, which make the magnetic flux lines spread out and bulge in the air gap,
    - the dependence of the permeability of ferromagnetic materials on the magnetic field intensity, that is, the nonlinear relation between $\vect{B}$ and $\vect{H}$.

::: {.example number="5-10"}
Consider the magnetic circuit shown below. Steady currents $I_1$ and $I_2$ flow in windings of $N_1$ and $N_2$ turns respectively. The core has a cross-sectional area $S_c$ and a permeability $\mu$. Determine the magnetic flux in the middle leg.

```{.figure #m05-ex10 caption=""}
```

::: {.solution}
- The equivalent circuit

```{.figure #m05-ex10-circuit caption=""}
```

$$\mathcal{R}_1=\frac{\ell_1}{\mu S_c},\qquad\mathcal{R}_2=\frac{\ell_2}{\mu S_c},\qquad\mathcal{R}_3=\frac{\ell_3}{\mu S_c}$$
$$\begin{aligned}&\mathit{Loop}~1:&N_1I_1&=(\mathcal{R}_1+\mathcal{R}_3)\Phi_1+\mathcal{R}_1\Phi_2\\&\mathit{Loop}~2:&N_1I_1-N_2I_2&=\mathcal{R}_1\Phi_1+(\mathcal{R}_1+\mathcal{R}_2)\Phi_2\end{aligned}$$
$$\Phi_1=\frac{\mathcal{R}_2N_1I_1+\mathcal{R}_1N_2I_2}{\mathcal{R}_1\mathcal{R}_2+\mathcal{R}_1\mathcal{R}_3+\mathcal{R}_2\mathcal{R}_3}$$
:::
:::

## Boundary Conditions for Magnetostatic Fields

```{.figure #m05-map-bc caption=""}
```

- The boundary condition for the normal components

$$\nabla\cdot\vect{B}=0\quad\Longrightarrow\quad\boxed{B_{1n}=B_{2n}\qquad(\mathrm{T})}$$

- In linear media

::: {.important}
$$\mu_1H_{1n}=\mu_2H_{2n}$$
:::

- The boundary condition for the tangential components

```{.figure #m05-bc caption=""}
```

$$\oint_C\vect{H}\cdot\dif\vect{\ell}=I$$
$$\oint_{abcda}\vect{H}\cdot\dif\vect{\ell}=\vect{H}_1\cdot\Delta\vect{w}+\vect{H}_2\cdot(-\Delta\vect{w})=J_{sn}\Delta w$$
$$H_{1t}-H_{2t}=J_{sn}\qquad(\mathrm{A/m})$$

::: {.important}
$$\uvec{n2}\times(\vect{H}_1-\vect{H}_2)=\vect{J}_s\qquad(\mathrm{A/m})$$
:::

## Inductances and Inductors

```{.figure #m05-map-induct caption=""}
```

- What kind of element is an inductor, and what is inductance?
- How is the inductance of different structures calculated?

```{.figure #m05-two-loops caption=""}
```

- Consider two closed loops. If a current $I_1$ flows in $C_1$, a magnetic field $\vect{B}_1$ is produced. Some of the magnetic flux due to $\vect{B}_1$ links $C_2$. This mutual flux is

$$\Phi_{12}=\int_{S_2}\vect{B}_1\cdot d\vect{s}_2\qquad(\mathrm{Wb})$$

- If $C_2$ has $N_2$ turns, the flux linkage is

$$\Lambda_{12}=N_2\Phi_{12}\qquad(\mathrm{Wb})$$

- From the Biot–Savart law, $\vect{B}_1$, and hence $\Phi_{12}$, is proportional to $I_1$. Therefore

$$\Lambda_{12}=L_{12}I_1\qquad(\mathrm{Wb})\quad\Longrightarrow\quad\boxed{L_{12}=\frac{\Lambda_{12}}{I_1}\qquad(\mathrm{H})}$$

- The proportionality constant $L_{12}$ is called the **mutual inductance** between the loops $C_1$ and $C_2$; its unit is the henry $(\mathrm{H})$. The mutual inductance between two circuits is the magnetic flux linkage with one circuit per unit current in the other.
- The total flux linkage with $C_1$ caused by $I_1$ is

$$\Lambda_{11}=N_1\Phi_{11}\quad\Longrightarrow\quad\boxed{L_{11}=\frac{\Lambda_{11}}{I_1}}$$

- The **self-inductance** of a loop is the magnetic flux linkage of the loop per unit current in the loop itself.
- The self-inductance of a circuit and the mutual inductance between two circuits depend on the geometrical shape and on the permeability of the medium. In a linear medium the self- and mutual inductances do not depend on the currents.
- A conductor shaped suitably to provide a certain amount of self-inductance is called an inductor.
- Just as a capacitor can store electric energy, an inductor can store magnetic energy.
- The steps for determining the **self-inductance** of an inductor are
    - choose a suitable coordinate system,
    - assume a current $I$ in the wire,
    - find $\vect{B}$ from $I$,
    - find the flux linking each turn

$$\Phi=\int_S\vect{B}\cdot d\vect{s}$$

- $S$: the surface over which $\vect{B}$ exists and which links the assumed current
    - find the flux linkage,
    - find $L$

$$L=\Lambda/I$$

- The steps for determining the **mutual inductance** between two circuits are
    - choose a suitable coordinate system,
    - assume a current $I_1$ in the wire,
    - find $\vect{B}_1$ from $I_1$,
    - find the mutual flux

$$\Phi_{12}=\int_{S_2}\vect{B}_1\cdot d\vect{s}_2$$

- find the flux linkage

$$\Lambda_{12}=N_2\Phi_{12}$$

- find $L_{12}$

$$L_{12}=\frac{\Lambda_{12}}{I_1}\qquad(\mathrm{H})$$

- It can be shown that

::: {.important}
$$L_{12}=L_{21}$$
:::

::: {.example number="5-11"}
Assume that $N$ turns of wire are tightly wound on a toroidal frame of rectangular cross-section, as shown below. Assuming that the permeability of the medium is $\mu_0$, find the self-inductance of the toroidal coil.

```{.figure #m05-ex11 caption=""}
```

::: {.solution}
- Choose cylindrical coordinates.
- Assume a current $I$ in the coil.
- Find $\vect{B}$ with Ampère's circuital law

$$\vect{B}=\uvec{\phi}B_\phi,\qquad\dif\vect{\ell}=\uvec{\phi}r\,d\phi$$
$$\oint_C\vect{B}\cdot\dif\vect{\ell}=\int_0^{2\pi}B_\phi r\,d\phi=2\pi rB_\phi$$
$$2\pi rB_\phi=\mu_0NI\quad\Longrightarrow\quad B_\phi=\frac{\mu_0NI}{2\pi r}$$

- Find $\Phi$ and $\Lambda$

$$\begin{aligned}\Phi=\int_S\vect{B}\cdot d\vect{s}&=\int_S\left(\uvec{\phi}\frac{\mu_0NI}{2\pi r}\right)\cdot(\uvec{\phi}h\,dr)\\&=\frac{\mu_0NIh}{2\pi}\int_a^b\frac{dr}{r}=\frac{\mu_0NIh}{2\pi}\ln\frac ba\end{aligned}\quad\Longrightarrow\quad\Lambda=\frac{\mu_0N^2Ih}{2\pi}\ln\frac ba$$

- Find $L$

$$L=\frac\Lambda I=\frac{\mu_0N^2h}{2\pi}\ln\frac ba$$
:::
:::

::: {.example number="5-12"}
Find the inductance per unit length of a very long solenoid with an air core and $n$ turns per unit length.

::: {.solution}
$$B=\mu_0nI$$
$$\Phi=BS=\mu_0nSI$$
$$\Lambda'=n\Phi=\mu_0n^2SI$$
$$L'=\mu_0n^2S\qquad(\mathrm{H/m})$$
:::
:::

::: {.example number="5-13"}
Find the mutual inductance between a triangular conducting loop and a very long straight wire.

```{.figure #m05-ex13 caption=""}
```

::: {.solution}
- Assume a current $I_2$ in the long wire and find the $\vect{B}$ it produces

$$\vect{B}_2=\uvec{\phi}\frac{\mu_0I_2}{2\pi r}$$

- Find the flux linkage

$$\begin{aligned}\Lambda_{21}&=\int_{S_1}\vect{B}_2\cdot d\vect{s}_1\\&=\int_d^{d+b}\int_0^{[(d+b)-r]\tan60^\circ}\frac{\mu_0I_2}{2\pi r}\,dz\,dr\end{aligned}$$
$$\begin{aligned}\Lambda_{21}&=-\frac{\sqrt3\mu_0I_2}{2\pi}\int_d^{d+b}\frac1r\left[r-(d+b)\right]dr\\&=\frac{\sqrt3\mu_0I_2}{2\pi}\left[(d+b)\ln\left(1+\frac bd\right)-b\right]\end{aligned}$$

::: {.important}
$$L_{21}=\frac{\Lambda_{21}}{I_2}=\frac{\sqrt3\mu_0}{2\pi}\left[(d+b)\ln\left(1+\frac bd\right)-b\right]\qquad(\mathrm{H})$$
:::
:::
:::

## Magnetic Energy and Forces

```{.figure #m05-map-energy caption=""}
```

### Magnetic Energy

- Work is required to assemble a group of charges in place, and this work is stored as **electric energy**.
- In the same way we expect that work must be done to establish currents in conducting loops, and that this work is stored as **magnetic energy**.
- Consider a closed loop with self-inductance $L_1$ and initial current $i_1=0$.
    - A generator is connected to the loop and increases the current $i_1$ from zero to $I_1$.
    - In this process a changing magnetic flux passes through the loop. So by Faraday's law of induction an electromotive force is induced in the loop

$$v_1=\frac{d\Phi_1}{dt}=L_1\frac{di_1}{dt}$$

- By Lenz's law this electromotive force opposes the change of flux and current. Work must therefore be done to overcome it. This work is stored as magnetic energy

$$W_1=\int v_1i_1\,dt=L_1\int_0^{I_1}i_1\,di_1=\frac12L_1I_1^2$$

- Now consider two closed loops carrying the currents $i_1$ and $i_2$. The initial currents are zero, and they are increased to $I_1$ and $I_2$ respectively.
    - To find the work required (or the magnetic energy stored), first keep $i_2=0$ and increase $i_1$ from zero to $I_1$. This requires the work $W_1$.
    - Then keep $i_1$ at $I_1$ and increase $i_2$ from zero to $I_2$. Two kinds of work must be done.
        - the work $W_{22}$ to increase $i_2$ from zero to $I_2$

$$W_{22}=\frac12L_2I_2^2$$

- Because of the mutual coupling, part of the magnetic flux due to $i_2$ links the first loop. So by Faraday's law of induction an electromotive force is induced in the first loop.

$$v_{21}=\frac{d\Phi_{21}}{dt}=L_{21}\frac{di_2}{dt}$$

- By Lenz's law this electromotive force opposes the change of the flux linking the first loop, through a change in the current of the first loop. Work must therefore be done to overcome it

$$W_{21}=\int v_{21}I_1\,dt=L_{21}I_1\int_0^{I_2}di_2=L_{21}I_1I_2$$

- The total work done, or the total magnetic energy stored, is

$$\begin{aligned}W_2&=\frac12L_1I_1^2+L_{21}I_1I_2+\frac12L_2I_2^2\\&=\frac12\sum_{j=1}^2\sum_{k=1}^2L_{jk}I_jI_k\end{aligned}$$

- In general, for $N$ current loops

$$W_m=\frac12\sum_{j=1}^N\sum_{k=1}^NL_{jk}I_jI_k\qquad(\mathrm{J})$$

- The flux linking the $k$th loop

$$\Phi_k=\sum_{j=1}^NL_{jk}I_j$$

::: {.important}
$$W_m=\frac12\sum_{k=1}^NI_k\Phi_k\qquad(\mathrm{J})$$
:::

- It can be shown that the magnetic energy stored by a continuous current distribution in a volume is

::: {.important}
$$W_m=\frac12\int_{V'}\vect{A}\cdot\vect{J}\,dv'\qquad(\mathrm{J})$$
:::

- $V'$: the region containing $\vect{J}$, which may extend over all space
- It can be shown that the stored magnetic energy in terms of the field quantities is

::: {.important}
$$W_m=\frac12\int_{V'}\vect{H}\cdot\vect{B}\,dv'\qquad(\mathrm{J})$$
$$W_m=\frac12\int_{V'}\frac{B^2}{\mu}\,dv'\qquad(\mathrm{J})$$
$$W_m=\frac12\int_{V'}\mu H^2\,dv'\qquad(\mathrm{J})$$
:::

- $V'$: all space

::: {.remark}
It is often easier to determine the self-inductance from the stored magnetic energy in terms of $\vect{H}$ or $\vect{B}$ than from the flux linkage

$$W_m=\frac12\sum_{j=1}^N\sum_{k=1}^NL_{jk}I_jI_k$$

- For an inductor carrying a current $I$, with inductance $L$

$$W_m=\frac12LI^2$$
$$L=\frac{2W_m}{I^2}\qquad(\mathrm{H})$$
:::

::: {.example number="5-14"}
Using the stored magnetic energy, determine the inductance per unit length of an air coaxial transmission line with a solid inner conductor of radius $a$ and a very thin outer conductor of inner radius $b$.

::: {.solution}
- The energy stored per unit length in the inner conductor

$$B_{\phi1}=\frac{\mu_0Ir}{2\pi a^2}\quad\Longrightarrow\quad\begin{aligned}W'_{m1}&=\frac{1}{2\mu_0}\int_0^a\!\!\int_0^{2\pi}B_{\phi1}^2\,r\,dr\,d\phi\\&=\frac{\mu_0I^2}{4\pi a^4}\int_0^ar^3\,dr=\frac{\mu_0I^2}{16\pi}\qquad(\mathrm{J/m})\end{aligned}$$

- The energy stored per unit length in the region between the two conductors

$$B_{\phi2}=\frac{\mu_0I}{2\pi r}\quad\Longrightarrow\quad\begin{aligned}W'_{m2}&=\frac{1}{2\mu_0}\int_a^b\!\!\int_0^{2\pi}B_{\phi2}^2\,r\,dr\,d\phi\\&=\frac{\mu_0I^2}{4\pi}\int_a^b\frac1r\,dr=\frac{\mu_0I^2}{4\pi}\ln\frac ba\qquad(\mathrm{J/m})\end{aligned}$$

- Therefore

$$\begin{aligned}L'&=\frac{2}{I^2}\left(W'_{m1}+W'_{m2}\right)\\&=\frac{\mu_0}{8\pi}+\frac{\mu_0}{2\pi}\ln\frac ba\qquad(\mathrm{H/m})\end{aligned}$$
:::
:::

::: {.example number="5-15"}
For a very long solenoid with cross-section $S$, $n$ turns per unit length and an air core, find the inductance per unit length.

::: {.solution}
$$B=\mu_0nI\quad\Longrightarrow\quad W_m=\frac12\int_{V'}\frac{B^2}{\mu}\,dv'=\frac{1}{2\mu_0}\int\mu_0^2n^2I^2\,dv$$
$$=\frac12\mu_0n^2I^2S=\frac12LI^2\quad\Rightarrow\quad L'=\mu_0n^2S\qquad\mathrm{H/m}$$
:::
:::

### Magnetic Forces and Torques

- When a charge $q$ moves with velocity $\vect{u}$ in a magnetic field of flux density $\vect{B}$, a magnetic force $\vect{F}_m$ acts on it.

$$\vect{F}_m=q\vect{u}\times\vect{B}\qquad(\mathrm{N})$$

- Topics
    - the Hall effect,
    - forces and torques on current-carrying conductors.

### The Hall Effect

- Consider a conducting material of rectangular cross-section $d\times b$ in a uniform magnetic field $\vect{B}=\uvec{z}B_0$. A uniform direct current flows in the $y$ direction.

```{.figure #m05-hall caption=""}
```

$$\vect{J}=\uvec{y}J_0=Nq\vect{u}$$

- The charge carriers are electrons, and $q$ is negative

$$\vect{u}=-\uvec{y}u_0$$

- The magnetic force tends to move the electrons in the $+x$ direction and creates a transverse electric field. The process continues until the transverse field is strong enough to stop the drift of the electrons.
- In the steady state the net force on the charge carriers is zero.

$$\vect{E}_h+\vect{u}\times\vect{B}=0\quad\Longrightarrow\quad\vect{E}_h=-\vect{u}\times\vect{B}\quad\Longrightarrow\quad\begin{aligned}\vect{E}_h&=-(-\uvec{y}u_0)\times\uvec{z}B_0\\&=\uvec{x}u_0B_0\end{aligned}$$

- $\vect{E}_h$: the Hall field
- The Hall voltage

$$V_h=-\int_0^dE_h\,dx=u_0B_0d$$

- The Hall coefficient

$$E_x/J_yB_z=1/Nq$$

- This phenomenon is called the **Hall effect**.
- The Hall effect is used to measure magnetic fields.

### Forces and Torques on Current-Carrying Conductors

- The magnetic force on a differential element of a closed circuit with contour $C$, cross-section $S$ and current $I$, in a magnetic field of flux density $\vect{B}$

```{.figure #m05-force-element caption=""}
```

$$d\vect{F}_m=q\vect{u}\times\vect{B}$$
$$\begin{aligned}d\vect{F}_m&=-NeS\lvert d\ell\rvert\vect{u}\times\vect{B}\\&=+NeS\lvert\vect{u}\rvert\,\dif\vect{\ell}\times\vect{B}\end{aligned}$$

- $N$: the number of electrons per unit volume, and $e$: the charge of an electron
- $\dif\vect{\ell}$ is opposite to $\vect{u}$, and $NeS\lvert\vect{u}\rvert=I$

::: {.important}
$$d\vect{F}_m=I\,\dif\vect{\ell}\times\vect{B}\qquad(\mathrm{N})$$
:::

- The magnetic force on a closed circuit with contour $C$, cross-section $S$ and current $I$, in a magnetic field of flux density $\vect{B}$

::: {.important}
$$\vect{F}_m=I\oint_C\dif\vect{\ell}\times\vect{B}\qquad(\mathrm{N})$$
:::

- $\dif\vect{\ell}$: in the direction of the current

::: {.example number="5-16"}
Determine the force per unit length between two very long parallel conducting wires carrying the currents $I_1$ and $I_2$ in the same direction, as shown below.

```{.figure #m05-ex16 caption=""}
```

::: {.solution}
$$\vect{F}'_{12}=I_2\oint_{C_2}\dif\vect{\ell}_2\times\vect{B}_{12}=I_2\int_0^1dz\,\uvec{z}\times\left(-\uvec{x}\frac{\mu_0I_1}{2\pi d}\right)$$

::: {.important title="An attractive force"}
$$\vect{F}'_{12}=-\uvec{y}\frac{\mu_0I_1I_2}{2\pi d}\qquad(\mathrm{N/m})$$
:::
:::
:::

- Consider a circular loop of radius $b$ carrying a current $I$ in a uniform magnetic field of flux density $\vect{B}$

$$\vect{B}=\vect{B}_\perp+\vect{B}_\parallel$$

```{.figure #m05-loop-fields caption=""}
```

- $\vect{B}_\perp$ produces no net force to move the loop; it only tends to expand the loop (or, if the current is reversed, to contract it).
- Although the net force on the loop due to $\vect{B}_\parallel$ is zero, there is a torque that tends to rotate the loop about the $x$-axis so as to align the magnetic field produced by $I$ with the external field $\vect{B}_\parallel$.

$$\begin{aligned}d\vect{T}&=\uvec{x}(dF)2b\sin\phi\\&=\uvec{x}(I\,d\ell\,B_\parallel\sin\phi)2b\sin\phi\\&=\uvec{x}2Ib^2B_\parallel\sin^2\phi\,d\phi\end{aligned}$$
$$\begin{aligned}\vect{T}=\int d\vect{T}&=\uvec{x}2Ib^2B_\parallel\int_0^\pi\sin^2\phi\,d\phi\\&=\uvec{x}I(\pi b^2)B_\parallel\end{aligned}$$
$$\vect{m}=\uvec{n}I(\pi b^2)=\uvec{n}IS$$
$$\vect{T}=\vect{m}\times\vect{B}_\parallel=\vect{m}\times(\vect{B}_\parallel+\vect{B}_\perp)$$

::: {.important}
$$\vect{T}=\vect{m}\times\vect{B}\qquad(\mathrm{N\cdot m})$$
:::

- It can be shown that this relation holds for a planar loop of any shape, as long as it lies in a uniform magnetic field

::: {.example number="5-17"}
A rectangular loop in the $xy$-plane with sides $b_1$ and $b_2$ carries a current $I$ and lies in the uniform magnetic field $\vect{B}=\uvec{x}B_x+\uvec{y}B_y+\uvec{z}B_z$. Determine the force and the torque on the loop.

```{.figure #m05-ex17-perp caption=""}
```

::: {.solution}
$$\vect{B}_\perp=\uvec{z}B_z,\qquad\vect{B}_\parallel=\uvec{x}B_x+\uvec{y}B_y$$

- The normal component exerts the forces $Ib_1B_z$ on the sides (1) and (3) and $Ib_2B_z$ on the sides (2) and (4), toward the centre. $\ELto$ No torque is produced.
- The forces on the loop due to the component parallel to the plane

```{.figure #m05-ex17-par caption=""}
```

$$\begin{aligned}\vect{F}_1&=Ib_1\uvec{x}\times(\uvec{x}B_x+\uvec{y}B_y)\\&=\uvec{z}Ib_1B_y=-\vect{F}_3\end{aligned}$$
$$\begin{aligned}\vect{F}_2&=Ib_2(-\uvec{y})\times(\uvec{x}B_x+\uvec{y}B_y)\\&=\uvec{z}Ib_2B_x=-\vect{F}_4\end{aligned}$$
$$\left.\begin{aligned}&\vect{T}_{13}=\uvec{x}Ib_1b_2B_y\\&\vect{T}_{24}=-\uvec{y}Ib_1b_2B_x\end{aligned}\right\}\quad\begin{aligned}&\vect{T}=\vect{T}_{13}+\vect{T}_{24}=Ib_1b_2(\uvec{x}B_y-\uvec{y}B_x)\qquad(\mathrm{N\cdot m})\\&\vect{T}=\vect{m}\times(\uvec{x}B_x+\uvec{y}B_y)=\vect{m}\times\vect{B}\end{aligned}$$
:::
:::
