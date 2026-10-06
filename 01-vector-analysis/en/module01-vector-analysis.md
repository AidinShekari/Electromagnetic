# Vector Analysis

## Course Outline

```{.figure #m01-course-outline caption=""}
```

## Vector Analysis

- **Vector analysis** is a mathematical tool with which the expression and understanding of electromagnetic concepts become simple.
- Quantities in electromagnetics are divided into the following two groups.
    - **Scalar:** a quantity that is completely specified by its magnitude (positive or negative). For example: charge, electric current, energy, …
    - **Vector:** a quantity that is described by a magnitude and a direction. For example the electric and magnetic field intensity, …
- Both of the above quantities can be functions of position and time.

::: {.example number="1-1"}
- In your opinion, of what type are the following quantities?
    - Temperature
    - Power
    - Force
    - Potential difference
    - Velocity
- Apart from the above, which other scalar and vector quantities in physics can you name?
:::

```{.figure #m01-vector-analysis-map caption=""}
```

- How can two vector quantities be added or subtracted graphically?
- How can vectors be multiplied? What is the meaning of this product? Where is it used?

$$\vect{A}=2\uvec{x}+3\uvec{y}+\uvec{z}\qquad \vect{B}=\uvec{x}-2\uvec{y}+3\uvec{z}\qquad \vect{C}=-\uvec{x}+4\uvec{y}-\uvec{z}$$

- Find the magnitude of the projection of vector $\vect{A}$ on vector $\vect{B}$.
- What is the angle between vectors $\vect{A}$ and $\vect{B}$?
- What is the area of the triangle formed by the two vectors $\vect{A}$ and $\vect{B}$?
- Find the unit vector normal to the plane containing the two vectors $\vect{A}$ and $\vect{B}$.
- What is the volume of the parallelepiped formed by the 3 vectors $\vect{A}$, $\vect{B}$ and $\vect{C}$?

## Vector Algebra

- Every vector has a magnitude and a direction.

$$\vect{A}=\uvec{A}A,\qquad \uvec{A}=\frac{\vect{A}}{\abs{\vect{A}}}=\frac{\vect{A}}{A}\quad(\text{unit vector})$$

```{.figure #m01-vector-magnitude caption=""}
```

::: {.remark}
For every vector quantity both the magnitude and the direction must be known. Leaving the direction of a vector quantity unspecified means ignoring part of the information of that quantity.
:::

## Addition of Vectors

- Adding two vectors graphically
    - The **parallelogram** rule
    - The **head-to-tail** rule

```{.figure #m01-vector-sum caption=""}
```

- Laws governing the addition of vectors
    - **Commutative law**
$$\vect{A}+\vect{B}=\vect{B}+\vect{A}$$

    - **Associative law**
$$\vect{A}+(\vect{B}+\vect{C})=(\vect{A}+\vect{B})+\vect{C}$$

## Subtraction of Vectors

- Vector subtraction

$$\vect{A}-\vect{B}=\vect{A}+(-\vect{B})$$

```{.figure #m01-vector-difference caption=""}
```

## Multiplication of Vectors

```{.figure #m01-products-map caption=""}
```

- Multiplication of a vector by a scalar:

$$k\vect{A}=\uvec{A}(kA)$$

## Dot or Scalar Product

::: {.definition title="Mathematical definition"}
$$\vect{A}\cdot\vect{B}\triangleq AB\cos\theta_{AB}$$

- It equals the product of the magnitude of one vector and the projection of the other vector on the first.
:::

```{.figure #m01-dot-product caption="$\\theta_{AB}$: the smaller angle between the two vectors when their tails are joined"}
```

- Properties of the dot product
    - The dot product of two vectors is a scalar quantity.
    - It is less than or equal to the product of their magnitudes.
    - Depending on the angle between them it can be positive or negative.
    - If the vectors are perpendicular to each other, it is zero.
    - It is commutative and distributive.
$$\vect{A}\cdot\vect{B}=\vect{B}\cdot\vect{A},\qquad \vect{A}\cdot(\vect{B}+\vect{C})=\vect{A}\cdot\vect{B}+\vect{A}\cdot\vect{C}$$

    - The dot product of a vector with itself
$$\vect{A}\cdot\vect{A}=A^2,\qquad A=+\sqrt{\vect{A}\cdot\vect{A}}$$

::: {.example number="1-2"}
Using the concept of the dot product, find the projection of vector $\vect{A}$ on $\vect{B}$.

```{.figure #m01-ex2-statement caption=""}
```

::: {.solution}
```{.figure #m01-ex2-projection caption=""}
```

Magnitude of the projection of vector $\vect{A}$ on $\vect{B}$:
$$A\cos\theta_{AB}=\frac{\vect{A}\cdot\vect{B}}{B}$$
Projection of vector $\vect{A}$ on $\vect{B}$:
$$\frac{\vect{A}\cdot\vect{B}}{B}\uvec{B}=\left(\frac{\vect{A}\cdot\vect{B}}{B}\right)\frac{\vect{B}}{B}=\frac{\vect{A}\cdot\vect{B}}{B^2}\vect{B}$$
:::
:::

::: {.example number="1-3"}
Prove the law of cosines for a triangle using the concept of the dot product.
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

## Cross or Vector Product

::: {.definition}
$$\vect{A}\times\vect{B}\triangleq\uvec{n}\abs{AB\sin\theta_{AB}}$$
:::

- The magnitude of this product equals the area of the parallelogram formed by the vectors $\vect{A}$ and $\vect{B}$, and its direction is perpendicular to both vectors.

```{.figure #m01-cross-product caption=""}
```

- Properties of the cross product
    - The cross product of two vectors is a vector quantity.
    - It is not commutative
$$\vect{B}\times\vect{A}=-\vect{A}\times\vect{B}$$

    - It is distributive
$$\vect{A}\times(\vect{B}+\vect{C})=\vect{A}\times\vect{B}+\vect{A}\times\vect{C}$$

    - It is not associative
$$\vect{A}\times(\vect{B}\times\vect{C})\neq(\vect{A}\times\vect{B})\times\vect{C}$$

::: {.example number="1-4"}
Prove the law of sines for a triangle using the concept of the cross product.
$$\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}$$

```{.figure #m01-ex4-triangle caption=""}
```

::: {.solution}
Area of the triangle:
$$\abs*{\tfrac12\vect{a}\times\vect{b}}=\abs*{\tfrac12\vect{b}\times\vect{c}}=\abs*{\tfrac12\vect{c}\times\vect{a}}$$
$$ab\sin C=bc\sin A=ca\sin B$$
$$\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}$$
:::
:::

## Product of Three Vectors

- **Scalar triple product**

$$\vect{A}\cdot(\vect{B}\times\vect{C})=\vect{B}\cdot(\vect{C}\times\vect{A})=\vect{C}\cdot(\vect{A}\times\vect{B})$$

- Its magnitude equals the volume of the parallelepiped formed by the three vectors $\vect{A}$, $\vect{B}$ and $\vect{C}$.
    - Area of the base: $\abs{\vect{B}\times\vect{C}}=\abs{BC\sin\theta_1}$
    - Height: $\abs{A\cos\theta_2}$
    - Volume of the parallelepiped: $\abs{ABC\sin\theta_1\cos\theta_2}$

```{.figure #m01-triple-product caption=""}
```

- **Vector triple product**
    - Known as the back-cab rule

$$\vect{A}\times(\vect{B}\times\vect{C})=\vect{B}(\vect{A}\cdot\vect{C})-\vect{C}(\vect{A}\cdot\vect{B})$$

::: {.example number="1-5"}
The expression $(\vect{A}\times\vect{B})\times\vect{C}$ is equal to which of the following expressions?

- $\vect{B}(\vect{A}\cdot\vect{C})-\vect{C}(\vect{A}\cdot\vect{B})$
- $-\vect{B}(\vect{A}\cdot\vect{C})+\vect{C}(\vect{A}\cdot\vect{B})$
- $-\vect{A}(\vect{C}\cdot\vect{B})+\vect{B}(\vect{C}\cdot\vect{A})$
- $\vect{A}(\vect{C}\cdot\vect{B})-\vect{B}(\vect{C}\cdot\vect{A})$

::: {.solution}
$$\begin{aligned}(\vect{A}\times\vect{B})\times\vect{C}&=-\vect{C}\times(\vect{A}\times\vect{B})\\&=-\vect{A}(\vect{C}\cdot\vect{B})+\vect{B}(\vect{C}\cdot\vect{A})\end{aligned}$$
:::
:::

## Orthogonal Coordinate Systems

```{.figure #m01-vector-analysis-map-coord caption=""}
```

- What are the principal surfaces in the different coordinate systems?
- How are the unit vectors defined in the different coordinate systems?
- How are the position vector of a point and the distance vector between two points computed in the different coordinate systems?
- Determine the differential length, surface and volume in the different coordinate systems, for use in integration.
- Find the representation of the vector $\vect{A}=\uvec{r}(3\cos\phi)-\uvec{\phi}2r+\uvec{z}5$ in Cartesian coordinates.
- The position of point $P$ in spherical coordinates is $(8,120^\circ,330^\circ)$. Express the position of this point in cylindrical and Cartesian coordinates.

- To describe the spatial variations of physical quantities, we must be able to describe all points of space uniquely and appropriately.
    - This requires the use of an appropriate coordinate system.
- The laws of electromagnetics do not depend on the coordinate system.
- For simplicity of the calculations, a coordinate system that suits the geometry of the problem is used.
- In three-dimensional space a point can be located at the intersection of three surfaces.
    - If these three surfaces are mutually perpendicular, we have an orthogonal coordinate system.
- The three orthogonal systems used in this course
    - Cartesian (rectangular) coordinates
    - Cylindrical coordinates
    - Spherical coordinates

## Cartesian Coordinate System

```{.figure #m01-cartesian-planes caption=""}
```

- Every point $P(x_1,y_1,z_1)$ is the intersection of the three planes $x=x_1$, $y=y_1$ and $z=z_1$.
- Unit vector $\uvec{x}$ $\ELto$ the unit vector normal to the $x$-constant plane, in the positive direction
- Unit vector $\uvec{y}$ $\ELto$ the unit vector normal to the $y$-constant plane, in the positive direction
- Unit vector $\uvec{z}$ $\ELto$ the unit vector normal to the $z$-constant plane, in the positive direction

- Cross and dot products of the unit vectors

$$\uvec{x}\times\uvec{y}=\uvec{z},\qquad \uvec{y}\times\uvec{z}=\uvec{x},\qquad \uvec{z}\times\uvec{x}=\uvec{y}$$

```{.figure #m01-cartesian-cycle caption=""}
```

$$\uvec{x}\cdot\uvec{y}=\uvec{y}\cdot\uvec{z}=\uvec{z}\cdot\uvec{x}=0$$
$$\uvec{x}\cdot\uvec{x}=\uvec{y}\cdot\uvec{y}=\uvec{z}\cdot\uvec{z}=1$$

- Representation of an arbitrary vector $\vect{A}$ in Cartesian coordinates

::: {.important}
$$\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z$$
$$A=\sqrt{A_x^2+A_y^2+A_z^2}$$
:::

- **Position vector**
    - The position vector of point $P$ is the directed distance from the origin to $P$.

$$\vect{R}_1=x_1\uvec{x}+y_1\uvec{y}+z_1\uvec{z},\qquad \vect{R}_2=x_2\uvec{x}+y_2\uvec{y}+z_2\uvec{z}$$

- **Distance vector**
    - The displacement vector from one point to another.

$$\vect{R}_{12}=\vect{R}_2-\vect{R}_1=(x_2-x_1)\uvec{x}+(y_2-y_1)\uvec{y}+(z_2-z_1)\uvec{z}$$

```{.figure #m01-position-vectors caption=""}
```

$$\vect{A}=A_x\uvec{x}+A_y\uvec{y}+A_z\uvec{z},\qquad \vect{B}=B_x\uvec{x}+B_y\uvec{y}+B_z\uvec{z}$$

- Dot product of the two vectors $\vect{A}$ and $\vect{B}$

::: {.important}
$$\vect{A}\cdot\vect{B}=A_xB_x+A_yB_y+A_zB_z$$
:::

- Cross product of the two vectors $\vect{A}$ and $\vect{B}$

$$\begin{aligned}\vect{A}\times\vect{B}={}&A_xB_x\uvec{x}\times\uvec{x}+A_xB_y\uvec{x}\times\uvec{y}+A_xB_z\uvec{x}\times\uvec{z}\\&+A_yB_x\uvec{y}\times\uvec{x}+A_yB_y\uvec{y}\times\uvec{y}+A_yB_z\uvec{y}\times\uvec{z}\\&+A_zB_x\uvec{z}\times\uvec{x}+A_zB_y\uvec{z}\times\uvec{y}+A_zB_z\uvec{z}\times\uvec{z}\\={}&(A_yB_z-A_zB_y)\uvec{x}+(A_zB_x-A_xB_z)\uvec{y}+(A_xB_y-A_yB_x)\uvec{z}\end{aligned}$$

::: {.important}
$$\vect{A}\times\vect{B}=\begin{vmatrix}\uvec{x}&\uvec{y}&\uvec{z}\\A_x&A_y&A_z\\B_x&B_y&B_z\end{vmatrix}$$
:::

- Differential length $\ELto$ **vector**

$$\dif\vect{\ell}=\uvec{x}\,dx+\uvec{y}\,dy+\uvec{z}\,dz$$

- Differential surface $\ELto$ **vector**

$$d\vect{S}=dS\,\uvec{n}$$
$$d\vect{S}=dy\,dz\,\uvec{x},\qquad d\vect{S}=dx\,dz\,\uvec{y},\qquad d\vect{S}=dx\,dy\,\uvec{z}$$

- Differential volume $\ELto$ **scalar**

$$dv=dx\,dy\,dz$$

```{.figure #m01-cartesian-differentials caption=""}
```

::: {.example number="1-6"}
(a) Find the vector whose initial point is $P_1(1,3,2)$ and whose terminal point is $P_2(3,-2,4)$.

(b) What is the length of this vector?

::: {.solution}
```{.figure #m01-ex6 caption=""}
```

(a)
$$\begin{aligned}\overrightarrow{P_1P_2}&=\overrightarrow{OP_2}-\overrightarrow{OP_1}\\&=(\uvec{x}3-\uvec{y}2+\uvec{z}4)-(\uvec{x}+\uvec{y}3+\uvec{z}2)\\&=\uvec{x}2-\uvec{y}5+\uvec{z}2\end{aligned}$$
(b)
$$P_1P_2=\abs{\overrightarrow{P_1P_2}}=\sqrt{2^2+(-5)^2+2^2}=\sqrt{33}$$
:::
:::

::: {.example number="1-7"}
Given $\vect{A}=\uvec{x}5-\uvec{y}2+\uvec{z}$, find the unit vector $\vect{B}$ such that

- (a) $\vect{B}\parallel\vect{A}$
- (b) $\vect{B}$ lies in the $xy$-plane and is perpendicular to $\vect{A}$

::: {.solution}
(a)
$$\vect{B}=\frac{\vect{A}}{A}=\frac{\uvec{x}5-\uvec{y}2+\uvec{z}}{\sqrt{5^2+2^2+1^2}}=\frac{\uvec{x}5-\uvec{y}2+\uvec{z}}{\sqrt{30}}$$
(b)
$$\begin{cases}B=\sqrt{B_x^2+B_y^2+B_z^2}=1\\B_z=0\\\vect{B}\cdot\vect{A}=5B_x-2B_y=0\end{cases}\quad\Rightarrow\quad\begin{cases}B_x=\dfrac{2}{\sqrt{29}}\\[2mm]B_y=\dfrac{5}{\sqrt{29}}\end{cases}$$
:::
:::

## Cylindrical Coordinate System

```{.figure #m01-cylindrical-surfaces caption=""}
```

- Every point $P(r_1,\phi_1,z_1)$ is the intersection of the cylinder $r=r_1$, the half-plane $\phi=\phi_1$ and the plane $z=z_1$.
- Unit vector $\uvec{r}$ $\ELto$ the unit vector normal to the $r$-constant cylinder, in the positive direction
- Unit vector $\uvec{\phi}$ $\ELto$ the unit vector normal to the $\phi$-constant half-plane, in the positive direction
- Unit vector $\uvec{z}$ $\ELto$ the unit vector normal to the $z$-constant plane, in the positive direction

::: {.remark}
The directions of the vectors $\uvec{r}$ and $\uvec{\phi}$ change from point to point in space. This must be taken into account in integration.
:::

- Cross and dot products of the unit vectors

$$\uvec{r}\times\uvec{\phi}=\uvec{z},\qquad \uvec{\phi}\times\uvec{z}=\uvec{r},\qquad \uvec{z}\times\uvec{r}=\uvec{\phi}$$

```{.figure #m01-cylindrical-cycle caption=""}
```

$$\uvec{r}\cdot\uvec{r}=\uvec{\phi}\cdot\uvec{\phi}=\uvec{z}\cdot\uvec{z}=1$$
$$\uvec{r}\cdot\uvec{\phi}=\uvec{\phi}\cdot\uvec{z}=\uvec{z}\cdot\uvec{r}=0$$

- Representation of an arbitrary vector $\vect{A}$ in cylindrical coordinates

::: {.important}
$$\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z$$
$$A=\sqrt{A_r^2+A_\phi^2+A_z^2}$$
:::

- Position vector

```{.figure #m01-cylindrical-position caption=""}
```

$$\vect{R}=r\uvec{r}+z\uvec{z}$$

::: {.example number="1-8"}
The cylindrical coordinates of an arbitrary point $P$ are $(r,\phi,0)$. Find the unit vector from the point $z=h$ on the $z$-axis toward the point $P$.

::: {.solution}
```{.figure #m01-ex8 caption=""}
```

$$\overrightarrow{QP}=\overrightarrow{OP}-\overrightarrow{OQ}=(\uvec{r}r)-(\uvec{z}h)$$
$$\uvec{QP}=\frac{\overrightarrow{QP}}{\abs{\overrightarrow{QP}}}=\frac{1}{\sqrt{r^2+h^2}}(\uvec{r}r-\uvec{z}h)$$
:::
:::

- Differential length $\ELto$ **vector**

$$\dif\vect{\ell}=\uvec{r}\,dr+\uvec{\phi}\,r\,d\phi+\uvec{z}\,dz$$

- Differential surface $\ELto$ **vector**

$$d\vect{S}=r\,d\phi\,dz\,\uvec{r},\qquad d\vect{S}=dr\,dz\,\uvec{\phi},\qquad d\vect{S}=r\,dr\,d\phi\,\uvec{z}$$

- Differential volume $\ELto$ **scalar**

$$dv=r\,dr\,d\phi\,dz$$

```{.figure #m01-cylindrical-differentials caption=""}
```

- Transformation of the representation of a vector from cylindrical to Cartesian coordinates

$$\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z$$

```{.figure #m01-cyl-cart-units caption=""}
```

$$\uvec{r}=\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y},\qquad \uvec{\phi}=-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y},\qquad \uvec{z}=\uvec{z}$$

$$\begin{aligned}\vect{A}&=(\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y})A_r\\&\quad+(-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y})A_\phi\\&\quad+\uvec{z}A_z\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{x}(\cos\phi\,A_r-\sin\phi\,A_\phi)\\&\quad+\uvec{y}(\sin\phi\,A_r+\cos\phi\,A_\phi)\\&\quad+\uvec{z}A_z\end{aligned}$$

- Transformation of the representation of a vector from Cartesian to cylindrical coordinates

$$\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z$$

$$\uvec{x}=\cos\phi\,\uvec{r}-\sin\phi\,\uvec{\phi},\qquad \uvec{y}=\sin\phi\,\uvec{r}+\cos\phi\,\uvec{\phi},\qquad \uvec{z}=\uvec{z}$$

$$\begin{aligned}\vect{A}&=(\cos\phi\,\uvec{r}-\sin\phi\,\uvec{\phi})A_x\\&\quad+(\sin\phi\,\uvec{r}+\cos\phi\,\uvec{\phi})A_y\\&\quad+\uvec{z}A_z\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{r}(\cos\phi\,A_x+\sin\phi\,A_y)\\&\quad+\uvec{\phi}(-\sin\phi\,A_x+\cos\phi\,A_y)\\&\quad+\uvec{z}A_z\end{aligned}$$

- Transformation of the representation of a vector from cylindrical to Cartesian coordinates

::: {.important}
$$\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}=\begin{bmatrix}\cos\phi&-\sin\phi&0\\\sin\phi&\cos\phi&0\\0&0&1\end{bmatrix}\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}$$
:::

- Transformation of the representation of a vector from Cartesian to cylindrical coordinates

::: {.important}
$$\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}=\begin{bmatrix}\cos\phi&\sin\phi&0\\-\sin\phi&\cos\phi&0\\0&0&1\end{bmatrix}\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}$$
:::

- Transformation from cylindrical to Cartesian coordinates

$$x=r\cos\phi,\qquad y=r\sin\phi,\qquad z=z$$

- Transformation from Cartesian to cylindrical coordinates

$$r=\sqrt{x^2+y^2},\qquad \phi=\tan^{-1}\frac{y}{x},\qquad z=z$$

```{.figure #m01-cyl-cart-coords caption=""}
```

## Spherical Coordinate System

```{.figure #m01-spherical-surfaces caption=""}
```

- Every point $P(R_1,\theta_1,\phi_1)$ is the intersection of the sphere $R=R_1$, the cone $\theta=\theta_1$ and the half-plane $\phi=\phi_1$
- Unit vector $\uvec{R}$ $\ELto$ the unit vector normal to the $R$-constant sphere, in the positive direction
- Unit vector $\uvec{\theta}$ $\ELto$ the unit vector normal to the $\theta$-constant cone, in the positive direction
- Unit vector $\uvec{\phi}$ $\ELto$ the unit vector normal to the $\phi$-constant half-plane, in the positive direction

::: {.remark}
The directions of the vectors $\uvec{R}$, $\uvec{\theta}$ and $\uvec{\phi}$ change from point to point in space. This must be taken into account in integration.
:::

- Cross and dot products of the unit vectors

$$\uvec{R}\times\uvec{\theta}=\uvec{\phi},\qquad \uvec{\theta}\times\uvec{\phi}=\uvec{R},\qquad \uvec{\phi}\times\uvec{R}=\uvec{\theta}$$

```{.figure #m01-spherical-cycle caption=""}
```

$$\uvec{R}\cdot\uvec{R}=\uvec{\theta}\cdot\uvec{\theta}=\uvec{\phi}\cdot\uvec{\phi}=1$$
$$\uvec{R}\cdot\uvec{\theta}=\uvec{\theta}\cdot\uvec{\phi}=\uvec{\phi}\cdot\uvec{R}=0$$

- Representation of an arbitrary vector $\vect{A}$ in spherical coordinates

::: {.important}
$$\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi$$
$$A=\sqrt{A_R^2+A_\theta^2+A_\phi^2}$$
:::

- Position vector

```{.figure #m01-spherical-position caption=""}
```

$$\vect{R}=R_1\uvec{R}$$

- Differential length $\ELto$ **vector**

$$\dif\vect{\ell}=\uvec{R}\,dR+\uvec{\theta}\,R\,d\theta+\uvec{\phi}\,R\sin\theta\,d\phi$$

- Differential surface $\ELto$ **vector**

$$d\vect{S}=R^2\sin\theta\,d\theta\,d\phi\,\uvec{R},\qquad d\vect{S}=R\sin\theta\,dR\,d\phi\,\uvec{\theta},\qquad d\vect{S}=R\,dR\,d\theta\,\uvec{\phi}$$

- Differential volume $\ELto$ **scalar**

$$dv=R^2\sin\theta\,dR\,d\theta\,d\phi$$

```{.figure #m01-spherical-differentials caption=""}
```

- Transformation of the representation of a vector from spherical to cylindrical coordinates

$$\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi\quad\Longrightarrow\quad\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z$$

```{.figure #m01-sph-cyl-units caption=""}
```

$$\uvec{R}=\sin\theta\,\uvec{r}+\cos\theta\,\uvec{z},\qquad \uvec{\theta}=\cos\theta\,\uvec{r}-\sin\theta\,\uvec{z},\qquad \uvec{\phi}=\uvec{\phi}$$

$$\begin{aligned}\vect{A}&=(\sin\theta\,\uvec{r}+\cos\theta\,\uvec{z})A_R\\&\quad+(\cos\theta\,\uvec{r}-\sin\theta\,\uvec{z})A_\theta\\&\quad+\uvec{\phi}A_\phi\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{r}(\sin\theta\,A_R+\cos\theta\,A_\theta)\\&\quad+\uvec{\phi}A_\phi\\&\quad+\uvec{z}(\cos\theta\,A_R-\sin\theta\,A_\theta)\end{aligned}$$

- Transformation of the representation of a vector from cylindrical to spherical coordinates

$$\vect{A}=\uvec{r}A_r+\uvec{\phi}A_\phi+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi$$

$$\uvec{r}=\sin\theta\,\uvec{R}+\cos\theta\,\uvec{\theta},\qquad \uvec{\phi}=\uvec{\phi},\qquad \uvec{z}=\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta}$$

$$\begin{aligned}\vect{A}&=(\sin\theta\,\uvec{R}+\cos\theta\,\uvec{\theta})A_r\\&\quad+\uvec{\phi}A_\phi\\&\quad+(\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta})A_z\end{aligned}\quad\Longrightarrow\quad\begin{aligned}\vect{A}&=\uvec{R}(\sin\theta\,A_r+\cos\theta\,A_z)\\&\quad+\uvec{\theta}(\cos\theta\,A_r-\sin\theta\,A_z)\\&\quad+\uvec{\phi}A_\phi\end{aligned}$$

- Transformation of the representation of a vector from spherical to cylindrical coordinates

::: {.important}
$$\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}=\begin{bmatrix}\sin\theta&\cos\theta&0\\0&0&1\\\cos\theta&-\sin\theta&0\end{bmatrix}\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}$$
:::

- Transformation of the representation of a vector from cylindrical to spherical coordinates

::: {.important}
$$\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}=\begin{bmatrix}\sin\theta&0&\cos\theta\\\cos\theta&0&-\sin\theta\\0&1&0\end{bmatrix}\begin{bmatrix}A_r\\A_\phi\\A_z\end{bmatrix}$$
:::

- Transformation of the representation of a vector from Cartesian to spherical coordinates

$$\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z\quad\Longrightarrow\quad\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi$$

$$\left\{\begin{aligned}\uvec{x}&=\cos\phi\,\uvec{r}-\sin\phi\,\uvec{\phi}\\\uvec{y}&=\sin\phi\,\uvec{r}+\cos\phi\,\uvec{\phi}\\\uvec{z}&=\uvec{z}\end{aligned}\right.\qquad\left\{\begin{aligned}\uvec{r}&=\sin\theta\,\uvec{R}+\cos\theta\,\uvec{\theta}\\\uvec{\phi}&=\uvec{\phi}\\\uvec{z}&=\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta}\end{aligned}\right.$$

$$\Longrightarrow\quad\left\{\begin{aligned}\uvec{x}&=\sin\theta\cos\phi\,\uvec{R}+\cos\theta\cos\phi\,\uvec{\theta}-\sin\phi\,\uvec{\phi}\\\uvec{y}&=\sin\theta\sin\phi\,\uvec{R}+\cos\theta\sin\phi\,\uvec{\theta}+\cos\phi\,\uvec{\phi}\\\uvec{z}&=\cos\theta\,\uvec{R}-\sin\theta\,\uvec{\theta}\end{aligned}\right.$$

::: {.important}
$$\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}=\begin{bmatrix}\sin\theta\cos\phi&\sin\theta\sin\phi&\cos\theta\\\cos\theta\cos\phi&\cos\theta\sin\phi&-\sin\theta\\-\sin\phi&\cos\phi&0\end{bmatrix}\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}$$
:::

- Transformation of the representation of a vector from spherical to Cartesian coordinates

$$\vect{A}=\uvec{R}A_R+\uvec{\theta}A_\theta+\uvec{\phi}A_\phi\quad\Longrightarrow\quad\vect{A}=\uvec{x}A_x+\uvec{y}A_y+\uvec{z}A_z$$

$$\left\{\begin{aligned}\uvec{R}&=\sin\theta\,\uvec{r}+\cos\theta\,\uvec{z}\\\uvec{\theta}&=\cos\theta\,\uvec{r}-\sin\theta\,\uvec{z}\\\uvec{\phi}&=\uvec{\phi}\end{aligned}\right.\qquad\left\{\begin{aligned}\uvec{r}&=\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y}\\\uvec{\phi}&=-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y}\\\uvec{z}&=\uvec{z}\end{aligned}\right.$$

$$\Longrightarrow\quad\left\{\begin{aligned}\uvec{R}&=\sin\theta\cos\phi\,\uvec{x}+\sin\theta\sin\phi\,\uvec{y}+\cos\theta\,\uvec{z}\\\uvec{\theta}&=\cos\theta\cos\phi\,\uvec{x}+\cos\theta\sin\phi\,\uvec{y}-\sin\theta\,\uvec{z}\\\uvec{\phi}&=-\sin\phi\,\uvec{x}+\cos\phi\,\uvec{y}\end{aligned}\right.$$

::: {.important}
$$\begin{bmatrix}A_x\\A_y\\A_z\end{bmatrix}=\begin{bmatrix}\sin\theta\cos\phi&\cos\theta\cos\phi&-\sin\phi\\\sin\theta\sin\phi&\cos\theta\sin\phi&\cos\phi\\\cos\theta&-\sin\theta&0\end{bmatrix}\begin{bmatrix}A_R\\A_\theta\\A_\phi\end{bmatrix}$$
:::

- Transformation from cylindrical to spherical coordinates

$$R=\sqrt{r^2+z^2},\qquad \theta=\tan^{-1}\frac{r}{z},\qquad \phi=\phi$$

- Transformation from spherical to cylindrical coordinates

$$r=R\sin\theta,\qquad \phi=\phi,\qquad z=R\cos\theta$$

- Transformation from spherical to Cartesian coordinates

$$x=R\sin\theta\cos\phi,\qquad y=R\sin\theta\sin\phi,\qquad z=R\cos\theta$$

- Transformation from Cartesian to spherical coordinates

$$R=\sqrt{x^2+y^2+z^2},\qquad \theta=\tan^{-1}\frac{\sqrt{x^2+y^2}}{z},\qquad \phi=\tan^{-1}\frac{y}{x}$$

```{.figure #m01-sph-coords caption=""}
```

## Integrals Containing Vector Functions

```{.figure #m01-vector-analysis-map-calc caption=""}
```

- The kinds of integrals containing vector functions that we deal with

$$\int_C\vect{F}\,d\ell\qquad \iint_S\vect{F}\,ds\qquad \iiint_V\vect{F}\,dv$$
$$\int_C V\,\dif\vect{\ell}$$
$$\int_C\vect{F}\cdot\dif\vect{\ell}\qquad \iint_S\vect{A}\cdot d\vect{s}$$
$$\int_C\vect{F}\times\dif\vect{\ell}$$

::: {.remark}
Important points about integration involving vector functions

- Using an appropriate coordinate system
- Correct determination of the differential length, surface and volume
- Attention to the variation of the unit vectors $\uvec{r}$, $\uvec{R}$, $\uvec{\theta}$ and $\uvec{\phi}$ over the range of integration
:::

- The integral of a vector function over a specified curve, surface and volume

$$\int_C\vect{F}\,d\ell\qquad \iint_S\vect{F}\,ds\qquad \iiint_V\vect{F}\,dv$$

- The result is a vector.
- Important applications in electromagnetics: computing the electric field intensity due to a line, surface and volume charge distribution

$$\left\{\begin{aligned}\vect{E}&=\frac{1}{4\pi\varepsilon_0}\int_C\frac{\rho_\ell\,d\ell'(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}\\\vect{E}&=\frac{1}{4\pi\varepsilon_0}\iint_S\frac{\rho_s\,ds'(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}\\\vect{E}&=\frac{1}{4\pi\varepsilon_0}\iiint_V\frac{\rho_v\,dv'(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}\end{aligned}\right.$$

::: {.example number="1-9"}
Evaluate the following integral over the curve $C$.
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

- The integral of a scalar function along a specified path

$$\int_C V\,\dif\vect{\ell}$$

- The result is a vector.
- Important applications in electromagnetics: computing the magnetic potential due to a line current

$$\vect{A}=\frac{\mu_0I}{4\pi}\oint_C\frac{\dif\vect{\ell}'}{\abs{\vect{R}-\vect{R}'}}$$

::: {.example number="1-10"}
Evaluate the following integral along the following paths

$$\int_O^P r^2\,\dif\vect{\ell},\qquad r^2=x^2+y^2$$

- Path $OP$
- Path $OP_1P$
- Path $OP_2P$

```{.figure #m01-ex10 caption=""}
```

::: {.solution}
- Along the path $OP$

$$\begin{aligned}\int_O^P r^2\,\dif\vect{\ell}&=\uvec{r}\int_0^{\sqrt2}r^2\,dr=\uvec{r}\,\frac{2\sqrt2}{3}\\&=\frac{2\sqrt2}{3}(\uvec{x}\cos45^\circ+\uvec{y}\sin45^\circ)\\&=\uvec{x}\frac23+\uvec{y}\frac23\end{aligned}$$

- Along the path $OP_1P$

$$\begin{aligned}\int_O^P(x^2+y^2)\,\dif\vect{\ell}&=\uvec{y}\int_O^{P_1}y^2\,dy+\uvec{x}\int_{P_1}^P(x^2+1)\,dx\\&=\uvec{y}\tfrac13y^3\Big|_0^1+\uvec{x}\left(\tfrac13x^3+x\right)\Big|_0^1\\&=\uvec{x}\frac43+\uvec{y}\frac13\end{aligned}$$

- Along the path $OP_2P$

$$\begin{aligned}\int_O^P(x^2+y^2)\,\dif\vect{\ell}&=\uvec{x}\int_O^{P_2}x^2\,dx+\uvec{y}\int_{P_2}^P(1+y^2)\,dy\\&=\uvec{x}\tfrac13x^3\Big|_0^1+\uvec{y}\left(y+\tfrac13y^3\right)\Big|_0^1\\&=\uvec{x}\frac13+\uvec{y}\frac43\end{aligned}$$
:::
:::

- Scalar line integral

$$\int_C\vect{F}\cdot\dif\vect{\ell}$$

- The result is a scalar.
- If $\vect{F}$ is a force
    - the work done by the force in moving a body from point $P_1$ to point $P_2$ along the specified path $C$
- Important applications in electromagnetics
    - Computing the electric potential difference between the points $P_1$ and $P_2$:
$$V=-\int_{P_1}^{P_2}\vect{E}\cdot\dif\vect{\ell}$$

    - Ampère's circuital law:
$$\mu_0I=-\oint_C\vect{B}\cdot\dif\vect{\ell}$$

::: {.example number="1-11"}
Evaluate the following integral along the quarter-circle path of the figure.

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

- Scalar surface integral

$$\iint_S\vect{A}\cdot d\vect{s}$$

- The result is a scalar.
- Result of the integral $\ELto$ the flux of the vector field $\vect{A}$ passing through the surface $S$
- Vector differential surface

$$d\vect{s}=\uvec{n}\,ds$$

```{.figure #m01-surface-normals caption="Direction of $\\mathbf{a}_n$ for a closed surface: normal to the surface, pointing out of the volume; for an open surface: depends on the direction of travel along the rim of the open surface, by the right-hand rule"}
```

- Important applications in electromagnetics
    - Gauss's law in free space:
$$\oiint_S\vect{E}\cdot d\vect{s}=\frac{Q}{\varepsilon_0}$$

    - Computing the electric current:
$$\iint_S\vect{J}\cdot d\vect{s}=I$$

::: {.example number="1-12"}
Evaluate the following integral over the closed surface about the $z$-axis specified by $z=\pm3$ and $r=2$

$$\oint_S\vect{F}\cdot d\vect{s},\qquad \vect{F}=\uvec{r}\frac{k_1}{r}+\uvec{z}k_2z$$

```{.figure #m01-ex12 caption=""}
```

::: {.solution}
$$\oint_S\vect{F}\cdot d\vect{s}=\oint_S\vect{F}\cdot\uvec{n}\,ds=\int_{\substack{\text{top}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds+\int_{\substack{\text{bottom}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds+\int_{\substack{\text{side}\\\text{wall}}}\vect{F}\cdot\uvec{n}\,ds$$

- Top face

$$z=3,\quad \uvec{n}=\uvec{z},\quad \vect{F}\cdot\uvec{n}=k_2z=3k_2,\quad ds=r\,dr\,d\phi$$
$$\int_{\substack{\text{top}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds=\int_0^{2\pi}\!\!\int_0^2 3k_2\,r\,dr\,d\phi=12\pi k_2$$

- Bottom face

$$z=-3,\quad \uvec{n}=-\uvec{z},\quad \vect{F}\cdot\uvec{n}=-k_2z=3k_2,\quad ds=r\,dr\,d\phi$$
$$\int_{\substack{\text{bottom}\\\text{face}}}\vect{F}\cdot\uvec{n}\,ds=12\pi k_2$$

- Side wall

$$r=2,\quad \uvec{n}=\uvec{r},\quad \vect{F}\cdot\uvec{n}=\frac{k_1}{r}=\frac{k_1}{2},\quad ds=r\,d\phi\,dz=2\,d\phi\,dz$$
$$\int_{\substack{\text{side}\\\text{wall}}}\vect{F}\cdot\uvec{n}\,ds=\int_{-3}^3\!\int_0^{2\pi}k_1\,d\phi\,dz=12\pi k_1$$

$$\oint_S\vect{F}\cdot d\vect{s}=12\pi k_2+12\pi k_2+12\pi k_1=12\pi(k_1+2k_2)$$
:::
:::

- Vector line integral

$$\int_C\vect{F}\times\dif\vect{\ell}$$

- The result is a vector.
- Important applications in electromagnetics
    - Biot–Savart law:
$$\vect{B}=\frac{\mu_0I}{4\pi}\oint_C\frac{\dif\vect{\ell}\times(\vect{R}-\vect{R}')}{\abs{\vect{R}-\vect{R}'}^3}$$

    - Computing the magnetic force on a current-carrying wire in a magnetic field:
$$\vect{F}=I\oint_C\dif\vect{\ell}\times\vect{B}$$

::: {.example number="1-13"}
Evaluate the following integral along the path $C$.

$$\int_C\vect{F}\times\dif\vect{\ell},\qquad \vect{F}=2\uvec{z}$$

```{.figure #m01-ex13 caption=""}
```

::: {.solution}
$$\dif\vect{\ell}=r\,d\phi\,\uvec{\phi}=a\,d\phi\,\uvec{\phi}$$
$$\begin{aligned}\int_C\vect{F}\times\dif\vect{\ell}&=\int_{2\pi}^0 2\uvec{z}\times a\,d\phi\,\uvec{\phi}=-2a\int_{2\pi}^0\uvec{r}\,d\phi\\&=-2a\int_{2\pi}^0(\cos\phi\,\uvec{x}+\sin\phi\,\uvec{y})\,d\phi=0\end{aligned}$$
:::
:::

## Differential Operations - Gradient

- **Prerequisite concepts for the discussion of the gradient**
    - The concept of the derivative of a function of one variable
        - The rate of change of the function at the point of interest
    - The concept of the directional derivative of a function of several variables
        - The rate of change of the function at the point of interest and in a specified direction

```{.figure #m01-derivative-concepts caption=""}
```

::: {.definition title="Gradient"}
The gradient of a **scalar quantity** is a **vector quantity** that lies in the direction in which the scalar quantity increases most, and whose magnitude equals the maximum rate of increase of the scalar quantity.

$$\operatorname{grad}v=\nabla v=\uvec{n}\frac{dv}{dn}$$
:::

- The directional derivative of $v$ in the direction of $\dif\vect{\ell}$:

$$\frac{dv}{d\ell}=\nabla v\cdot\uvec{\ell}$$

- The gradient of $v$ is normal to the surfaces of constant $v$.

```{.figure #m01-gradient-map caption=""}
```

- The gradient in Cartesian coordinates is as follows

::: {.important}
$$\nabla v=\frac{\partial v}{\partial x}\uvec{x}+\frac{\partial v}{\partial y}\uvec{y}+\frac{\partial v}{\partial z}\uvec{z}$$
:::

- The general expression of the gradient

::: {.important}
$$\nabla V=\uvec{u_1}\frac{\partial V}{h_1\,\partial u_1}+\uvec{u_2}\frac{\partial V}{h_2\,\partial u_2}+\uvec{u_3}\frac{\partial V}{h_3\,\partial u_3}$$
:::

| Metric coefficients | Cartesian | Cylindrical | Spherical |
|---|---|---|---|
| $h_1$ | $1$ | $1$ | $1$ |
| $h_2$ | $1$ | $r$ | $R$ |
| $h_3$ | $1$ | $1$ | $R\sin\theta$ |

- **The concept of the gradient**
    - Representing a hill by contours of height $\ELto$ $h(x,y)$
    - If a ball is placed at point $P$, in which direction does it move and what is the magnitude of the force acting on it?
        - The answer is proportional to $-\nabla h$.

```{.figure #m01-gradient-hill caption=""}
```

::: {.example number="1-14"}
The electric field intensity $\vect{E}$ can be obtained as the negative of the gradient of the scalar electric potential $V$. Find $\vect{E}$ at the point $(1,1,0)$ if
$$V=E_0R\cos\theta$$

::: {.solution}
$$\vect{E}=-\nabla V$$
$$\begin{aligned}\vect{E}&=-\left[\uvec{R}\frac{\partial}{\partial R}+\uvec{\theta}\frac{\partial}{R\,\partial\theta}+\uvec{\phi}\frac{\partial}{R\sin\theta\,\partial\phi}\right]E_0R\cos\theta\\&=-(\uvec{R}\cos\theta-\uvec{\theta}\sin\theta)E_0\end{aligned}$$
$$\vect{E}=-\uvec{z}E_0$$
:::
:::

## Differential Operations - Divergence

- **Prerequisite concepts for the discussion of the divergence**
    - In studying vector fields it is easier to represent the variations of the field graphically by flux lines. These are directed lines or curves that indicate the direction of the vector field at each point.

```{.figure #m01-flux-lines caption=""}
```

- The flux of a vector field is analogous to the flow of a fluid such as water.
- If $\vect{A}$ is a flux density vector, the total flux leaving the surface $S$ equals

$$\oint_S\vect{A}\cdot d\vect{s}$$

- In a volume with a closed surface, there will be an excess of inward or outward flux only when the volume contains a sink or a source, respectively.
    - The net outward flux from $v_a$ is positive: there is a source in the volume $v_a$
    - The net outward flux from $v_b$ is negative: there is a sink in the volume $v_b$
    - The net outward flux from $v_c$ is zero.

```{.figure #m01-source-sink caption=""}
```

::: {.definition title="Divergence"}
The divergence of a **vector field** $\vect{A}$ at a point is the net outward flux of $\vect{A}$ per unit volume as the volume about the point tends to zero

$$\operatorname{div}\vect{A}\triangleq\lim_{\Delta v\to0}\frac{\oint_S\vect{A}\cdot d\vect{s}}{\Delta v}$$
:::

- In Cartesian coordinates the divergence is as follows

::: {.important}
$$\operatorname{div}\vect{A}=\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}\qquad\qquad \nabla\cdot\vect{A}\equiv\operatorname{div}\vect{A}$$
:::

- The general expression of the divergence

::: {.important}
$$\nabla\cdot\vect{A}=\frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial u_1}(h_2h_3A_1)+\frac{\partial}{\partial u_2}(h_1h_3A_2)+\frac{\partial}{\partial u_3}(h_1h_2A_3)\right]$$
:::

::: {.example number="1-15"}
The magnetic flux density $\vect{B}$ outside a long current-carrying wire is circular and inversely proportional to the distance from the axis of the wire. Find the divergence of $\vect{B}$.

::: {.solution}
- Assuming the wire coincides with the $z$-axis

$$\vect{B}=\uvec{\phi}\frac{k}{r}$$
$$\nabla\cdot\vect{B}=\frac1r\frac{\partial}{\partial r}(rB_r)+\frac1r\frac{\partial B_\phi}{\partial\phi}+\frac{\partial B_z}{\partial z}$$
$$\nabla\cdot\vect{B}=0$$

```{.figure #m01-ex15 caption=""}
```
:::
:::

## Differential Operations - Curl

- **Prerequisite concepts for the discussion of the curl**
    - The circulation of a vector field around a closed path

$$\text{Circulation of }\vect{A}\text{ around contour }C\triangleq\oint_C\vect{A}\cdot\dif\vect{\ell}$$

- The physical meaning of the circulation depends on the kind of field that the vector $\vect{A}$ represents.
    - If $\vect{A}$ is the force acting on a body, the circulation of $\vect{A}$ is the work done by the force in moving the body around the path.

::: {.definition title="Curl"}
The curl of a **vector field** $\vect{A}$ at a point is a **vector** whose magnitude is the maximum net circulation of $\vect{A}$ per unit area as the area about the point tends to zero, and whose direction is the direction of the normal to the area when the area is oriented so as to make the net circulation maximum.

$$\operatorname{curl}\vect{A}\equiv\nabla\times\vect{A}\triangleq\lim_{\Delta s\to0}\frac{1}{\Delta s}\left[\uvec{n}\oint_C\vect{A}\cdot\dif\vect{\ell}\right]_{\max}$$
:::

- In Cartesian coordinates the curl is as follows

::: {.important}
$$\nabla\times\vect{A}=\begin{vmatrix}\uvec{x}&\uvec{y}&\uvec{z}\\[1mm]\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\[3mm]A_x&A_y&A_z\end{vmatrix}$$
:::

- The general expression of the curl

::: {.important}
$$\nabla\times\vect{A}=\frac{1}{h_1h_2h_3}\begin{vmatrix}\uvec{u_1}h_1&\uvec{u_2}h_2&\uvec{u_3}h_3\\[1mm]\dfrac{\partial}{\partial u_1}&\dfrac{\partial}{\partial u_2}&\dfrac{\partial}{\partial u_3}\\[3mm]h_1A_1&h_2A_2&h_3A_3\end{vmatrix}$$
:::

- **The concept of the curl**
    - The rotation of a paddle wheel in a stream of water with velocity vector $u$
        - The maximum angular velocity of the paddle wheel is proportional to the magnitude of the curl of the velocity vector.
        - The axis of the wheel, by the right-hand rule, lies in the direction of the curl.

```{.figure #m01-paddle-wheel caption=""}
```

::: {.example number="1-16"}
Find the curl of the following vector
$$\vect{A}=\uvec{\phi}\left(\frac{k}{r}\right)$$

::: {.solution}
$$\nabla\times\vect{A}=\frac1r\begin{vmatrix}\uvec{r}&\uvec{\phi}r&\uvec{z}\\[1mm]\dfrac{\partial}{\partial r}&\dfrac{\partial}{\partial\phi}&\dfrac{\partial}{\partial z}\\[3mm]0&k&0\end{vmatrix}=0$$

```{.figure #m01-ex16 caption=""}
```
:::
:::

## Important Vector Theorems

```{.figure #m01-vector-analysis-map-thm caption=""}
```

::: {.theorem title="Divergence theorem"}
The volume integral of the divergence of a vector field equals the total outward flux of the vector through the surface enclosing the volume.
$$\int_V\nabla\cdot\vect{A}\,dv=\oint_S\vect{A}\cdot d\vect{s}$$
:::

```{.figure #m01-divergence-theorem caption=""}
```

::: {.theorem title="Stokes's theorem"}
The surface integral of the curl of a vector field over an open surface equals the closed line integral of the vector along the contour bounding the surface.
$$\int_S(\nabla\times\vect{A})\cdot d\vect{s}=\oint_C\vect{A}\cdot\dif\vect{\ell}$$
:::

```{.figure #m01-stokes-theorem caption=""}
```

::: {.theorem title="Helmholtz's theorem"}
A vector field is determined to within an additive constant if both its divergence and its curl are specified.
:::

::: {.example number="1-17"}
Verify the divergence theorem for the shell region enclosed by the spherical surfaces $R=R_1$ and $R=R_2$ $(R_2>R_1)$ centred at the origin, for the following vector field.
$$\vect{F}=\uvec{R}kR$$

```{.figure #m01-ex17 caption=""}
```

::: {.solution}
$$\int_V\nabla\cdot\vect{A}\,dv=\oint_S\vect{A}\cdot d\vect{s}$$

- For the outer surface

$$R=R_2,\qquad d\vect{s}=\uvec{R}R_2^2\sin\theta\,d\theta\,d\phi$$
$$\int_{\substack{\text{outer}\\\text{surface}}}\vect{F}\cdot d\vect{s}=\int_0^{2\pi}\!\!\int_0^\pi(kR_2)R_2^2\sin\theta\,d\theta\,d\phi=4\pi kR_2^3$$

- For the inner surface

$$R=R_1,\qquad d\vect{s}=-\uvec{R}R_1^2\sin\theta\,d\theta\,d\phi$$
$$\int_{\substack{\text{inner}\\\text{surface}}}\vect{F}\cdot d\vect{s}=-\int_0^{2\pi}\!\!\int_0^\pi(kR_1)R_1^2\sin\theta\,d\theta\,d\phi=-4\pi kR_1^3$$

$$\oint_S\vect{F}\cdot d\vect{s}=4\pi k(R_2^3-R_1^3)$$
$$\nabla\cdot\vect{F}=\frac{1}{R^2}\frac{\partial}{\partial R}(R^2F_R)=\frac{1}{R^2}\frac{\partial}{\partial R}(kR^3)=3k$$
$$\int_V\nabla\cdot\vect{F}\,dv=(\nabla\cdot\vect{F})V=4\pi k(R_2^3-R_1^3)$$
:::
:::

::: {.example number="1-18"}
Verify Stokes's theorem over a quarter of a circular disk of radius 3 in the first quadrant for the following vector field.
$$\vect{F}=\uvec{x}xy-\uvec{y}2x$$

```{.figure #m01-ex18 caption=""}
```

::: {.solution}
$$\int_S(\nabla\times\vect{A})\cdot d\vect{s}=\oint_C\vect{A}\cdot\dif\vect{\ell}$$
$$\nabla\times\vect{F}=\begin{vmatrix}\uvec{x}&\uvec{y}&\uvec{z}\\[1mm]\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\[3mm]xy&-2x&0\end{vmatrix}=-\uvec{z}(2+x)$$
$$\int_S(\nabla\times\vect{F})\cdot d\vect{s}=\int_0^{\pi/2}\!\!\int_0^3-\uvec{z}(2+r\cos\phi)\cdot r\,dr\,d\phi\,\uvec{z}=-9\left(1+\frac{\pi}{2}\right)$$

- From $B$ to $O$

$$x=0,\ \text{and}\ \vect{F}\cdot\dif\vect{\ell}=\vect{F}\cdot(\uvec{y}\,dy)=2x\,dy=0$$

- From $O$ to $A$

$$y=0,\ \text{and}\ \vect{F}\cdot\dif\vect{\ell}=\vect{F}\cdot(\uvec{x}\,dx)=xy\,dx=0$$

$$\oint_{ABOA}\vect{F}\cdot\dif\vect{\ell}=\int_A^B\vect{F}\cdot\dif\vect{\ell}=-9\left(1+\frac{\pi}{2}\right)$$

(examined in Example \ELnumc{1-11})
:::
:::

## Important Vector Identities

::: {.important title="Identity I"}
The curl of the gradient of any scalar quantity is zero
$$\nabla\times(\nabla V)\equiv0$$
:::

- A curl-free vector field is called an **irrotational** or **conservative** field.
- If a vector quantity is curl-free, it can be expressed as the gradient of a scalar quantity.

::: {.important title="Identity II"}
The divergence of the curl of any vector field is zero.
$$\nabla\cdot(\nabla\times\vect{A})\equiv0$$
:::

- A divergence-free vector field is called a **solenoidal** field.
- If a vector quantity is divergence-free, it can be expressed as the curl of a vector quantity.
