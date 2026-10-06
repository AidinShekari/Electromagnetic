# Steady Electric Currents

## Course Outline

```{.figure #m04-course-outline caption=""}
```

## Steady Electric Currents

- In the previous chapters we dealt with electrostatic problems due to electric charges at rest.
    - In this chapter we turn to moving electric charges, which produce electric current.
- Electric currents due to the motion of free charges are divided into three kinds
    - **Conduction currents:** produced in conductors and semiconductors by the drift motion of electrons or holes.
    - **Electrolytic currents:** due to the motion of positive and negative ions
    - **Convection currents:** due to the motion of electrons or ions in vacuum
- In this chapter we concentrate on conduction currents, which are governed by Ohm's law.

```{.figure #m04-map caption=""}
```

- What is the concept of the **volume current density**, and what is the relation for the **convection current density**?
- What is the relation for the **conduction current density**?
- What is the point form of **Ohm's law**?
- What is the **equation of continuity**, and how is **Kirchhoff's current law** derived from it?
- What is **Joule's law**, which gives the power dissipated by a current flowing in a conducting body?

## Current Density and Ohm's Law

```{.figure #m04-current-element caption=""}
```

- Consider the steady motion of charge carriers, each with charge $q$, moving with velocity $\vect{u}$ across a small surface element $\Delta s$
- If $N$ is the number of charge carriers per unit volume, the charge passing through the surface $\Delta s$ in the time $\Delta t$ is

$$\Delta Q=Nq\vect{u}\cdot\uvec{n}\,\Delta s\,\Delta t\qquad(\mathrm{C})$$

- Since current is the time rate of change of charge, we have

$$\Delta I=\frac{\Delta Q}{\Delta t}=Nq\vect{u}\cdot\uvec{n}\,\Delta s=Nq\vect{u}\cdot\Delta\vect{s}\qquad(\mathrm{A})$$

- We define the volume current density, in amperes per square metre, as follows

$$\vect{J}=Nq\vect{u}\qquad(\mathrm{A/m^2})$$

::: {.important title="Convection current density"}
$$\vect{J}=\rho\vect{u}\qquad(\mathrm{A/m^2})$$
:::

- Therefore

$$\Delta I=\vect{J}\cdot\Delta\vect{s}$$

- Thus the total current flowing through an arbitrary surface $S$ is

::: {.important}
$$I=\int_S\vect{J}\cdot d\vect{s}\qquad(\mathrm{A})$$
:::

- Conduction currents are the result of the drift motion of charge carriers under the influence of an applied electric field.
- For most conducting materials the average drift velocity is directly proportional to the electric field intensity.
    - For metallic conductors we have

$$\vect{u}=-\mu_e\vect{E}\qquad(\mathrm{m/s})$$

- $\mu_e$: electron mobility, in $\mathrm{m^2/V\cdot s}$

$$\vect{J}=-\rho_e\mu_e\vect{E}$$

- $\rho_e=-Ne$: the volume charge density of the drifting electrons, a negative quantity

::: {.important title="Point form of Ohm's law"}
$$\vect{J}=\sigma\vect{E}\qquad(\mathrm{A/m^2})$$
:::

- $\sigma=-\rho_e\mu_e$: a fundamental parameter of the medium, called the conductivity
- The unit of conductivity is $\mathrm{A/V\cdot m}$, or siemens per metre. The reciprocal of conductivity is called resistivity, in $\Omega\cdot\mathrm{m}$.

- Obtaining the relation between the voltage and the current of a piece of homogeneous material of conductivity $\sigma$, length $\ell$ and uniform cross-section $S$ from the point form of Ohm's law

```{.figure #m04-resistor caption=""}
```

$$\left.\begin{aligned}V_{12}=E\ell\quad&\Longrightarrow\quad E=\frac{V_{12}}{\ell}\\I=\int_S\vect{J}\cdot d\vect{s}=JS\quad&\Longrightarrow\quad J=\frac IS\end{aligned}\right\}\quad\frac IS=\sigma\frac{V_{12}}{\ell}$$
$$V_{12}=\left(\frac{\ell}{\sigma S}\right)I=RI$$

::: {.important}
$$R=\frac{\ell}{\sigma S}\qquad(\Omega)$$
$$G=\frac1R=\sigma\frac S\ell\qquad(\mathrm{S})$$
:::

- $G$: conductance, the reciprocal of resistance, in mhos or siemens

## Equation of Continuity and Kirchhoff's Current Law

```{.figure #m04-map-continuity caption=""}
```

- The principle of conservation of charge is one of the fundamental postulates of physics.
    - Electric charge can be neither created nor destroyed.
- Consider an arbitrary volume $V$ bounded by the surface $S$, containing a net charge $Q$. If a net current $I$ flows out of the region through the surface, the charge in the volume must decrease at a rate equal to the current. Conversely, if a net current flows into the region through the surface, the charge in the volume must increase at a rate equal to the current.
- The current leaving the region is the total outward flux of the current density vector through the surface $S$

$$I=\oint_S\vect{J}\cdot d\vect{s}=-\frac{dQ}{dt}=-\frac{d}{dt}\int_V\rho\,dv$$
$$\int_V\nabla\cdot\vect{J}\,dv=-\int_V\frac{\partial\rho}{\partial t}\,dv$$

- Since the above equation must hold regardless of the choice of $V$

::: {.important title="Equation of continuity"}
$$\nabla\cdot\vect{J}=-\frac{\partial\rho}{\partial t}\qquad(\mathrm{A/m^3})$$
:::

- If there are no time variations

$$\nabla\cdot\vect{J}=0$$

::: {.important title="Kirchhoff's current law"}
$$\oint_S\vect{J}\cdot d\vect{s}=0$$
:::

- We said earlier that charges placed inside a conductor move to its surface, so that at equilibrium $\rho=0$ inside the conductor. We now want to prove this statement

$$\left.\begin{aligned}\sigma\nabla\cdot\vect{E}&=-\frac{\partial\rho}{\partial t}\\\nabla\cdot\vect{E}&=\rho/\epsilon\end{aligned}\right\}\quad\frac{\partial\rho}{\partial t}+\frac\sigma\epsilon\rho=0\quad\Longrightarrow\quad\rho=\rho_0e^{-(\sigma/\epsilon)t}\qquad(\mathrm{C/m^3})$$

- $\rho_0$: initial charge density
- The above equation states that the charge density at a given point decreases exponentially with time.
- The initial density decays to $1/e$, or $36.8\%$, of its value in a time equal to $\tau=\epsilon/\sigma$.
    - For a good conductor such as copper, $\tau=1.52\times10^{-19}\,\mathrm{s}$.
    - For a good insulator this time may be hours or days.

## Power Dissipation and Joule's Law

```{.figure #m04-map-joule caption=""}
```

- Under the influence of an electric field, the free electrons in a conductor move and collide with the atoms of the crystal lattice. Energy is thus transferred from the electric field to the vibrating atoms.
- The work done by the electric field in moving a charge $q$ through the distance $\Delta\ell$ is

$$\Delta W=\vect{F}\cdot\Delta\vect{\ell}=q\vect{E}\cdot\Delta\vect{\ell}$$

- This work corresponds to the power

$$p=\lim_{\Delta t\to0}\frac{\Delta w}{\Delta t}=q\vect{E}\cdot\vect{u}$$

- $\vect{u}$: the velocity of the charge carriers

$$dp=\rho\,dv\,\vect{E}\cdot\vect{u}$$
$$dP=\vect{E}\cdot\vect{J}\,dv$$

- For a given volume $V$ the total power converted into heat is

::: {.important title="Joule's law"}
$$P=\int_V\vect{E}\cdot\vect{J}\,dv\qquad(\mathrm{W})$$
:::

- In a conductor of constant cross-section we have

$$P=\int_LE\,d\ell\int_SJ\,ds=VI$$

::: {.important}
$$P=I^2R\qquad(\mathrm{W})$$
:::

- which is the familiar relation for ohmic power and gives the heat dissipated in the resistance $R$.

## Boundary Conditions for Current Density

```{.figure #m04-map-boundary caption=""}
```

- When a current crosses the interface between two media of different conductivities obliquely, the current density vector changes in both direction and magnitude.
- The governing equations for the steady current density are

**Governing Equations for Steady Current Density**

| Differential Form | Integral Form |
|---|---|
| $\nabla\cdot\vect{J}=0$ | $\oint_S\vect{J}\cdot d\vect{s}=0$ |
| $\nabla\times\left(\dfrac{\vect{J}}{\sigma}\right)=0$ | $\oint_C\dfrac1\sigma\vect{J}\cdot\dif\vect{\ell}=0$ |


- The boundary conditions are as follows

::: {.important}
$$\nabla\cdot\vect{J}=0\quad\Longrightarrow\quad J_{1n}=J_{2n}\qquad(\mathrm{A/m^2})$$
$$\nabla\times(\vect{J}/\sigma)=0\quad\Longrightarrow\quad\frac{J_{1t}}{J_{2t}}=\frac{\sigma_1}{\sigma_2}$$
:::

- When a steady current crosses the boundary between two different lossy dielectrics

$$J_{1n}=J_{2n}\to\sigma_1E_{1n}=\sigma_2E_{2n}$$
$$D_{1n}-D_{2n}=\rho_s\to\epsilon_1E_{1n}-\epsilon_2E_{2n}=\rho_s$$
$$\rho_s=\left(\epsilon_1\frac{\sigma_2}{\sigma_1}-\epsilon_2\right)E_{2n}=\left(\epsilon_1-\epsilon_2\frac{\sigma_1}{\sigma_2}\right)E_{1n}$$

- $E_{1n}=\uvec{n2}\cdot\vect{E}_1$ and $E_{2n}=\uvec{n2}\cdot\vect{E}_2$
- If medium 2 is a much better conductor than medium 1

$$\rho_s=\epsilon_1E_{1n}=D_{1n}$$

- which is the boundary condition of a conductor.

::: {.example number="4-1"}
A potential difference $\mathcal{V}$ is applied to a parallel-plate capacitor of area $S$. The space between the conducting plates is filled with two lossy dielectric materials of thicknesses $d_1$ and $d_2$, permittivities $\epsilon_1$ and $\epsilon_2$, and conductivities $\sigma_1$ and $\sigma_2$. Find

- (a) the electric field intensity in the two media
- (b) the current density in the two media
- (c) the surface charge densities on the conducting plates and at the interface of the two dielectrics

```{.figure #m04-ex1 caption=""}
```

::: {.solution}
- (a)

$$J_1=J_2\quad\Longrightarrow\quad\begin{aligned}\mathcal{V}&=E_1d_1+E_2d_2\\\sigma_1E_1&=\sigma_2E_2\end{aligned}$$
$$E_1=\frac{\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}\qquad E_2=\frac{\sigma_1\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$

- (b)

$$J_1=J_2=\sigma_1E_1=\sigma_2E_2=\frac{\sigma_1\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$

- (c)

$$\uvec{n}\cdot\vect{E}_1=\frac{\rho_{s1}}{\epsilon_1}\quad\Longrightarrow\quad\rho_{s1}=\epsilon_1E_1=\frac{\epsilon_1\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$
$$\uvec{n}\cdot\vect{E}_2=\frac{\rho_{s2}}{\epsilon_2}\quad\Longrightarrow\quad\rho_{s2}=-\epsilon_2E_2=-\frac{\epsilon_2\sigma_1\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}$$
$$\rho_{si}=\left(\epsilon_1-\epsilon_2\frac{\sigma_1}{\sigma_2}\right)E_{1n}\quad\Longrightarrow\quad\begin{aligned}\rho_{si}&=\left(\epsilon_2\frac{\sigma_1}{\sigma_2}-\epsilon_1\right)\frac{\sigma_2\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}\\&=\frac{(\epsilon_2\sigma_1-\epsilon_1\sigma_2)\mathcal{V}}{\sigma_2d_1+\sigma_1d_2}\qquad(\mathrm{C/m^2})\end{aligned}$$
:::
:::

## Resistance Calculations

```{.figure #m04-map-resistance caption=""}
```

- How is the **leakage resistance** of capacitive structures computed?
- How is the resistance of various structures computed?

- The capacitance between two conductors separated by a dielectric medium is

$$C=\frac QV=\frac{\oint_S\vect{D}\cdot d\vect{s}}{-\int_L\vect{E}\cdot\dif\vect{\ell}}=\frac{\oint_S\epsilon\vect{E}\cdot d\vect{s}}{-\int_L\vect{E}\cdot\dif\vect{\ell}}$$

- The surface integral is taken over a surface enclosing the positive conductor, and the line integral from the negative conductor to the positive conductor.
- If the dielectric medium is lossy, a current flows from the positive to the negative conductor. The resistance between the conductors (the leakage resistance) is

$$R=\frac VI=\frac{-\int_L\vect{E}\cdot\dif\vect{\ell}}{\oint_S\vect{J}\cdot d\vect{s}}=\frac{-\int_L\vect{E}\cdot\dif\vect{\ell}}{\oint_S\sigma\vect{E}\cdot d\vect{s}}$$

- If the permittivity and the conductivity have the same space dependence ($\epsilon(x,y,z)=k\sigma(x,y,z)$), or if the dielectric medium is homogeneous ($\epsilon$ and $\sigma$ independent of the space coordinates)

::: {.important}
$$RC=\frac CG=\frac\epsilon\sigma$$
:::

::: {.example number="4-2"}
Find the leakage resistance per unit length

- (a) between the inner and outer conductors of a coaxial cable with inner-conductor radius $a$, outer-conductor radius $b$ and a dielectric of conductivity $\sigma$
- (b) of a two-wire transmission line consisting of two wires of radius $a$ separated by $D$, in a medium of conductivity $\sigma$

::: {.solution}
- (a) The capacitance per unit length of a coaxial cable

$$C_1=\frac{2\pi\epsilon}{\ln(b/a)}\qquad(\mathrm{F/m})$$

- The leakage resistance per unit length

$$R_1=\frac\epsilon\sigma\left(\frac{1}{C_1}\right)=\frac{1}{2\pi\sigma}\ln\left(\frac ba\right)\qquad(\Omega\cdot\mathrm{m})$$

- (b) The capacitance per unit length of a two-wire transmission line

$$C'_1=\frac{\pi\epsilon}{\cosh^{-1}\left(\dfrac{D}{2a}\right)}\qquad(\mathrm{F/m})$$

- The leakage resistance per unit length

$$\begin{aligned}R'_1&=\frac\epsilon\sigma\left(\frac{1}{C'_1}\right)=\frac{1}{\pi\sigma}\cosh^{-1}\left(\frac{D}{2a}\right)\\&=\frac{1}{\pi\sigma}\ln\left[\frac{D}{2a}+\sqrt{\left(\frac{D}{2a}\right)^2-1}\right]\qquad(\Omega\cdot\mathrm{m})\end{aligned}$$
:::
:::

- In certain situations electrostatic and steady-current problems are not exactly analogous.
- **First method** for computing the resistance of a piece of conducting material between two surfaces or terminals
    - Choosing an appropriate coordinate system
    - Applying a potential difference $V_0$ between the two terminals
    - Finding the electric field intensity (if the material is homogeneous, by solving Laplace's equation for the electric potential and then computing the electric field intensity)
    - Finding the total current
$$I=\int_S\vect{J}\cdot d\vect{s}=\int_S\sigma\vect{E}\cdot d\vect{s}$$
    - $S$: the cross-section through which the current flows
    - The resistance is $V_0/I$

- **Second method** for computing the resistance of a piece of conducting material between two surfaces or terminals (when $J$ can easily be determined from $I$)
    - Choosing an appropriate coordinate system
    - Passing a current $I$ between the two terminals
    - Finding $J$ from $I$
    - Computing the electric field intensity $\vect{E}=\vect{J}/\sigma$ and the potential difference $V_0$
$$V_0=-\int\vect{E}\cdot\dif\vect{\ell}$$
        - The integration is carried out from the terminal at the lower potential to the terminal at the higher potential.
    - The resistance is $V_0/I$

::: {.example number="4-3"}
Consider a conducting material of uniform thickness $h$ and conductivity $\sigma$ in the shape shown in the figure below. Find the resistance between its two end faces.

```{.figure #m04-ex3 caption=""}
```

::: {.solution}
- Choosing cylindrical coordinates

$$V=0\quad\text{at}\quad\phi=0,\qquad V=V_0\quad\text{at}\quad\phi=\pi/2$$
$$\frac{d^2V}{d\phi^2}=0\quad\Longrightarrow\quad V=c_1\phi+c_2\quad\Longrightarrow\quad V=\frac{2V_0}{\pi}\phi$$
$$\begin{aligned}\vect{J}=\sigma\vect{E}&=-\sigma\nabla V\\&=-\uvec{\phi}\sigma\frac{\partial V}{r\,\partial\phi}=-\uvec{\phi}\frac{2\sigma V_0}{\pi r}\end{aligned}$$
$$\begin{aligned}I=\int_S\vect{J}\cdot d\vect{s}&=\int_0^h\!\!\int_a^b\left(-\uvec{\phi}\frac{2\sigma V_0}{\pi r}\right)\cdot\left(-\uvec{\phi}\,dr\,dz\right)\\&=\frac{2\sigma hV_0}{\pi}\ln\frac ba\end{aligned}$$
$$R=\frac{V_0}{I}=\frac{\pi}{2\sigma h\ln(b/a)}$$
:::
:::
