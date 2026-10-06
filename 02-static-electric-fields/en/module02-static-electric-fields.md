# Static Electric Fields

## Course Outline

```{.figure #m02-course-outline caption=""}
```

## Static Electric Fields

- In electrostatics the electric charges are at rest and the electric fields do not change with time.
    - In this case there are no magnetic fields.
- In introductory physics the development of electrostatics usually begins with Coulomb's experimental law for the force between two charges.
- In this course, instead of following the historical development of electrostatics, we introduce the subject by postulating the divergence and the curl of the electric field intensity in free space.

```{.figure #m02-map caption=""}
```

- What are the fundamental postulates of electrostatics from which the other relations and laws of the subject can be derived?
- How are Coulomb's and Gauss's laws derived from these postulates?
- How is the electric field of a point charge, of a number of discrete point charges and of a continuous charge distribution computed?

## Fundamental Postulates of Electrostatics in Free Space

- **Electric field intensity**
    - The force on a small test charge placed in the field, divided by the charge. $\ELto$ $\mathrm{N/C}$ (newtons per coulomb), equivalent to $\mathrm{V/m}$ (volts per metre)

::: {.definition}
$$\vect{E}=\lim_{q\to0}\frac{\vect{F}}{q}\qquad(\mathrm{V/m})$$
:::

- The electric field intensity is proportional to the force and in the same direction.
- The two fundamental postulates of electrostatics in free space

::: {.important}
$$\nabla\cdot\vect{E}=\frac{\rho}{\epsilon_0}\qquad\qquad \nabla\times\vect{E}=0$$
:::

- $\rho$: volume charge density $(\mathrm{C/m^3})$; $\epsilon_0$: permittivity of free space $(\mathrm{F/m})$
- $\vect{E}$ is not solenoidal unless $\rho=0$
- $\vect{E}$ is irrotational

- Integral form of the first equation $\ELto$ integration over an arbitrary volume $V$

$$\int_V\nabla\cdot\vect{E}\,dv=\frac{1}{\epsilon_0}\int_V\rho\,dv$$

- $\int_V\rho\,dv$: the total charge contained in the volume $V$ enclosed by the surface $S$
- Using the divergence theorem:

::: {.important}
$$\oint_S\vect{E}\cdot d\vect{s}=\frac{Q}{\epsilon_0}$$
:::

- This relation is a form of **Gauss's law**
    - The total outward flux of the electric field intensity through any closed surface equals the total charge enclosed in the surface divided by $\epsilon_0$.

- Integral form of the second equation $\ELto$ integration over an arbitrary open surface $S$

$$\int_S(\nabla\times\vect{E})\cdot d\vect{s}=0$$

- Using Stokes's theorem:

::: {.important}
$$\oint_C\vect{E}\cdot\dif\vect{\ell}=0$$
:::

- The scalar line integral of the static electric field intensity around any closed path is zero.
- The scalar product $\vect{E}\cdot\dif\vect{\ell}$ integrated over any path is the voltage along that path.
- This equation is an expression of **Kirchhoff's voltage law**
    - The algebraic sum of the voltage drops around any closed path is zero.

- The line integrals of the irrotational field $\vect{E}$ are independent of the path and depend only on the initial and final points.

```{.figure #m02-two-paths caption=""}
```

$$\oint_C\vect{E}\cdot\dif\vect{\ell}=0$$
$$\int_{C_1}\vect{E}\cdot\dif\vect{\ell}+\int_{C_2}\vect{E}\cdot\dif\vect{\ell}=0$$
$$\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}+\int_{P_2}^{P_1}\vect{E}\cdot\dif\vect{\ell}=0$$
$$\int_{\substack{P_1\\\text{Along }C_1}}^{P_2}\vect{E}\cdot\dif\vect{\ell}=-\int_{\substack{P_2\\\text{Along }C_2}}^{P_1}\vect{E}\cdot\dif\vect{\ell}$$
$$\int_{\substack{P_1\\\text{Along }C_1}}^{P_2}\vect{E}\cdot\dif\vect{\ell}=\int_{\substack{P_1\\\text{Along }C_2}}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

## Coulomb's Law

```{.figure #m02-map-coulomb caption=""}
```

- **The electric field intensity of a point charge $q$ in free space**
    - We consider a hypothetical spherical surface of radius $R$ centred at $q$.
    - Since a point charge has no preferred direction, we expect the field to be radial everywhere and its intensity to be constant over the spherical surface.

```{.figure #m02-point-charge caption=""}
```

- The electric field intensity on the spherical surface:

$$\vect{E}=E_R\uvec{R}$$
$$\oint_S\vect{E}\cdot d\vect{s}=\oint_S(\uvec{R}E_R)\cdot\uvec{R}\,ds=\frac{q}{\epsilon_0}$$
$$E_R\oint_S ds=E_R(4\pi R^2)=\frac{q}{\epsilon_0}$$

::: {.important}
$$\vect{E}=\uvec{R}E_R=\uvec{R}\frac{q}{4\pi\epsilon_0R^2}\qquad(\mathrm{V/m})$$
:::

- If the charge is not at the origin of the coordinate system

```{.figure #m02-offset-charge caption=""}
```

$$\vect{E}_P=\uvec{qP}\frac{q}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^2},\qquad \uvec{qP}=\frac{\vect{R}-\vect{R}'}{\abs{\vect{R}-\vect{R}'}}$$

::: {.important}
$$\vect{E}_P=\frac{q(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}\qquad(\mathrm{V/m})$$
:::

- When a point charge $q_2$ is placed in the electric field of another point charge $q_1$, the force acting on it is

::: {.important title="Mathematical statement of Coulomb's law"}
$$\vect{F}_{12}=q_2\vect{E}_{12}=\uvec{R}\frac{q_1q_2}{4\pi\epsilon_0R^2}\qquad(\mathrm{N})$$
:::

```{.figure #m02-two-charges caption=""}
```

- **The electric field intensity of a set of discrete charges**

::: {.important}
$$\vect{E}=\frac{1}{4\pi\epsilon_0}\sum_{k=1}^{n}\frac{q_k(\vect{R}-\vect{R}'_k)}{\abs{\vect{R}-\vect{R}'_k}^3}\qquad(\mathrm{V/m})$$
:::

```{.figure #m02-discrete-charges caption=""}
```

- **The electric field intensity of a continuous charge distribution**
    - The field of a differential charge $dq$ is

$$d\vect{E}=\frac{dq(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- Line charge distribution

$$dq=\rho_\ell\,d\ell'\qquad\qquad \vect{E}=\int_{L'}\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- Surface charge distribution

$$dq=\rho_s\,ds'\qquad\qquad \vect{E}=\int_{S'}\frac{\rho_s\,ds'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- Volume charge distribution

$$dq=\rho_v\,dv'\qquad\qquad \vect{E}=\int_{V'}\frac{\rho_v\,dv'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- **Steps in computing the electric field intensity of a continuous charge distribution**
    - Choosing an appropriate coordinate system
    - Correctly determining the differential element $d\ell'$, $ds'$ and $dv'$ (note that in these relations the magnitudes of the differential length and surface vectors are used)
    - Correctly determining the position vector of the field point $(\vect{R})$
    - Correctly determining the position vector of the source point $(\vect{R}')$
    - Evaluating the integral
        - Note that we integrate with respect to the primed coordinates.

::: {.example number="2-1"}
Determine the electric field intensity of an infinitely long straight line charge of uniform density $\rho_\ell$.

```{.figure #m02-ex1 caption=""}
```

::: {.solution}
$$\vect{E}=\int_{L'}\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- Choosing cylindrical coordinates

$$d\ell'=dz'\qquad \vect{R}=r\uvec{r}\qquad \vect{R}'=z'\uvec{z}$$
$$\vect{E}=\frac{\rho_\ell}{4\pi\epsilon_0}\int_{-\infty}^{\infty}\frac{r\uvec{r}-z'\uvec{z}}{(r^2+z'^2)^{3/2}}\,dz'$$

- It is intuitively clear that the field has no component along $z$.

$$\vect{E}=\uvec{r}E_r=\uvec{r}\frac{\rho_\ell r}{4\pi\epsilon_0}\int_{-\infty}^{\infty}\frac{dz'}{(r^2+z'^2)^{3/2}}$$
$$\vect{E}=\uvec{r}\frac{\rho_\ell}{2\pi\epsilon_0r}\qquad(\mathrm{V/m})$$
:::
:::

::: {.example number="2-2"}
A ring of radius $a$ carries a line charge density $\rho_\ell$. Find the electric field intensity on the axis of the ring at a distance $h$ from it.

```{.figure #m02-ex2 caption=""}
```

::: {.solution}
$$\vect{E}=\int_{L'}\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- Choosing cylindrical coordinates

$$d\ell'=a\,d\phi'\qquad \vect{R}=h\uvec{z}\qquad \vect{R}'=a\uvec{r'}$$
$$\vect{E}=\frac{\rho_\ell}{4\pi\epsilon_0}\int_0^{2\pi}\frac{h\uvec{z}-a\uvec{r'}}{(a^2+h^2)^{3/2}}\,a\,d\phi'$$

- It is intuitively clear that the field has no component along $r$.

$$\vect{E}=\frac{\rho_\ell ah}{4\pi\epsilon_0(a^2+h^2)^{3/2}}\uvec{z}\int_0^{2\pi}d\phi'=\frac{\rho_\ell ah}{2\epsilon_0(a^2+h^2)^{3/2}}\uvec{z}$$
:::
:::

::: {.example number="2-3"}
Determine the electric field intensity of an infinite planar charge with a uniform surface charge density $\rho_s$.

```{.figure #m02-ex3 caption=""}
```

::: {.solution}
$$\vect{E}=\int_{S'}\frac{\rho_s\,ds'(\vect{R}-\vect{R}')}{4\pi\epsilon_0\abs{\vect{R}-\vect{R}'}^3}$$

- Choosing cylindrical coordinates

$$ds'=r'\,dr'\,d\phi'\qquad \vect{R}=h\uvec{z}\qquad \vect{R}'=r'\uvec{r'}$$
$$\vect{E}=\frac{\rho_s}{4\pi\epsilon_0}\int_0^{2\pi}\!\!\int_0^{\infty}\frac{h\uvec{z}-r'\uvec{r'}}{(h^2+r'^2)^{3/2}}\,r'\,dr'\,d\phi'$$

- It is intuitively clear that the field has no component along $r$.

$$\vect{E}=\frac{\rho_sh\uvec{z}}{4\pi\epsilon_0}\int_0^{2\pi}\!\!\int_0^{\infty}\frac{r'\,dr'\,d\phi'}{(h^2+r'^2)^{3/2}}=\frac{\rho_s}{2\epsilon_0}\uvec{z}$$
:::
:::

## Gauss's Law

```{.figure #m02-map-gauss caption=""}
```

::: {.important}
$$\oint_S\vect{E}\cdot d\vect{s}=\frac{Q}{\epsilon_0}$$
:::

- $Q$: the total charge contained in the volume $V$ enclosed by the surface $S$
- The total outward flux of the electric field intensity through any closed surface equals the total charge enclosed in the surface divided by $\epsilon_0$.
- The surface $S$ can be any closed surface, chosen for convenience.

::: {.remark}
Gauss's law always holds, but in using it to determine the electric field intensity the following point must be observed.

- The basis of applying Gauss's law to determine the electric field intensity lies, first, in recognizing the conditions of symmetry and, second, in choosing an appropriate surface over which the normal component of $\vect{E}$ due to a given charge distribution is constant (the Gaussian surface).
:::

::: {.example number="2-4"}
Using Gauss's law, determine the electric field intensity of an infinitely long straight line charge of uniform density $\rho_\ell$ at a distance $r$ from it.

```{.figure #m02-ex4 caption=""}
```

::: {.solution}
$$\vect{E}=\uvec{r}E_r$$

- Choosing a cylinder of length $L$ and radius $r$ as the Gaussian surface
    - For the top and bottom faces: $\vect{E}\cdot d\vect{s}=0$
    - For the side surface: $d\vect{s}=\uvec{r}\,r\,d\phi\,dz$

$$\oint_S\vect{E}\cdot d\vect{s}=\int_0^L\!\!\int_0^{2\pi}E_r\,r\,d\phi\,dz=2\pi rLE_r$$
$$Q=\rho_\ell L\qquad 2\pi rLE_r=\frac{\rho_\ell L}{\epsilon_0}\qquad \vect{E}=\uvec{r}E_r=\uvec{r}\frac{\rho_\ell}{2\pi\epsilon_0r}$$
:::
:::

::: {.example number="2-5"}
Determine the electric field intensity of an infinite planar charge with a uniform surface charge density $\rho_s$.

```{.figure #m02-ex5 caption=""}
```

::: {.solution}
$$\vect{E}=\pm E_z\uvec{z}$$

- Choosing a box as the Gaussian surface
- For the top face

$$\vect{E}\cdot d\vect{s}=(\uvec{z}E_z)\cdot(\uvec{z}\,ds)=E_z\,ds$$

- For the bottom face

$$\vect{E}\cdot d\vect{s}=(-\uvec{z}E_z)\cdot(-\uvec{z}\,ds)=E_z\,ds$$

- For the side faces

$$\vect{E}\cdot d\vect{s}=0$$

- Therefore

$$\oint_S\vect{E}\cdot d\vect{s}=2E_z\int_A ds=2E_zA$$
$$Q=\rho_sA\qquad 2E_zA=\frac{\rho_sA}{\epsilon_0}$$

::: {.important}
$$\vect{E}=\uvec{z}E_z=\uvec{z}\frac{\rho_s}{2\epsilon_0},\qquad z>0$$
$$\vect{E}=-\uvec{z}E_z=-\uvec{z}\frac{\rho_s}{2\epsilon_0},\qquad z<0$$
:::
:::
:::

::: {.example number="2-6"}
Determine the field $\vect{E}$ of an electron cloud with volume charge density $\rho=-\rho_0$ in the region $0\leq R\leq b$ and $\rho=0$ in the region $R>b$.

```{.figure #m02-ex6 caption=""}
```

::: {.solution}
$$\vect{E}=\uvec{R}E_R$$

- (a) $0\leq R\leq b$
    - Choosing a sphere as the Gaussian surface

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_i}\vect{E}\cdot d\vect{s}=E_R\int_{S_i}ds=E_R4\pi R^2$$
$$Q=\int_V\rho\,dv=-\rho_0\int_V dv=-\rho_0\frac{4\pi}{3}R^3\qquad \vect{E}=-\uvec{R}\frac{\rho_0}{3\epsilon_0}R$$

- (b) $R\geq b$
    - Choosing a sphere as the Gaussian surface

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_o}\vect{E}\cdot d\vect{s}=E_R\int_{S_o}ds=E_R4\pi R^2$$
$$Q=-\rho_0\frac{4\pi}{3}b^3\qquad \vect{E}=-\uvec{R}\frac{\rho_0b^3}{3\epsilon_0R^2}$$
:::
:::

::: {.example number="2-7"}
A spherical charge distribution of radius $b$ has the following density. Find the electric field intensity at all points of space.
$$\rho_v=\begin{cases}\dfrac{\rho_0R}{b}&0\leq R\leq b\\[2mm]0&R>b\end{cases}$$

```{.figure #m02-ex7 caption=""}
```

::: {.solution}
$$\vect{E}=\uvec{R}E_R$$

- (a) $0\leq R\leq b$
    - Choosing a sphere as the Gaussian surface

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_i}\vect{E}\cdot d\vect{s}=E_R\int_{S_i}ds=E_R4\pi R^2$$
$$Q=\int_v\rho_v\,dv=\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^{R}\frac{\rho_0R}{b}R^2\sin\theta\,dR\,d\theta\,d\phi=\frac{\rho_0\pi R^4}{b}$$
$$\vect{E}=E_R\uvec{R}=\frac{\rho_0R^2}{4\epsilon_0b}\uvec{R}$$

- (b) $R\geq b$
    - Choosing a sphere as the Gaussian surface

$$d\vect{s}=\uvec{R}\,ds$$
$$\oint_{S_o}\vect{E}\cdot d\vect{s}=E_R\int_{S_o}ds=E_R4\pi R^2\qquad Q=\rho_0\pi b^3$$
$$\vect{E}=E_R\uvec{R}=\frac{\rho_0b^3}{4\epsilon_0R^2}\uvec{R}$$
:::
:::

## Electric Potential

```{.figure #m02-map-potential caption=""}
```

- What is the concept of the electric potential difference between two points and of the electric potential of a point?
- How is the electric potential of a point charge, of a number of discrete point charges and of a continuous charge distribution computed?
- How can the electric field intensity be computed from the electric potential, and what is the advantage of this over computing the electric field intensity directly?

- Suppose we want to move a point charge $q$, located in the electric field $\vect{E}$, by $d\ell$.

```{.figure #m02-move-charge caption=""}
```

- The force exerted on the charge by the electric field:
$$\vect{F}_E=q\vect{E}$$

- The magnitude of the component of this force along $d\ell$:
$$F_{EL}=\vect{F}_E\cdot\uvec{\ell}=q\vect{E}\cdot\uvec{\ell}$$

- The force that must be applied to the charge:
$$F_{apply}=-F_{EL}=-q\vect{E}\cdot\uvec{\ell}$$

- The work done in moving the charge by $d\ell$:
$$dW=F_{apply}\,d\ell=-q\vect{E}\cdot\dif\vect{\ell}$$

- The work done in moving the charge from point $P_1$ to point $P_2$:
$$W=-q\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

$$\nabla\times\vect{E}=0\Rightarrow\vect{E}=-\nabla V$$
$$\nabla V\cdot\uvec{\ell}=\frac{dV}{d\ell}$$
$$q=+1\,\mathrm{C}\qquad W=\int_{P_1}^{P_2}\nabla V\cdot\dif\vect{\ell}\quad\Longrightarrow\quad W=\int_{P_1}^{P_2}dV=V_2-V_1$$

::: {.definition title="Electric potential difference"}
The electric potential difference between two points is the work done by an external source in moving a unit positive charge from one point to the other.
$$V_2-V_1=-\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

- It does not depend on the path of integration
:::

- In many cases a reference point at infinity with zero potential is chosen, and the potential differences of the various points are expressed with respect to this reference point.

::: {.important}
$$V_P=-\int_{\infty}^{P}\vect{E}\cdot\dif\vect{\ell}$$
:::

::: {.remark title="Remark 1"}
The minus sign in the potential relation is needed for consistency with the fact that moving against the direction of the field increases the electric potential.
:::

::: {.remark title="Remark 2"}
The gradient of $V$ is normal to the surfaces of constant $V$; consequently the electric field lines are normal to the equipotential surfaces.
:::

- **The electric potential of a point charge $q$ at a distance $R$ from it**

```{.figure #m02-potential-point caption=""}
```

$$V=-\int_{\infty}^{R}\left(\frac{q}{4\pi\epsilon_0R^2}\uvec{R}\right)\cdot dR\,\uvec{R}=\frac{q}{4\pi\epsilon_0R}$$

- **The electric potential of $n$ discrete point charges**

$$V=\frac{1}{4\pi\epsilon_0}\sum_{k=1}^{n}\frac{q_k}{\abs{\vect{R}-\vect{R}'_k}}$$

- $\vect{R}$: position vector of the field point; $\vect{R}'_k$: position vectors of the source points

- **The electric potential of a continuous charge distribution**
    - Line charge distribution
$$V=\frac{1}{4\pi\epsilon_0}\int_{L'}\frac{\rho_\ell\,d\ell'}{\abs{\vect{R}-\vect{R}'}}$$

    - Surface charge distribution
$$V=\frac{1}{4\pi\epsilon_0}\int_{S'}\frac{\rho_s\,ds'}{\abs{\vect{R}-\vect{R}'}}$$

    - Volume charge distribution
$$V=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho_v\,dv'}{\abs{\vect{R}-\vect{R}'}}$$

::: {.example number="2-8"}
Find the electric potential and the electric field intensity of an electric dipole at an arbitrary point very far from it.

::: {.solution}
$$V=\frac{1}{4\pi\epsilon_0}\sum_{k=1}^{2}\frac{q_k}{\abs{\vect{R}-\vect{R}'_k}}=\frac{1}{4\pi\epsilon_0}\left[\frac{q}{\abs{\vect{R}-\vect{d}/2}}+\frac{-q}{\abs{\vect{R}+\vect{d}/2}}\right]$$

```{.figure #m02-ex8-dipole caption=""}
```

$$V=\frac{q}{4\pi\epsilon_0}\left(\frac{1}{R_+}-\frac{1}{R_-}\right)$$
$$\frac{1}{R_+}\cong\left(R-\frac{d}{2}\cos\theta\right)^{-1}\cong R^{-1}\left(1+\frac{d}{2R}\cos\theta\right)$$
$$\frac{1}{R_-}\cong\left(R+\frac{d}{2}\cos\theta\right)^{-1}\cong R^{-1}\left(1-\frac{d}{2R}\cos\theta\right)$$

- $\vect{p}=q\vect{d}$: the electric dipole moment vector

$$V=\frac{qd\cos\theta}{4\pi\epsilon_0R^2}\quad\overset{\vect{d}=d\uvec{z}}{\Longrightarrow}\quad V=\frac{q\vect{d}\cdot\uvec{R}}{4\pi\epsilon_0R^2}\quad\overset{\vect{p}=q\vect{d}}{\Longrightarrow}\quad V=\frac{\vect{p}\cdot\uvec{R}}{4\pi\epsilon_0R^2}$$
$$\begin{aligned}\vect{E}=-\nabla V&=-\uvec{R}\frac{\partial V}{\partial R}-\uvec{\theta}\frac{\partial V}{R\,\partial\theta}\\&=\frac{p}{4\pi\epsilon_0R^3}(\uvec{R}2\cos\theta+\uvec{\theta}\sin\theta)\end{aligned}$$

```{.figure #m02-ex8-field caption=""}
```
:::
:::

::: {.example number="2-9"}
Find the electric potential and the electric field intensity of a charged disk of radius $b$ with surface charge density $\rho_s$ on its axis.

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
Find the electric potential and the electric field intensity of a line charge of length $L$ and charge density $\rho_\ell$ along its extension.

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
A volume charge of density $\rho=-\rho_0$ exists in the region $0\leq R\leq b$. What is the electric potential at an arbitrary point inside this volume?

```{.figure #m02-ex11 caption=""}
```

::: {.solution}
$$\vect{E}=-\uvec{R}\frac{\rho_0}{3\epsilon_0}R,\qquad 0\leq R\leq b$$
$$\vect{E}=-\uvec{R}\frac{\rho_0b^3}{3\epsilon_0R^2},\qquad R\geq b$$
$$\begin{aligned}V=-\int_{\infty}^{R}\vect{E}\cdot\dif\vect{\ell}&=-\int_{\infty}^{b}\frac{-\rho_0b^3}{3\epsilon_0R^2}\uvec{R}\cdot dR\,\uvec{R}-\int_{b}^{R}\frac{-\rho_0R}{3\epsilon_0}\uvec{R}\cdot dR\,\uvec{R}\\&=-\frac{\rho_0b^2}{3\epsilon_0}-\frac{\rho_0}{6\epsilon_0}\left(b^2-R^2\right)\end{aligned}$$
:::
:::

## Behaviour of the Static Electric Field in Material Media

```{.figure #m02-map-media caption=""}
```

- Classification of materials according to their electrical properties
    - Conductors
    - Semiconductors
    - Insulators (dielectrics)
- In conductors the electrons of the outer shells of the atoms are held by a weak force and pass easily from one atom to another.
- But the electrons in the atoms of insulators are tightly bound to their orbits and under normal conditions cannot be detached.
- The electrical properties of semiconductors lie between those of conductors and insulators.

- How does the static electric field intensity behave in the presence of a conductor?
- How does the static electric field intensity behave in the presence of a dielectric?
- What is the concept of electric flux density, and how is it related to the electric field intensity?
- What is the concept of the dielectric constant?
- How does the static electric field intensity behave at the boundary between two different media?

## Conductors in Static Electric Field

- If we release charges inside a conductor, a field forms in it that drives the charges apart and to the surface.
    - Under static conditions the charge and the electric field inside a conductor are zero.
$$\rho=0\qquad \vect{E}=0$$

    - The time needed for the charges to distribute themselves on the surface of the conductor and reach equilibrium depends on the conductivity of the conductor.
- If under static conditions the electric field on the surface of a conductor had a tangential component, it would produce a tangential force, set the charges in motion, and there would be no charge equilibrium.
    - Therefore, under static conditions the electric field on the surface of a conductor is everywhere normal to the surface. In other words, under static conditions the surface of a conductor is an equipotential surface. In fact, since $\vect{E}=0$ at all points inside the conductor, the whole conductor has the same electric potential.

- **Boundary conditions at a conductor / free-space interface**

```{.figure #m02-conductor-boundary caption=""}
```

- Normal component:
$$\oint_S\vect{E}\cdot d\vect{s}=E_n\Delta S=\frac{\rho_s\Delta S}{\epsilon_0}\qquad\Longrightarrow\qquad E_n=\frac{\rho_s}{\epsilon_0}$$

- Tangential component:
$$\oint\vect{E}\cdot d\vect{L}=0$$
$$E_t\Delta w-E_{N,\text{at }b}\tfrac12\Delta h+E_{N,\text{at }a}\tfrac12\Delta h=0\qquad\Longrightarrow\qquad E_t=0$$

::: {.example number="2-12"}
A point charge $+Q$ is at the centre of a conducting spherical shell of inner radius $R_i$ and outer radius $R_o$. Find $\vect{E}$ and $V$ in all space.

```{.figure #m02-ex12 caption=""}
```

::: {.solution}
$$\vect{E}=E_R\uvec{R}$$

- For $R>R_o$

$$\oint_S\vect{E}\cdot d\vect{s}=E_{R1}4\pi R^2=\frac{Q}{\epsilon_0}$$
$$E_{R1}=\frac{Q}{4\pi\epsilon_0R^2}\qquad V_1=-\int_{\infty}^{R}(E_{R1})\,dR=\frac{Q}{4\pi\epsilon_0R}$$

- For $R_i<R<R_o$

$$E_{R2}=0\qquad V_2=V_1\Big|_{R=R_o}=\frac{Q}{4\pi\epsilon_0R_o}$$

- For $R<R_i$

$$E_{R3}=\frac{Q}{4\pi\epsilon_0R^2}$$
$$V_3=-\int_{\infty}^{R_o}E_{R1}\,dR-\int_{R_o}^{R_i}E_{R2}\,dR-\int_{R_i}^{R}E_{R3}\,dR$$
$$V_3=\frac{Q}{4\pi\epsilon_0}\left(\frac1R+\frac{1}{R_o}-\frac{1}{R_i}\right)$$

```{.figure #m02-ex12-plots caption=""}
```
:::
:::

## Dielectrics in Static Electric Field

- Ideal dielectrics have no free charges. As a result, their charge density and internal electric field are not zero, as they are in conductors.
- Dielectrics have **bound charges**; applying an external field to a dielectric creates electric dipoles and polarizes the dielectric material.
- The induced electric dipoles change the electric field inside and outside the dielectric material.

```{.figure #m02-polarization caption=""}
```

- **Equivalent charge distributions in polarized dielectrics**
    - To analyse the macroscopic effect of the induced dipoles, we define the polarization vector $\vect{P}$ as follows

::: {.definition}
$$\vect{P}=\lim_{\Delta v\to0}\frac{\sum_{k=1}^{n\Delta v}\vect{p}_k}{\Delta v}\qquad(\mathrm{C/m^2})$$

- $n$: number of dipoles per unit volume; $\vect{p}_k$: dipole moment
:::

- If $d\vect{p}$ is the dipole moment of a small volume $dv'$, then

$$d\vect{p}=\vect{P}\,dv'\qquad dV=\frac{\vect{P}\cdot\uvec{R}}{4\pi\epsilon_0R^2}\,dv'\qquad V=\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\vect{P}\cdot\uvec{R}}{R^2}\,dv'$$
$$V=\frac{1}{4\pi\epsilon_0}\oint_{S'}\frac{\vect{P}\cdot\vect{a}'_n}{R}\,ds'+\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{(-\nabla'\cdot\vect{P})}{R}\,dv'$$

- The electric potential, and hence the electric field intensity, of a polarized dielectric can be computed from the effect of two charge distributions, a surface one and a volume one, with the following densities, called the **polarization charge densities** or **bound charge densities**

::: {.important}
$$\rho_{ps}=\vect{P}\cdot\uvec{n}\qquad\qquad \rho_p=-\nabla\cdot\vect{P}$$
$$V=\frac{1}{4\pi\epsilon_0}\oint_{S'}\frac{\rho_{ps}}{R}\,ds'+\frac{1}{4\pi\epsilon_0}\int_{V'}\frac{\rho_p}{R}\,dv'$$
:::

::: {.remark}
Since we are dealing with an electrically neutral dielectric body, the total charge of the body after polarization must still be zero
$$\begin{aligned}\text{Total charge}&=\oint_S\rho_{ps}\,ds+\int_V\rho_p\,dv\\&=\oint_S\vect{P}\cdot\uvec{n}\,ds-\int_V\nabla\cdot\vect{P}\,dv=0\end{aligned}$$
:::

## Electric Flux Density

```{.figure #m02-map-flux caption=""}
```

- Since a dielectric gives rise to an equivalent volume charge density $\rho_p$, we expect the electric field intensity due to a given charge distribution in a dielectric to differ from the electric field intensity in free space.

$$\nabla\cdot\vect{E}=\frac{1}{\epsilon_0}(\rho+\rho_p)$$
$$\nabla\cdot(\epsilon_0\vect{E}+\vect{P})=\rho$$

- The electric flux density or electric displacement $\vect{D}$ is defined as follows

::: {.definition}
$$\vect{D}=\epsilon_0\vect{E}+\vect{P}\qquad(\mathrm{C/m^2})$$
:::

- Using the vector $\vect{D}$, the relation between the electric field and the free charge distributions in any medium can be written without having to deal with the polarization vector $\vect{P}$ or the polarization charge densities.

::: {.important}
$$\nabla\cdot\vect{D}=\rho\qquad(\mathrm{C/m^3})$$
:::

- Integral form

$$\int_V\nabla\cdot\vect{D}\,dv=\int_V\rho\,dv$$

::: {.important title="Another form of Gauss's law"}
$$\oint_S\vect{D}\cdot d\vect{s}=Q\qquad(\mathrm{C})$$
:::

- The fundamental equations of electrostatics in any medium

::: {.important}
$$\begin{cases}\nabla\cdot\vect{D}=\rho\\\nabla\times\vect{E}=0\end{cases}$$
:::

## Dielectric Constant

- The relation between the polarization vector and the electric field intensity

$$\vect{P}=\epsilon_0\chi_e\vect{E}$$

- $\chi_e$: electric susceptibility

- The relation between the electric field intensity and the electric flux density

::: {.important}
$$\begin{aligned}\vect{D}&=\epsilon_0(1+\chi_e)\vect{E}\\&=\epsilon_0\epsilon_r\vect{E}=\epsilon\vect{E}\qquad(\mathrm{C/m^2})\end{aligned}$$
:::

$$\epsilon_r=1+\chi_e=\frac{\epsilon}{\epsilon_0}$$

- $\epsilon_r$: a dimensionless constant called the relative permittivity or dielectric constant

- A dielectric medium is **linear** if $\epsilon_r$ is independent of $\vect{E}$, **homogeneous** if $\epsilon_r$ is independent of the space coordinates, and isotropic if $\epsilon_r$ is a scalar.
    - A linear, homogeneous and isotropic medium is called a simple medium.
    - In anisotropic media the dielectric constant is a matrix. In such media $\vect{D}$ and $\vect{E}$ are not necessarily in the same direction.

::: {.example number="2-13"}
A point charge $+Q$ is at the centre of a dielectric spherical shell of inner radius $R_i$ and outer radius $R_o$. The dielectric constant of the shell is $\epsilon_r$. Find $\vect{E}$, $V$, $\vect{D}$ and $\vect{P}$ in all space.

```{.figure #m02-ex13 caption=""}
```

::: {.solution}
$$\vect{E}=E_R\uvec{R}$$

- For $R>R_o$

$$E_{R1}=\frac{Q}{4\pi\epsilon_0R^2}\qquad V_1=\frac{Q}{4\pi\epsilon_0R}$$
$$D_{R1}=\epsilon_0E_{R1}=\frac{Q}{4\pi R^2}\qquad P_{R1}=0$$

- For $R_i<R<R_o$

$$D_{R2}=\frac{Q}{4\pi R^2}$$
$$E_{R2}=\frac{Q}{4\pi\epsilon_0\epsilon_rR^2}=\frac{Q}{4\pi\epsilon R^2}$$
$$P_{R2}=\left(1-\frac{1}{\epsilon_r}\right)\frac{Q}{4\pi R^2}$$
$$\begin{aligned}V_2&=-\int_{\infty}^{R_o}E_{R1}\,dR-\int_{R_o}^{R}E_{R2}\,dR\\&=V_1\Big|_{R=R_o}-\frac{Q}{4\pi\epsilon}\int_{R_o}^{R}\frac{1}{R^2}\,dR\\&=\frac{Q}{4\pi\epsilon_0}\left[\left(1-\frac{1}{\epsilon_r}\right)\frac{1}{R_o}+\frac{1}{\epsilon_rR}\right]\end{aligned}$$

- For $R<R_i$

$$E_{R3}=\frac{Q}{4\pi\epsilon_0R^2}\qquad D_{R3}=\frac{Q}{4\pi R^2}\qquad P_{R3}=0$$
$$\begin{aligned}V_3&=V_2\Big|_{R=R_i}-\int_{R_i}^{R}E_{R3}\,dR\\&=\frac{Q}{4\pi\epsilon_0}\left[\left(1-\frac{1}{\epsilon_r}\right)\frac{1}{R_o}-\left(1-\frac{1}{\epsilon_r}\right)\frac{1}{R_i}+\frac{1}{R}\right]\end{aligned}$$

$$\begin{aligned}\rho_{ps}\Big|_{R=R_i}&=\vect{P}\cdot(-\uvec{R})\Big|_{R=R_i}=-P_{R2}\Big|_{R=R_i}\\&=-\left(1-\frac{1}{\epsilon_r}\right)\frac{Q}{4\pi R_i^2}\end{aligned}$$
$$\begin{aligned}\rho_{ps}\Big|_{R=R_o}&=\vect{P}\cdot\uvec{R}\Big|_{R=R_o}=P_{R2}\Big|_{R=R_o}\\&=\left(1-\frac{1}{\epsilon_r}\right)\frac{Q}{4\pi R_o^2}\end{aligned}$$
$$\begin{aligned}\rho_p&=-\nabla\cdot\vect{P}\\&=-\frac{1}{R^2}\frac{\partial}{\partial R}(R^2P_{R2})=0\end{aligned}$$
:::
:::

## Dielectric Strength

- An external electric field causes small displacements of the bound charges and creates electric dipoles.
- If the electric field is strong, it completely detaches electrons from the molecules, accelerates them and makes them collide with the molecular lattice structure.
- In this case the material may become conducting and large currents may arise.
    - This phenomenon is called **dielectric breakdown**.
- The maximum electric field intensity that a dielectric material can withstand without breakdown is called the **dielectric strength** of the material.
    - For example, the dielectric strength of air is $3\,\mathrm{kV/mm}$.

::: {.example number="2-14"}
When a coaxial cable is used to carry electric power, the radius of the inner conductor is determined by the load current, and the overall size by the voltage and the insulating material used. Suppose that the radius of the inner conductor is $0.4\,\mathrm{cm}$ and that two layers, rubber with relative permittivity $\epsilon_{rr}=3.2$ and polystyrene with relative permittivity $\epsilon_{rp}=2.6$, are used as the insulating material. Design this cable so that it can operate at a voltage of $20\,\mathrm{kV}$. To avoid breakdown due to abnormal external conditions, the maximum electric field intensity in the insulating materials must not exceed 25\% of their dielectric strengths. (The dielectric strength of rubber is $25\times10^6\,\mathrm{V/m}$ and that of polystyrene is $20\times10^6\,\mathrm{V/m}$.)

```{.figure #m02-ex14 caption=""}
```

::: {.solution}
- The aim is to determine the order of the insulating layers and the values of $r_o$ and $r_m$.
- Assuming that the free charge density on the surface of the inner conductor is $\rho_s$, Gauss's law gives

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

## Boundary Conditions for Static Electric Fields

```{.figure #m02-map-boundary caption=""}
```

```{.figure #m02-boundary caption=""}
```

- Tangential component:

$$\oint_{abcda}\vect{E}\cdot\dif\vect{\ell}=\vect{E}_1\cdot\Delta\vect{w}+\vect{E}_2\cdot(-\Delta\vect{w})=E_{1t}\Delta w-E_{2t}\Delta w=0$$

::: {.important}
$$E_{1t}=E_{2t}\qquad\qquad \frac{D_{1t}}{\epsilon_1}=\frac{D_{2t}}{\epsilon_2}$$
:::

- Normal component:

$$\begin{aligned}\oint_S\vect{D}\cdot d\vect{s}&=(\vect{D}_1\cdot\uvec{n2}+\vect{D}_2\cdot\uvec{n1})\Delta S\\&=\uvec{n2}\cdot(\vect{D}_1-\vect{D}_2)\Delta S\\&=\rho_s\Delta S\end{aligned}$$

::: {.important}
$$\uvec{n2}\cdot(\vect{D}_1-\vect{D}_2)=\rho_s\qquad\qquad \uvec{n2}\cdot(\epsilon_1\vect{E}_1-\epsilon_2\vect{E}_2)=\rho_s$$
:::

::: {.example number="2-15"}
Two dielectric media with permittivities $\epsilon_1$ and $\epsilon_2$ are separated by a charge-free boundary as shown in the figure below. The electric field intensity in medium 1 at the point $P_1$ has magnitude $E_1$ and makes an angle $\alpha_1$ with the normal. Determine the magnitude and direction of the electric field intensity at the point $P_2$ in region 2.

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

## Capacitance and Capacitors

```{.figure #m02-map-cap caption=""}
```

- What kind of element is a capacitor, and what is the concept of capacitance?
- How is the capacitance of various structures computed?
- How can the electric energy stored in a set of charges, or the work needed to assemble a set of charges, be found?
- How can the electric energy stored in capacitive structures be computed?

- Suppose a charge $Q$ is placed on an arbitrary conductor. This charge distributes itself over the surface of the conductor and forms the charge density $\rho_s$.
- Increasing the total charge by a factor $k$ increases the charge density $\rho_s$ by the factor $k$, and consequently the potential due to this charge also increases by the factor $k$.
    - Therefore the ratio of $Q$ to $V$ remains constant

::: {.important}
$$Q=CV$$
:::

- The constant of proportionality $(C)$ is called the **capacitance of the isolated conducting body**; it is the electric charge that must be added to the body to raise its electric potential by one unit.
    - Its unit is the coulomb per volt, or farad $(\mathrm{F})$.

- Two conductors separated by free space or by a dielectric medium are called a capacitor.

```{.figure #m02-capacitor caption=""}
```

- The capacitance of a capacitor is defined as follows

::: {.definition}
$$C=\frac{Q}{V_{12}}\qquad(\mathrm{F})$$
:::

- The capacitance of a capacitor depends on its geometry and on the permittivity of the medium between the two conductors.
- Procedure for computing the capacitance of a capacitor
    - Choosing an appropriate coordinate system
    - Placing the charges $+Q$ and $-Q$ on the conductors
    - Finding $\vect{E}$ from $Q$
    - Computing the potential difference between the two conductors from the following relation, from the charge $-Q$ to the charge $+Q$
$$V=-\int_{P_{-Q}}^{P_{+Q}}\vect{E}\cdot\dif\vect{\ell}$$
    - Finding the capacitance from the ratio $Q/V$

::: {.example number="2-16"}
A parallel-plate capacitor consists of two parallel conducting plates of area $S$ separated by $d$. The space between the plates is filled with a dielectric of constant permittivity $\epsilon$. Find the capacitance of this capacitor.

```{.figure #m02-ex16 caption=""}
```

::: {.solution}
- Using Cartesian coordinates
- Placing the charges $+Q$ and $-Q$ on the plates $\ELto$ $\rho_s=\dfrac{Q}{S}$
- Computing the electric field intensity in the space between the two conducting plates with Gauss's law, neglecting the fringing fields

$$\vect{E}=-\uvec{y}\frac{\rho_s}{\epsilon}=-\uvec{y}\frac{Q}{\epsilon S}$$

- Computing the potential difference between the conducting plates in terms of $Q$

$$V_{12}=-\int_{y=0}^{y=d}\vect{E}\cdot\dif\vect{\ell}=-\int_0^d\left(-\uvec{y}\frac{Q}{\epsilon S}\right)\cdot(\uvec{y}\,dy)=\frac{Q}{\epsilon S}d$$

- Determining the capacitance

$$C=\frac{Q}{V_{12}}=\epsilon\frac{S}{d}$$
:::
:::

::: {.example number="2-17"}
A cylindrical capacitor consists of an inner conductor of radius $a$ and an outer conductor of radius $b$. The space between the two conductors is filled with a dielectric of constant permittivity $\epsilon$, and the length of the capacitor is $L$. Find the capacitance of this capacitor.

```{.figure #m02-ex17 caption=""}
```

::: {.solution}
- Using cylindrical coordinates
- Placing the charges $+Q$ and $-Q$ on the inner and outer conductors respectively
- Computing the electric field intensity in the space between the two conductors with Gauss's law

$$\vect{E}=\uvec{r}E_r=\uvec{r}\frac{Q}{2\pi\epsilon Lr}$$

- Computing the potential difference between the conductors in terms of $Q$

$$\begin{aligned}V_{ab}&=-\int_{r=b}^{r=a}\vect{E}\cdot\dif\vect{\ell}=-\int_b^a\left(\uvec{r}\frac{Q}{2\pi\epsilon Lr}\right)\cdot(\uvec{r}\,dr)\\&=\frac{Q}{2\pi\epsilon L}\ln\left(\frac ba\right)\end{aligned}$$

- Determining the capacitance

$$C=\frac{Q}{V_{ab}}=\frac{2\pi\epsilon L}{\ln\left(\dfrac ba\right)}$$
:::
:::

::: {.example number="2-18"}
A spherical capacitor consists of an inner conducting sphere of radius $R_i$ and an outer conducting sphere of radius $R_o$. The space between the two conductors is filled with a dielectric of constant permittivity $\epsilon$. Determine the capacitance of this capacitor.

```{.figure #m02-ex18 caption=""}
```

::: {.solution}
- Using spherical coordinates
- Placing the charges $+Q$ and $-Q$ on the inner and outer conductors respectively
- Computing the electric field intensity in the space between the two conductors with Gauss's law

$$\vect{E}=\uvec{R}E_R=\uvec{R}\frac{Q}{4\pi\epsilon R^2}$$

- Computing the potential difference between the conductors in terms of $Q$

$$V=-\int_{R_o}^{R_i}\vect{E}\cdot(\uvec{R}\,dR)=-\int_{R_o}^{R_i}\frac{Q}{4\pi\epsilon R^2}\,dR=\frac{Q}{4\pi\epsilon}\left(\frac{1}{R_i}-\frac{1}{R_o}\right)$$

- Determining the capacitance

$$C=\frac QV=\frac{4\pi\epsilon}{\dfrac{1}{R_i}-\dfrac{1}{R_o}}$$
:::
:::

- **Capacitors connected in parallel**

```{.figure #m02-parallel caption=""}
```

$$\begin{aligned}Q&=Q_1+Q_2+\cdots+Q_n\\&=C_1V+C_2V+\cdots+C_nV=C_{\parallel}V\end{aligned}$$

::: {.important}
$$C_{\parallel}=C_1+C_2+\cdots+C_n$$
:::

- **Capacitors connected in series**

```{.figure #m02-series caption=""}
```

$$V=\frac{Q}{C_{sr}}=\frac{Q}{C_1}+\frac{Q}{C_2}+\cdots+\frac{Q}{C_n}$$

::: {.important}
$$\frac{1}{C_{sr}}=\frac{1}{C_1}+\frac{1}{C_2}+\cdots+\frac{1}{C_n}$$
:::

::: {.example number="2-19"}
A cylindrical capacitor of length $L$ is formed by coaxial cylindrical conducting surfaces of radii $r_i$ and $r_o$. Two dielectric materials of permittivities $\epsilon_1$ and $\epsilon_2$ fill the space between the conductors as shown in the figure below. Determine the capacitance of this capacitor.

```{.figure #m02-ex19 caption=""}
```

::: {.solution}
- **First method**
    - The capacitance of a cylindrical capacitor $\ELto$ $C=\dfrac{2\pi\epsilon L}{\ln\left(\dfrac{r_o}{r_i}\right)}$
    - Since each dielectric fills half of the space, the capacitance of each half is

$$C_1=\frac{\pi\epsilon_1L}{\ln\left(\dfrac{r_o}{r_i}\right)}\qquad\qquad C_2=\frac{\pi\epsilon_2L}{\ln\left(\dfrac{r_o}{r_i}\right)}$$

- Since the two capacitors $C_1$ and $C_2$ are in parallel, the total capacitance is

$$C=C_1+C_2=\frac{2\pi L}{\ln\left(\dfrac{r_o}{r_i}\right)}\left(\frac{\epsilon_1+\epsilon_2}{2}\right)$$

- **Second method**
    - Using cylindrical coordinates
    - Placing the charges $+Q$ and $-Q$ on the inner and outer conductors respectively
    - Computing the electric field intensity in the space between the two conductors with Gauss's law

```{.figure #m02-ex19-gauss caption=""}
```

$$\left.\begin{aligned}E_{r1}&=\frac{Q_1}{\pi r\epsilon_1L}\\E_{r2}&=\frac{Q_2}{\pi r\epsilon_2L}\end{aligned}\right\}\ \overset{E_{r1}=E_{r2}}{\Longrightarrow}\ \left.\begin{aligned}\frac{Q_1}{\epsilon_1}&=\frac{Q_2}{\epsilon_2}\\Q_1+Q_2&=Q\end{aligned}\right\}\ \begin{cases}Q_1=\dfrac{Q\epsilon_1}{\epsilon_1+\epsilon_2}\\[3mm]Q_2=\dfrac{Q\epsilon_2}{\epsilon_1+\epsilon_2}\end{cases}$$

- Computing the potential difference between the conductors in terms of $Q$

$$V=-\int_{r_o}^{r_i}\frac{Q_1}{\pi r\epsilon_1L}\,dr=-\int_{r_o}^{r_i}\frac{Q}{\pi rL(\epsilon_1+\epsilon_2)}\,dr=\frac{Q}{\pi L(\epsilon_1+\epsilon_2)}\ln\left(\frac{r_o}{r_i}\right)$$

- Determining the capacitance

$$C=\frac{2\pi L}{\ln\left(\dfrac{r_o}{r_i}\right)}\left(\frac{\epsilon_1+\epsilon_2}{2}\right)$$
:::
:::

::: {.example number="2-20"}
A capacitor is formed by two concentric conducting spherical shells of radii $R_i$ and $R_o$. The space between the shells is filled with a dielectric of relative permittivity $\epsilon_r$ from $R_i$ to $b$ and a dielectric of relative permittivity $2\epsilon_r$ from $b$ to $R_o$. Determine the capacitance of this capacitor.

```{.figure #m02-ex20 caption=""}
```

::: {.solution}
- **First method**
    - The capacitance of a spherical capacitor $\ELto$ $C=\dfrac QV=\dfrac{4\pi\epsilon}{\dfrac{1}{R_i}-\dfrac{1}{R_o}}$
    - This capacitor can be regarded as two capacitors in series, as follows

$$C_1=\frac{4\pi\epsilon_0\epsilon_r}{\dfrac{1}{R_i}-\dfrac1b}\qquad\qquad C_2=\frac{4\pi\epsilon_0(2\epsilon_r)}{\dfrac1b-\dfrac{1}{R_o}}$$

- Therefore the total capacitance is

$$C=\frac{1}{1/C_1+1/C_2}=\frac{4\pi\epsilon_0\epsilon_r}{\dfrac{1}{R_i}-\dfrac{1}{2b}-\dfrac{1}{2R_o}}$$

- **Second method**
    - Using spherical coordinates
    - Placing the charges $+Q$ and $-Q$ on the inner and outer conductors respectively
    - Computing the electric field intensity in the space between the two conductors with Gauss's law

$$E_{R1}=\frac{Q}{4\pi\epsilon_0\epsilon_rR^2}\qquad\qquad E_{R2}=\frac{Q}{4\pi\epsilon_0(2\epsilon_r)R^2}$$

- Computing the potential difference between the conductors in terms of $Q$

$$V=-\int_{R_o}^{b}\frac{Q}{4\pi\epsilon_0(2\epsilon_r)R^2}\,dR-\int_{b}^{R_i}\frac{Q}{4\pi\epsilon_0\epsilon_rR^2}\,dR=\frac{Q}{4\pi\epsilon_0\epsilon_r}\left(\frac{1}{R_i}-\frac{1}{2b}-\frac{1}{2R_o}\right)$$

- Determining the capacitance

$$C=\frac{4\pi\epsilon_0\epsilon_r}{\dfrac{1}{R_i}-\dfrac{1}{2b}-\dfrac{1}{2R_o}}$$
:::
:::

## Electrostatic Energy

```{.figure #m02-map-energy caption=""}
```

- The electric potential of a point in an electric field is equal to the work needed to bring a unit positive charge from infinity (the zero-potential reference) to that point.
- To bring a charge $Q_2$ from infinity to the distance $R_{12}$ from the charge $Q_1$, the work needed is

```{.figure #m02-energy-two caption=""}
```

$$W_2=Q_2V_2=Q_2\frac{Q_1}{4\pi\epsilon_0R_{12}}$$

- $V_2$: the potential at the location of the charge $Q_2$

$$W_2=Q_1\frac{Q_2}{4\pi\epsilon_0R_{12}}=Q_1V_1$$
$$W_2=\tfrac12(Q_1V_1+Q_2V_2)$$

- This work is stored in the system of two charges as potential energy.

- Now suppose another charge $Q_3$ is brought from infinity to a point at the distance $R_{13}$ from $Q_1$ and $R_{23}$ from $Q_2$; the additional work needed is

```{.figure #m02-energy-three caption=""}
```

$$\Delta W=Q_3V_3=Q_3\left(\frac{Q_1}{4\pi\epsilon_0R_{13}}+\frac{Q_2}{4\pi\epsilon_0R_{23}}\right)$$

- $V_3$: the potential at the location of the charge $Q_3$
- Thus the potential energy stored in the system of three charges is

$$W_3=W_2+\Delta W=\frac{1}{4\pi\epsilon_0}\left(\frac{Q_1Q_2}{R_{12}}+\frac{Q_1Q_3}{R_{13}}+\frac{Q_2Q_3}{R_{23}}\right)$$
$$\begin{aligned}W_3=\frac12\bigg[&Q_1\left(\frac{Q_2}{4\pi\epsilon_0R_{12}}+\frac{Q_3}{4\pi\epsilon_0R_{13}}\right)+Q_2\left(\frac{Q_1}{4\pi\epsilon_0R_{12}}+\frac{Q_3}{4\pi\epsilon_0R_{23}}\right)\\&+Q_3\left(\frac{Q_1}{4\pi\epsilon_0R_{13}}+\frac{Q_2}{4\pi\epsilon_0R_{23}}\right)\bigg]=\tfrac12(Q_1V_1+Q_2V_2+Q_3V_3)\end{aligned}$$

- Thus the potential energy of $N$ discrete point charges at rest is

::: {.important}
$$W_e=\frac12\sum_{k=1}^{N}Q_kV_k\qquad(\mathrm{J})$$
:::

- where $V_k$ is the electric potential at the point of $Q_k$ due to the other charges.
- The $\mathrm{SI}$ unit of energy is the joule, which is a large unit. Here another unit, the electron-volt $(\mathrm{eV})$, is used.
    - One electron-volt is the energy or work needed to move an electron against a potential difference of one volt.

$$1\,(\mathrm{eV})=(1.60\times10^{-19})\times1=1.60\times10^{-19}\qquad(\mathrm{J})$$

- In a continuous charge distribution of density $\rho$ the stored energy is

::: {.important}
$$W_e=\tfrac12\int_{V'}\rho V\,dv\qquad(\mathrm{J})$$
:::

- where $V$ is the potential at the point where the volume charge density is $\rho$, and $V'$ is the volume of the region in which $\rho$ exists.

::: {.example number="2-21"}
Find the energy required to assemble a uniformly charged sphere of radius $b$ and volume charge density $\rho$.

::: {.solution}
$$W_e=\frac\rho2\int_{V'}V\,dv=\frac\rho2\int_0^bV\,4\pi R^2\,dR$$
$$\vect{E}_{R1}=\uvec{R}\frac{Q}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho b^3}{3\epsilon_0R^2},\qquad R\geq b$$
$$\vect{E}_{R2}=\uvec{R}\frac{Q_R}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho R}{3\epsilon_0},\qquad 0<R\leq b$$
$$\begin{aligned}V&=-\int_{\infty}^{R}\vect{E}\cdot d\vect{R}=-\left[\int_{\infty}^{b}E_{R1}\,dR+\int_b^RE_{R2}\,dR\right]\\&=-\left[\int_{\infty}^{b}\frac{\rho b^3}{3\epsilon_0R^2}\,dR+\int_b^R\frac{\rho R}{3\epsilon_0}\,dR\right]\\&=\frac{\rho}{3\epsilon_0}\left(b^2+\frac{b^2}{2}-\frac{R^2}{2}\right)=\frac{\rho}{3\epsilon_0}\left(\frac32b^2-\frac{R^2}{2}\right)\end{aligned}$$
$$W_e=\frac\rho2\int_0^b\frac{\rho}{3\epsilon_0}\left(\frac32b^2-\frac{R^2}{2}\right)4\pi R^2\,dR=\frac{4\pi\rho^2b^5}{15\epsilon_0}$$
:::
:::

- Earlier we obtained the electrostatic energy of a charge distribution in terms of the charge density and the potential.
- Sometimes it is better to express this energy in terms of field quantities.
- It can be shown that

::: {.important}
$$W_e=\tfrac12\int_{V'}\vect{D}\cdot\vect{E}\,dv\qquad(\mathrm{J})$$
$$W_e=\tfrac12\int_{V'}\epsilon E^2\,dv\qquad(\mathrm{J})$$
$$W_e=\tfrac12\int_{V'}\frac{D^2}{\epsilon}\,dv\qquad(\mathrm{J})$$
:::

- $V'$: all space

::: {.example number="2-22"}
Solve Example \ELnumc{2-21} using the expression of the energy in terms of field quantities.

::: {.solution}
$$\vect{E}_{R1}=\uvec{R}\frac{Q}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho b^3}{3\epsilon_0R^2},\qquad R\geq b$$
$$\vect{E}_{R2}=\uvec{R}\frac{Q_R}{4\pi\epsilon_0R^2}=\uvec{R}\frac{\rho R}{3\epsilon_0},\qquad 0<R\leq b$$
$$\begin{aligned}W_e=\frac12\epsilon_0\int_{V'}\abs{\vect{E}}^2\,dv&=\frac12\epsilon_0\int_0^b\left(\frac{\rho R}{3\epsilon_0}\right)^24\pi R^2\,dR\\&\quad+\frac12\epsilon_0\int_b^{\infty}\left(\frac{\rho b^3}{3\epsilon_0R^2}\right)^24\pi R^2\,dR=\frac{4\pi\rho^2b^5}{15\epsilon_0}\end{aligned}$$
:::
:::

::: {.example number="2-23"}
In the figure below a parallel-plate capacitor of area $S$ and plate separation $d$ is charged by the voltage $V$. The permittivity of the insulator is $\epsilon$. Find the stored energy.

```{.figure #m02-ex23 caption=""}
```

::: {.solution}
$$E=\frac Vd$$
$$W_e=\frac12\int_{V'}\epsilon\left(\frac Vd\right)^2dv=\frac12\epsilon\left(\frac Vd\right)^2(Sd)=\frac12\left(\epsilon\frac Sd\right)V^2$$

::: {.important}
$$W_e=\tfrac12CV^2\quad(\mathrm{J})\qquad\qquad W_e=\tfrac12QV\quad(\mathrm{J})\qquad\qquad W_e=\frac{Q^2}{2C}\quad(\mathrm{J})$$
:::

::: {.remark}
It can be proved that the above equations hold for any capacitor made of two conductors.
:::
:::
:::

::: {.example number="2-24"}
Using the energy relation, find the capacitance of a cylindrical capacitor of length $L$ consisting of an inner conductor of radius $a$ and an outer conductor of radius $b$, with permittivity $\epsilon$.

::: {.solution}
$$\vect{E}=\uvec{r}E_r=\uvec{r}\frac{Q}{2\pi\epsilon Lr},\qquad a<r<b$$
$$\begin{aligned}W_e&=\frac12\int_a^b\epsilon\left(\frac{Q}{2\pi\epsilon Lr}\right)^2(L2\pi r\,dr)\\&=\frac{Q^2}{4\pi\epsilon L}\int_a^b\frac{dr}{r}=\frac{Q^2}{4\pi\epsilon L}\ln\frac ba\end{aligned}$$
$$\frac{Q^2}{2C}=\frac{Q^2}{4\pi\epsilon L}\ln\frac ba\qquad\Longrightarrow\qquad C=\frac{2\pi\epsilon L}{\ln\dfrac ba}$$
:::
:::

```{.figure #m02-map-end caption=""}
```
