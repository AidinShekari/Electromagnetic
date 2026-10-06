# Time-Varying Electromagnetic Fields

## Course Outline

```{.figure #m06-course-outline caption=""}
```

## Introduction

- The fundamental relations of electrostatics and magnetostatics

| Fundamental Relations | Electrostatic Model | Magnetostatic Model |
|---|:---:|:---:|
| Governing equations | $\nabla\times\vect{E}=0$, $\nabla\cdot\vect{D}=\rho$ | $\nabla\cdot\vect{B}=0$, $\nabla\times\vect{H}=\vect{J}$ |
| Constitutive relations (linear and isotropic media) | $\vect{D}=\epsilon\vect{E}$ | $\vect{H}=\dfrac1\mu\vect{B}$ |

- In the static (time-invariant) case, the electric field vectors and the magnetic field vectors form separate, independent pairs.
- We shall see that in the time-varying case a time-varying magnetic field produces an electric field, and vice versa

## Faraday's Law of Electromagnetic Induction

- In 1820 **Hans Christian Ørsted** showed that a wire carrying an electric current deflects a compass needle.
    - The motion of the compass needle was caused by the magnetic force of the magnetic field produced by the electric current.
- After this discovery **Michael Faraday** reasoned that a magnetic field should, in the same way, have an electric effect and produce a current in a wire.
- After about ten years of experiments he made the discovery known as Faraday's law of electromagnetic induction.

::: {.definition title="Faraday's law of electromagnetic induction"}
If the magnetic flux through a closed circuit changes with time, an electromotive force is induced in the circuit. This electromotive force drives a current.
:::

- The polarity of the electromotive force, and hence the direction of the induced current, can be found from Lenz's law.

::: {.definition title="Lenz's law"}
The current induced in a circuit always flows in the direction that opposes the change of the magnetic flux producing it.
:::

- The mathematical statement of Faraday's law of electromagnetic induction

::: {.important}
$$v_{emf}=-N\frac{d\Phi}{dt}=-N\frac{d}{dt}\int_S\vect{B}\cdot d\vect{s}$$
:::

- The definition of the electromotive force induced in a circuit with the closed contour $C$

$$v_{emf}\triangleq\oint_C\vect{E}\cdot\dif\vect{\ell}$$

- For a stationary circuit

$$v_{emf}=\oint_C\vect{E}\cdot\dif\vect{\ell}=-\int_S\frac{\partial\vect{B}}{\partial t}\cdot d\vect{s}\quad\Longrightarrow\quad\int_S(\nabla\times\vect{E})\cdot d\vect{s}=-\int_S\frac{\partial\vect{B}}{\partial t}\cdot d\vect{s}$$

- The last step uses Stokes's theorem.

::: {.important}
$$\nabla\times\vect{E}=-\frac{\partial\vect{B}}{\partial t}$$
:::

- In the time-varying case the electric field is not conservative $\ELto$ $\nabla\times\vect{E}\neq0$
- In the time-varying case the scalar potential cannot be defined as $V=-\int\vect{E}\cdot\dif\vect{\ell}$, because the potential difference between two points would depend on the path of integration and would not have a fixed value.
- At low frequencies $\ELto$ $\nabla\times\vect{E}\simeq0$ $\ELto$ the scalar potential can be defined (lumped-circuit theory)

::: {.example number="6-1"}
A circular loop of $N$ turns of conducting wire lies in the $xy$-plane with its centre at the origin, in a magnetic field given by

$$\vect{B}=\uvec{z}B_0\cos\left(\frac{\pi r}{2b}\right)\sin(\omega t)$$

Here $b$ is the radius of the loop and $\omega$ the angular frequency. Find the induced electromotive force.

::: {.solution}
$$\begin{aligned}\Phi=\int_S\vect{B}\cdot d\vect{s}&=\int_0^{2\pi}\!\!\int_0^b\left[B_0\cos\left(\frac{\pi r}{2b}\right)\sin(\omega t)\,\uvec{z}\right]\cdot\left(r\,dr\,d\phi\,\uvec{z}\right)\\&=\frac{8b^2}{\pi}\left(\frac\pi2-1\right)B_0\sin(\omega t)\end{aligned}$$
$$v=-N\frac{d\Phi}{dt}=-\frac{8Nb^2}{\pi}\left(\frac\pi2-1\right)B_0\omega\cos(\omega t)$$
:::
:::

## Displacement Current

- Ampère's circuital law for the static magnetic field

$$\nabla\times\vect{H}=\vect{J}$$

- **James Clerk Maxwell** doubted this equation, because

$$\nabla\cdot(\nabla\times\vect{H})=0=\nabla\cdot\vect{J}$$

- which is not consistent with the equation of continuity

$$\nabla\cdot\vect{J}=-\frac{\partial\rho}{\partial t}$$

- To remove this inconsistency Maxwell modified the relation as follows

$$\nabla\cdot(\nabla\times\vect{H})=0=\nabla\cdot\vect{J}+\frac{\partial\rho}{\partial t}\quad\xrightarrow{\ \nabla\cdot\vect{D}=\rho\ }\quad\nabla\cdot(\nabla\times\vect{H})=\nabla\cdot\left(\vect{J}+\frac{\partial\vect{D}}{\partial t}\right)$$

::: {.important}
$$\nabla\times\vect{H}=\vect{J}+\frac{\partial\vect{D}}{\partial t}$$
:::

- It can easily be shown that $\partial\vect{D}/\partial t$ has the dimension of a current density. It is called the **displacement current density**.
- The modified form of Ampère's circuital law states that a time-varying electric field produces a magnetic field even when there is no current.

## Maxwell's Equations

- The equations governing time-varying electric and magnetic fields, or **Maxwell's equations**

| Differential Form | Integral Form | Significance |
|---|---|---|
| $\nabla\times\vect{E}=-\dfrac{\partial\vect{B}}{\partial t}$ | $\oint_C\vect{E}\cdot\dif\vect{\ell}=-\dfrac{d\Phi}{dt}$ | Faraday's law |
| $\nabla\times\vect{H}=\vect{J}+\dfrac{\partial\vect{D}}{\partial t}$ | $\oint_C\vect{H}\cdot\dif\vect{\ell}=I+\int_S\dfrac{\partial\vect{D}}{\partial t}\cdot d\vect{s}$ | Ampère's circuital law |
| $\nabla\cdot\vect{D}=\rho$ | $\oint_S\vect{D}\cdot d\vect{s}=Q$ | Gauss's law |
| $\nabla\cdot\vect{B}=0$ | $\oint_S\vect{B}\cdot d\vect{s}=0$ | No isolated magnetic charge |
