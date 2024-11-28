# DSMC-Method

 ### Numerical illustrations using Direct Simulation Monte Carlo method

<h2>Description</h2>
Numerical simulations to illustrate the analytical solutions to the Kac's equation
and explore analytically intractable scenarios.
<br />

<h2>Kac equation</h2>
The Kac equation can be represented as:

$$\frac{\partial f}{\partial t} + v\ \frac{\partial f}{\partial x} + F\ \frac{\partial f}{\partial v} = Q(f,f)$$

where $f = f(t,\ v,\ x)$ is the distribution function, $F$ is the external force, $g(\theta) = g( - \theta)$ is the collision kernel, and $Q(f, f)$ is the collision operator.

The collision operator is a nonlinear integral operator that acts on $f(t,\ v,\ x)$ with respect to the velocity $v$ and describes the collision between particles. 

We represent the collision operator as:


$$Q(f,f) = \int_{- \infty}^{\infty}{\int_{- \pi}^{\pi}{g(\theta)\left( f(v'\ )f(v_{*}'\ ) - f(v)f(v_{*}\ ) \right) d\theta\ dv_{*}}}$$


where $t \in \mathbb{R}$, $v,v_{*},x \in \mathbb{R}$.


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
