# Solution of Electrostatic Problems

## Course Outline

```{.figure #m03-course-outline caption=""}
```

## Solution of Electrostatic Problems

- Electrostatic problems are problems that deal with the effects of electric charges at rest. Solving such problems usually involves determining the electric potential, the electric field intensity or the electric charge distribution.
- If the charge distribution is given, both the potential and the electric field can be computed with the relations of the previous chapter.
    - In many practical problems the exact charge distribution is not known everywhere, and finding the potential and the electric field directly with the formulas of the previous chapter is not possible. $\ELto$ the method of images can be used for a particular class of problems
    - In another kind of problem the potentials of all conducting bodies are known, and we want to find the potential and the electric field intensity in the surrounding space as well as the surface charge distributions on the conducting boundaries. $\ELto$ solving boundary-value problems

```{.figure #m03-map caption=""}
```

- What is the form of Poisson's and Laplace's equations that govern the electric potential, and when is each of them used?
- How can the electric potential and the electric field intensity be obtained by solving Poisson's and Laplace's equations?
- Is a solution of Poisson's equation that satisfies given boundary conditions unique?

## Poisson's and Laplace's Equations

- The two fundamental equations of electrostatics in all media

$$\nabla\cdot\vect{D}=\rho\qquad\qquad \nabla\times\vect{E}=0$$

- On the other hand we have

$$\vect{E}=-\nabla V$$
$$\vect{D}=\epsilon\vect{E}\quad\Longrightarrow\quad\nabla\cdot\epsilon\vect{E}=\rho\quad\Longrightarrow\quad\nabla\cdot(\epsilon\nabla V)=-\rho$$

- If the medium is homogeneous ($\epsilon$ constant)

::: {.important}
$$\nabla^2V=-\frac{\rho}{\epsilon}$$
:::

- $\rho$: free charge density
- In the above equation, known as **Poisson's equation**, the **Laplacian** operator (the divergence of the gradient) is used.

- The Laplacian of a scalar quantity in the different coordinate systems
    - Cartesian
$$\nabla^2V=\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}$$
    - Cylindrical
$$\nabla^2V=\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2V}{\partial\phi^2}+\frac{\partial^2V}{\partial z^2}$$
    - Spherical
$$\nabla^2V=\frac{1}{R^2}\frac{\partial}{\partial R}\left(R^2\frac{\partial V}{\partial R}\right)+\frac{1}{R^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial V}{\partial\theta}\right)+\frac{1}{R^2\sin^2\theta}\frac{\partial^2V}{\partial\phi^2}$$

- Solving Poisson's equation in three-dimensional space with given boundary conditions is usually not a simple task.
- At points of a simple medium where there is no free charge

::: {.important}
$$\nabla^2V=0$$
:::

- The above equation is called **Laplace's equation**.
    - This equation governs problems involving a set of conductors held at different potentials.
    - Once $V$ has been found from this equation, $\vect{E}$ and the charge distribution on the conducting surfaces are easily obtained

$$\vect{E}=-\nabla V\qquad\qquad \rho_s=-\epsilon E_n$$

::: {.example number="3-1"}
The two plates of a parallel-plate capacitor are separated by the distance $d$ and held at the potentials $0$ and $V_0$ as shown in the figure below. Neglecting the fringing fields, find

- (a) the potential at all points between the plates
- (b) the surface charge densities on the plates

```{.figure #m03-ex1 caption=""}
```

::: {.solution}
- (a) Using Laplace's equation

$$\nabla^2V=0\quad\Longrightarrow\quad\frac{d^2V}{dy^2}=0\quad\Longrightarrow\quad\frac{dV}{dy}=C_1\quad\Longrightarrow\quad V=C_1y+C_2$$

- Boundary conditions:

$$\left.\begin{aligned}&\text{At }y=0,\quad V=0\\&\text{At }y=d,\quad V=V_0\end{aligned}\right\}\quad\Longrightarrow\quad V=\frac{V_0}{d}y$$

- (b)

$$\vect{E}=-\nabla V\quad\Longrightarrow\quad\vect{E}=-\uvec{y}\frac{dV}{dy}=-\uvec{y}\frac{V_0}{d}$$
$$E_n=\uvec{n}\cdot\vect{E}=\frac{\rho_s}{\epsilon}$$

- For the lower plate

$$\uvec{n}=\uvec{y},\qquad E_{n\ell}=-\frac{V_0}{d},\qquad \rho_{s\ell}=-\frac{\epsilon V_0}{d}$$

- For the upper plate

$$\uvec{n}=-\uvec{y},\qquad E_{nu}=\frac{V_0}{d},\qquad \rho_{su}=\frac{\epsilon V_0}{d}$$
:::
:::

::: {.example number="3-2"}
Solving Poisson's and Laplace's equations for $V$, determine the field $\vect{E}$ inside and outside a spherical electron cloud with uniform volume charge density $\rho=-\rho_0$ for $0\leq R\leq b$ and $\rho=0$ for $R>b$.

::: {.solution}
- Inside the electron cloud $\ELto$ using Poisson's equation

$$\nabla^2V=-\frac\rho\epsilon\quad\Longrightarrow\quad\frac{1}{R^2}\frac{d}{dR}\left(R^2\frac{dV_i}{dR}\right)=\frac{\rho_0}{\epsilon_0}\quad\Longrightarrow\quad\frac{d}{dR}\left(R^2\frac{dV_i}{dR}\right)=\frac{\rho_0}{\epsilon_0}R^2\quad\Longrightarrow\quad R^2\frac{dV_i}{dR}=\frac{\rho_0}{3\epsilon_0}R^3+C_1$$
$$\frac{dV_i}{dR}=\frac{\rho_0}{3\epsilon_0}R+\frac{C_1}{R^2}\quad\Longrightarrow\quad\vect{E}_i=-\nabla V_i=-\uvec{R}\left(\frac{dV_i}{dR}\right)$$

- Since the field at $R=0$ cannot be infinite

$$C_1=0\quad\Longrightarrow\quad\vect{E}_i=-\uvec{R}\frac{\rho_0}{3\epsilon_0}R,\qquad 0\leq R\leq b$$

- Outside the electron cloud $\ELto$ using Laplace's equation

$$\nabla^2V=0\quad\Longrightarrow\quad\frac{1}{R^2}\frac{\partial}{\partial R}\left(R^2\frac{dV_o}{dR}\right)=0\quad\Longrightarrow\quad\frac{dV_o}{dR}=\frac{C_2}{R^2}$$
$$\vect{E}_o=-\nabla V_o=-\uvec{R}\frac{dV_o}{dR}=-\uvec{R}\frac{C_2}{R^2}$$

- Because the medium is continuous, the fields $\vect{E}_i$ and $\vect{E}_o$ are equal at $R=b$

$$\frac{C_2}{b^2}=\frac{\rho_0}{3\epsilon_0}b\quad\Longrightarrow\quad C_2=\frac{\rho_0b^3}{3\epsilon_0}\quad\Longrightarrow\quad\vect{E}_o=-\uvec{R}\frac{\rho_0b^3}{3\epsilon_0R^2},\qquad R\geq b$$
:::
:::

## Uniqueness Theorem

```{.figure #m03-map-unique caption=""}
```

- A solution of Poisson's equation (and, as a special case, of Laplace's equation) that satisfies the given boundary conditions is the unique solution of that equation.
- The consequence of this theorem is that a solution of any electrostatic problem that satisfies the boundary conditions is the only possible solution, regardless of the method by which it was obtained.

## Method of Images

```{.figure #m03-map-images caption=""}
```

- What is the method of images, and how can it be used to solve a particular class of electrostatic problems?

- In a class of electromagnetic problems, solving Laplace's equation while satisfying the boundary conditions is very difficult. In these problems, however, the boundary conditions can be satisfied with the help of **image charges**.
    - This method, which consists of replacing the boundary surfaces by equivalent image charges, is called the **method of images**.
- As an example consider the following problem. We want to find the potential at all points $y>0$.

```{.figure #m03-image-problem caption=""}
```

- Gauss's law cannot be used to compute the field and then the potential, because a Gaussian surface cannot be determined.
- Nor can the potential be computed directly, because the presence of the positive charge $Q$ induces negative charges on the surface of the conductor, giving a surface charge density $\rho_s$. We have

$$V(x,y,z)=\frac{Q}{4\pi\epsilon_0\sqrt{x^2+(y-d)^2+z^2}}+\frac{1}{4\pi\epsilon_0}\int_S\frac{\rho_s}{R_1}\,ds$$

- The difficulty is that $\rho_s$ must be found first, and even when $\rho_s$ is known the surface integral is difficult to evaluate.
- Solving Laplace's equation to obtain the solution is also impossible or very difficult. In fact the solution of Laplace's equation must satisfy the following conditions

$$V(x,0,z)=0$$
$$V\to\frac{Q}{4\pi\epsilon_0R},\ \text{as}\ R\to0$$

- At points very far from the charge $Q$ the potential must be zero

$$V(x,y,z)=V(-x,y,z)$$
$$V(x,y,z)=V(x,y,-z)$$

- Such a problem can be solved easily with the method of images.

### Point Charge and Conducting Plane

- We remove the conducting plane and replace it by an image point charge $-Q$ at $y=-d$

```{.figure #m03-image-plane caption=""}
```

::: {.important}
$$V(x,y,z)=\frac{Q}{4\pi\epsilon_0}\left(\frac{1}{R_+}-\frac{1}{R_-}\right)$$
$$R_+=\left[x^2+(y-d)^2+z^2\right]^{1/2},\qquad R_-=\left[x^2+(y+d)^2+z^2\right]^{1/2}$$
:::

- It can easily be shown that this solution satisfies Laplace's equation and the boundary conditions. Therefore it is a solution of the problem and, by the uniqueness theorem, also its only solution.
- Once the potential is known, computing the field and the surface charge distribution on the conductor is easy.

::: {.remark}
Note that this method cannot be used to compute the potential in the region $y<0$.
:::

### Line Charge and Parallel Conducting Cylinder

```{.figure #m03-line-cylinder caption=""}
```

- The aim is to find the potential outside the conducting cylinder.
- The image must be a parallel line charge inside the cylinder that makes the cylinder surface $r=a$ an equipotential surface. The aim is to find $d_i$ and $\rho_i$.
- We assume

::: {.important}
$$\rho_i=-\rho_\ell$$
:::

- The potential at the distance $r$ from a line charge of density $\rho_\ell$, with the reference at $r_0$, is

$$V=-\int_{r_0}^{r}E_r\,dr=-\frac{\rho_\ell}{2\pi\epsilon_0}\int_{r_0}^{r}\frac1r\,dr=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_0}{r}$$

- The potential at the point $M$ on the surface of the cylinder is

$$\begin{aligned}V_M&=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_0}{r}-\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_0}{r_i}\\&=\frac{\rho_\ell}{2\pi\epsilon_0}\ln\frac{r_i}{r}\end{aligned}$$

- Therefore the equipotential surfaces are specified by

$$\frac{r_i}{r}=\text{Constant}$$

```{.figure #m03-similar-triangles caption=""}
```

- If the condition $\dfrac{d_i}{a}=\dfrac ad$ holds, then by the similarity of the two triangles $OMP_i$ and $OPM$ the ratio $\dfrac{r_i}{r}$ is always constant. Therefore

::: {.important}
$$d_i=\frac{a^2}{d}$$
:::

- Thus the line charge $-\rho_\ell$ can replace the conducting cylindrical surface, and the potential and the electric field at any point outside the cylinder can be found.

::: {.remark}
Note that this method cannot be used to compute the potential in the region inside the conducting cylinder.
:::

::: {.example number="3-3"}
Find the capacitance per unit length between two very long parallel circular conducting wires of radius $a$ separated by $D$.

```{.figure #m03-ex3 caption=""}
```

::: {.solution}
- We place the charges $+Q$ and $-Q$ on conductors 1 and 2 respectively.
- With the method of images, the equipotential surfaces of the wires can be replaced by two line charges $+\rho_\ell$ and $-\rho_\ell$.

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

## Boundary-Value Problems

```{.figure #m03-map-bvp caption=""}
```

- The method of images applies to problems involving free charges near conducting boundaries of simple geometry.
- If the problem involves a set of conductors held at given potentials, with no isolated free charges, it cannot be solved by the method of images, and Laplace's equation must be solved.
- Laplace's equation is a partial differential equation. Problems governed by partial differential equations with given boundary conditions are called **boundary-value problems**.
- Boundary-value problems for potential functions are divided into classes
    - Dirichlet problems: the value of the potential is specified at all points of the boundaries.
    - Neumann problems: the normal derivative of the potential is specified on all boundaries.
    - Mixed boundary-value problems: the potential is specified on some of the boundaries and the normal derivative of the potential on the rest.

- How are electrostatic boundary-value problems solved in the different coordinate systems to obtain the potential distribution?

### Cartesian Coordinates

- Laplace's equation in Cartesian coordinates

$$\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}=0$$

- Using the method of separation of variables

$$V(x,y,z)=X(x)Y(y)Z(z)$$
$$Y(y)Z(z)\frac{d^2X(x)}{dx^2}+X(x)Z(z)\frac{d^2Y(y)}{dy^2}+X(x)Y(y)\frac{d^2Z(z)}{dz^2}=0$$
$$\underbrace{\frac{1}{X(x)}\frac{d^2X(x)}{dx^2}}_{-k_x^2}+\underbrace{\frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2}}_{-k_y^2}+\underbrace{\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}}_{-k_z^2}=0$$
$$k_x^2+k_y^2+k_z^2=0$$

::: {.important}
$$\frac{d^2X(x)}{dx^2}+k_x^2X(x)=0\qquad \frac{d^2Y(y)}{dy^2}+k_y^2Y(y)=0\qquad \frac{d^2Z(z)}{dz^2}+k_z^2Z(z)=0$$
:::

**Possible Solutions of $X''(x)+k_x^2X(x)=0$**

| $k_x^2$ | $k_x$ | $X(x)$ | Exponential forms of $X(x)$ |
|---|---|---|---|
| $0$ | $0$ | $A_0x+B_0$ | |
| $+$ | $k$ | $A_1\sin kx+B_1\cos kx$ | $C_1e^{jkx}+D_1e^{-jkx}$ |
| $-$ | $jk$ | $A_2\sinh kx+B_2\cosh kx$ | $C_2e^{kx}+D_2e^{-kx}$ |


::: {.example number="3-4"}
Two grounded, semi-infinite, parallel conducting plates are separated by the distance $d$. A third plate, perpendicular to both and insulated from them, is held at the potential $V_0$. Determine the potential distribution in the region enclosed by the plates.

```{.figure #m03-ex4 caption=""}
```

::: {.solution}
- Boundary conditions

$$\text{(1)}\ \ V(x,y,z)=V(x,y)\qquad\text{(2)}\ \ V(0,y)=V_0\qquad\text{(3)}\ \ V(\infty,y)=0\qquad\text{(4)}\ \ V(x,0)=0\qquad\text{(5)}\ \ V(x,b)=0$$

$$\text{(1)}\quad\Longrightarrow\quad\frac{\partial V}{\partial z}=0\quad\Longrightarrow\quad Z(z)=B_0$$
$$\left.\begin{aligned}k_z^2&=-\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}=0\\k_x^2+k_y^2+k_z^2&=0\end{aligned}\right\}\quad k_y^2=-k_x^2=k^2\qquad(k\ \text{real})$$
$$k_x=jk\quad\Longrightarrow\quad X(x)=C_2e^{kx}+D_2e^{-kx}\quad\overset{(3)}{\Longrightarrow}\quad X(x)=D_2e^{-kx}$$
$$k_y=k\quad\Longrightarrow\quad Y(y)=A_1\sin ky+B_1\cos ky\quad\overset{(4)}{\Longrightarrow}\quad Y(y)=A_1\sin ky$$
$$\begin{aligned}V_n(x,y)&=(B_0D_2A_1)e^{-kx}\sin ky\\&=C_ne^{-kx}\sin ky\end{aligned}$$
$$\overset{(5)}{\Longrightarrow}\quad V_n(x,b)=C_ne^{-kx}\sin kb=0\quad\Longrightarrow\quad\sin kb=0\quad\Longrightarrow\quad kb=n\pi$$
$$k=\frac{n\pi}{b},\qquad n=1,2,3,\ldots$$
$$V_n(x,y)=C_ne^{-n\pi x/b}\sin\frac{n\pi}{b}y$$

- The above relation satisfies Laplace's equation but by itself cannot satisfy the second boundary condition at $x=0$ for all $y$ from $0$ to $b$.
- Since Laplace's equation is a linear partial differential equation, a combination of $V_n$ of the above form for different values of $n$ is also a solution.

$$V(x,y)=\sum_{n=1}^{\infty}V_n(x,y)$$

$$\overset{(2)}{\Longrightarrow}\quad\begin{aligned}V(0,y)&=\sum_{n=1}^{\infty}V_n(0,y)=\sum_{n=1}^{\infty}C_n\sin\frac{n\pi}{b}y\\&=V_0,\qquad 0<y<b\end{aligned}$$

- The above relation is the Fourier series expansion of a periodic odd function whose value on the interval $0<y<b$ is $V_0$.

```{.figure #m03-ex4-square caption=""}
```

::: {.remark title="Reminder"}
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

### Cylindrical Coordinates

- Laplace's equation in cylindrical coordinates

$$\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2V}{\partial\phi^2}+\frac{\partial^2V}{\partial z^2}=0$$

- Assuming the length is large compared with the radius, in cylindrical geometry the potential is independent of $z$.

$$\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2V}{\partial\phi^2}=0$$

- Using the method of separation of variables

$$V(r,\phi)=R(r)\Phi(\phi)$$
$$\underbrace{\frac{r}{R(r)}\frac{d}{dr}\left[r\frac{dR(r)}{dr}\right]}_{k^2}+\underbrace{\frac{1}{\Phi(\phi)}\frac{d^2\Phi(\phi)}{d\phi^2}}_{-k^2}=0$$

- The differential equation in $\phi$

::: {.important}
$$\frac{d^2\Phi(\phi)}{d\phi^2}+k^2\Phi(\phi)=0$$
:::

- **When $k\neq0$**
    - In circular cylindrical configurations the potential functions, and hence $\Phi(\phi)$, are periodic in $\phi$, and the hyperbolic functions are not used.
        - If the range of $\phi$ is not restricted, $k$ must be an integer ($k=n$)

$$\Phi(\phi)=A_\phi\sin n\phi+B_\phi\cos n\phi$$

- The differential equation in $r$ (Euler's equation)

$$r^2\frac{d^2R(r)}{dr^2}+r\frac{dR(r)}{dr}-n^2R(r)=0$$
$$R(r)=A_rr^n+B_rr^{-n}$$

::: {.important}
$$V_n(r,\phi)=r^n(A_n\sin n\phi+B_n\cos n\phi)+r^{-n}(A'_n\sin n\phi+B'_n\cos n\phi),\qquad n\neq0$$
:::

- When the region of interest includes $r=0$, the terms containing $r^{-n}$ cannot exist, and when the region of interest includes infinity, the terms containing $r^n$ cannot exist.

- **When $k=0$**

$$\frac{d^2\Phi(\phi)}{d\phi^2}=0$$
$$\Phi(\phi)=A_0\phi+B_0\quad\Longrightarrow\quad\Phi(\phi)=B_0$$

- If there is no circumferential variation

$$\frac{d}{dr}\left[r\frac{dR(r)}{dr}\right]=0$$
$$R(r)=C_0\ln r+D_0$$

::: {.example number="3-5"}
Consider a very long coaxial cable. The inner conductor has radius $a$ and is held at the potential $V_0$. The outer conductor has radius $b$ and is grounded. Find the potential distribution in the space between the two conductors.

```{.figure #m03-ex5 caption=""}
```

::: {.solution}
- Since the cable is long, there is no dependence on $z$.
- By symmetry, there is no dependence on $\phi$ ($k=0$).

$$V(r)=C_1\ln r+C_2$$
$$V(b)=0,\qquad V(a)=V_0$$
$$C_1=-\frac{V_0}{\ln(b/a)},\qquad C_2=\frac{V_0\ln b}{\ln(b/a)}\qquad\Longrightarrow\qquad V(r)=\frac{V_0}{\ln(b/a)}\ln\left(\frac br\right)$$
:::
:::

::: {.example number="3-6"}
Two semi-infinite conducting plates are held at the potentials $V_0$ and zero as shown in the figure below. Assuming that the plates are very long along the $z$-axis, find the potential distribution in all space.

```{.figure #m03-ex6 caption=""}
```

::: {.solution}
- Since the plates are long, there is no dependence on $z$.
- There is no dependence on $r$ ($k=0$).

$$\Phi(\phi)=A_0\phi+B_0$$
$$V(\phi)=\begin{cases}0&\phi=0,2\pi\\V_0&\phi=\alpha\end{cases}$$

- $0\leq\phi\leq\alpha$

$$V(\phi)=\frac{V_0}{\alpha}\phi$$

- $\alpha\leq\phi\leq2\pi$

$$V(\phi)=\frac{V_0}{2\pi-\alpha}(2\pi-\phi)$$
:::
:::

::: {.example number="3-7"}
A very long, thin conducting cylindrical tube of radius $b$ is split into two parts. The upper half is held at the potential $V_0$ and the lower half at the potential $-V_0$. Find the potential distribution inside and outside the tube.

```{.figure #m03-ex7 caption=""}
```

::: {.solution}
- Since the tube is long, there is no dependence on $z$.

$$V_n(r,\phi)=r^n(A_n\sin n\phi+B_n\cos n\phi)+r^{-n}(A'_n\sin n\phi+B'_n\cos n\phi)$$
$$V(b,\phi)=\begin{cases}V_0&\text{for }0<\phi<\pi\\-V_0&\text{for }\pi<\phi<2\pi\end{cases}$$

- Inside the tube ($r<b$)
    - Since the region of interest includes $r=0$, the terms containing $r^{-n}$ cannot exist.
    - Since $V(r,\phi)$ is an odd function of $\phi$, therefore

$$V_n(r,\phi)=A_nr^n\sin n\phi$$

- The above term alone cannot satisfy the boundary conditions. Therefore

$$\begin{aligned}V(r,\phi)&=\sum_{n=1}^{\infty}V_n(r,\phi)\\&=\sum_{n=1}^{\infty}A_nr^n\sin n\phi\end{aligned}$$
$$\sum_{n=1}^{\infty}A_nb^n\sin n\phi=\begin{cases}V_0&\text{for }0<\phi<\pi\\-V_0&\text{for }\pi<\phi<2\pi\end{cases}$$

- The above relation is the Fourier series expansion of a periodic odd function whose value is $V_0$ on the interval $0<\phi<\pi$ and $-V_0$ on the interval $\pi<\phi<2\pi$.

$$A_n=\begin{cases}\dfrac{4V_0}{n\pi b^n}&\text{if }n\text{ is odd}\\[2mm]0&\text{if }n\text{ is even}\end{cases}\qquad\qquad V(r,\phi)=\frac{4V_0}{\pi}\sum_{n=\text{odd}}^{\infty}\frac1n\left(\frac rb\right)^n\sin n\phi,\qquad r<b$$

- Outside the tube ($r>b$)
    - Since the region of interest includes $r\to\infty$, the terms containing $r^n$ cannot exist.
    - $V(r,\phi)$ is an odd function of $\phi$.
    - A single term cannot satisfy the boundary conditions. Therefore

$$\begin{aligned}V(r,\phi)&=\sum_{n=1}^{\infty}V_n(r,\phi)\\&=\sum_{n=1}^{\infty}B'_nr^{-n}\sin n\phi\end{aligned}\qquad\begin{aligned}V(b,\phi)&=\sum_{n=1}^{\infty}B'_nb^{-n}\sin n\phi\\&=\begin{cases}V_0&\text{for }0<\phi<\pi\\-V_0&\text{for }\pi<\phi<2\pi\end{cases}\end{aligned}$$
$$B'_n=\begin{cases}\dfrac{4V_0b^n}{n\pi}&\text{if }n\text{ is odd}\\[2mm]0&\text{if }n\text{ is even}\end{cases}$$

::: {.important}
$$V(r,\phi)=\frac{4V_0}{\pi}\sum_{n=\text{odd}}^{\infty}\frac1n\left(\frac br\right)^n\sin n\phi,\qquad r>b$$
:::
:::
:::
