# DSMC-Method

 ### Numerical illustrations using Direct Simulation Monte Carlo method

<h2>Description</h2>
Numerical simulations to illustrate the analytical solutions to the Kac's equation
and explore analytically intractable scenarios.
<br />

<h2>Kac equation</h2>
The Kac equation can be represented as:

![equation](https://latex.codecogs.com/svg.latex?\frac{\partial&space;f}{\partial&space;t}&space;+&space;v\&space;\frac{\partial&space;f}{\partial&space;x}&space;+&space;F\&space;\frac{\partial&space;f}{\partial&space;v}&space;=&space;Q(f,f))

where $f = f(t,\ v,\ x)$ is the distribution function, $F$ is the external force, $g(\theta) = g( - \theta)$ is the collision kernel, and $Q(f, f)$ is the collision operator.

The collision operator is a nonlinear integral operator that acts on $f(t,\ v,\ x)$ with respect to the velocity $v$ and describes the collision between particles. 

We represent the collision operator as:

![equation](https://latex.codecogs.com/svg.latex?Q(f,f)&space;=&space;\int_{-&space;\infty}^{\infty}{\int_{-&space;\pi}^{\pi}{g(\theta)f(v'\&space;)f(v_{*}'\&space;)&space;d\theta\&space;dv_{*}}}&space;-&space;\int_{-&space;\infty}^{\infty}{\int_{-&space;\pi}^{\pi}{g(\theta)f(v)f(v_{*}\&space;)&space;d\theta\&space;dv_{*}}})

where cct \in \mathbb{R}$, $v,v_{*},x \in \mathbb{R}$.


<h2>Simplifications and assumptions</h2>
 
Given the complexity, we simplify the kac_equation for a feasible numerical illustration within this format.

We choose 

\begin{equation}
    g(\theta)=\frac{1}{2\pi}, \label{eq: g}
\end{equation}

which implies a uniform distribution of scattering angles. This choice satisfies the normalization condition \eqref{eq: normalization_condition} for the collision kernel.

Furthermore, we consider other assumptions as discussed in section \ref{assumptions}, such as:

\begin{itemize}
    \item Spatially homogeneous case: Ignoring spatial dependence \((\frac{\partial f}{\partial x}=0)\) to focus on the velocity distribution evolution over time.
    \item No external force: Setting \(F=0\) to eliminate the acceleration term \((\frac{\partial f}{\partial v})\).
\end{itemize}

Hence, we have the simplified Kac equation \eqref{eq: reduced_kac}.g(\theta)=\frac{1}{2\pi}, \label{eq: g}
\end{equation}

which implies a uniform distribution of scattering angles. This choice satisfies the normalization condition \eqref{eq: normalization_condition} for the collision kernel.

Furthermore, we consider other assumptions as discussed in section \ref{assumptions}, such as:

\begin{itemize}
    \item Spatially homogeneous case: Ignoring spatial dependence \((\frac{\partial f}{\partial x}=0)\) to focus on the velocity distribution evolution over time.
    \item No external force: Setting \(F=0\) to eliminate the acceleration term \((\frac{\partial f}{\partial v})\).
\end{itemize}

Hence, we have the simplified Kac equation \eqref{eq: reduced_kac}.

#############################################################################
<h1>JWipe - Disk Sanitization</h1>

<h2>Description</h2>
Project consists of a simple PowerShell script that walks the user through "zeroing out" (wiping) any drives that are connected to the system. The utility allows you to select the target disk and choose the number of passes that are performed. The PowerShell script will configure a diskpart script file based on the user's selections and then launch Diskpart to perform the disk sanitization.
<br />


<h2>Languages and Utilities Used</h2>

- <b>PowerShell</b> 
- <b>Diskpart</b>

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
