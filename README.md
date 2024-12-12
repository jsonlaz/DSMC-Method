# DSMC-Method

 ### Numerical illustrations using the Direct Simulation Monte Carlo method

<h2>Description</h2>
Numerical simulations to illustrate the analytical solutions to Kac's equation
and explore analytically intractable scenarios.
<br />

<h2>Kac equation</h2>

The Kac equation can be represented as:

![Kac Equation](https://latex.codecogs.com/svg.latex?\frac{\partial&space;f}{\partial&space;t}&space;+&space;v\&space;\frac{\partial&space;f}{\partial&space;x}&space;+&space;F\&space;\frac{\partial&space;f}{\partial&space;v}&space;=&space;Q(f,f))

where $f = f(t,\ v,\ x)$ is the distribution function, $F$ is the external force, $g(\theta) = g( - \theta)$ is the collision kernel, and $Q(f, f)$ is the collision operator.

The collision operator is a nonlinear integral operator that acts on $f(t,\ v,\ x)$ with respect to the velocity $v$ and describes the collision between particles.

We represent the collision operator as:

![Collision Operator](https://latex.codecogs.com/svg.latex?Q(f,f)&space;=&space;\int_{-&space;\infty}^{\infty}{\int_{-&space;\pi}^{\pi}{g(\theta)f(v'\&space;)f(v_{*}'\&space;)&space;d\theta\&space;dv_{*}}}&space;-&space;\int_{-&space;\infty}^{\infty}{\int_{-&space;\pi}^{\pi}{g(\theta)f(v)f(v_{*}\&space;)&space;d\theta\&space;dv_{*}}})

where $t \in \mathbb{R}$, $v,v_{*},x \in \mathbb{R}$.



<h2>Simplifications and assumptions</h2>

Given the complexity, we simplify the Kac equation for a feasible numerical illustration within this format.

We choose

![g(theta)](https://latex.codecogs.com/svg.latex?g(\theta)=\frac{1}{2\pi},\%20%5Clabel%7Beq%3A%20g%7D)

which implies a uniform distribution of scattering angles. This choice satisfies the normalization conditions for the collision kernel.

Furthermore, we consider other assumptions such as:

- Spatially homogeneous case: Ignoring spatial dependence $\left(\frac{\partial f}{\partial x}=0\right)$ to focus on the velocity distribution evolution over time.
- No external force: Setting $F=0$ to eliminate the acceleration term $\left(\frac{\partial f}{\partial v}\right)$.

Hence, we have the simplified Kac equation as:

![Kac Equation](https://latex.codecogs.com/svg.latex?\frac{\partial&space;f}{\partial&space;t}&space;=&space;Q(f,f)).

<h2>Direct Simulation Monte Carlo method</h2>

Using the Direct Simulation Monte Carlo method, we focus on how the distribution of particle velocities evolves with time according to the Kac model and how it compares to the equilibrium state described by the Maxwellian distribution.
<br />

To simulate particle collision and the relaxation towards equilibrium using the Direct Simulation Monte Carlo method, first input parameters such as the number of particles, the number of time steps to simulate, and the range for velocity. Simulate collisions by randomly pairing particles and updating their velocities. To do this, sample a random collision angle $\theta$ uniformly from $-\pi$ to $\pi$, then update the velocities of the particles based on the collision angle.

## Illustration 1

We consider a uniform initial distribution of $n = 10\times 10^4$ particles in our illustration.

![Uniform initial velocity distribution](https://raw.githubusercontent.com/jsonlaz/DSMC-method/main/results/uniform_initial.png)

![Final velocity distribution](https://raw.githubusercontent.com/jsonlaz/DSMC-method/main/results/uniform_final_dsmc.png)

This shows the evolution of a uniform initial distribution towards equilibrium (final velocity distribution) against a fixed range of velocities $v \in [-5,5]$.

## Illustration 2

We consider a triangular initial distribution of $n = 10\times 10^4$ particles in our illustration.

![Triangular initial velocity distribution](https://raw.githubusercontent.com/jsonlaz/DSMC-method/main/results/triangular_initial.png)

![Final velocity distribution](https://raw.githubusercontent.com/jsonlaz/DSMC-method/main/results/triangular_final_dsmc.png)

This present the evolution of a triangular initial distribution towards equilibrium against a fixed range of velocities $v \in [-5,5]$.

## Conclusion

Over time, due to the random nature of collisions, particle systems tend towards equilibrium characterized by a Maxwellian distribution regardless of the initial velocity distribution. The H-theorem,  which states that a system not in equilibrium will evolve over time reaching a maximum at equilibrium, provides a theoretical foundation for the behaviour of the gas velocity described by the Boltzmann equation to evolve towards equilibrium.








