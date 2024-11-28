# Import Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy.integrate import simps

# Initialize random seed for reproducibility
np.random.seed(0)
# Setting a random seed ensures that the random number generation is reproducible, making the simulation results consistent across runs.

# Define Parameters
n_particles = 100000  # Number of particles
time_steps = 50  # Number of time steps to simulate
hist_range = (-5, 5)  # Range for visualization
velocity_grid = np.linspace(hist_range[0], hist_range[1], 300)  # Velocity grid for plots
n_cells = 10  # Number of cells for spatial division

# Define the Maxwellian distribution function
def maxwellian_distribution(v):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-v**2 / 2)
# This function calculates the Maxwellian distribution, which is the target equilibrium distribution for particle velocities.

# Initial velocity distribution: Uniform distribution
v_initial = np.random.uniform(low=-2.5, high=2.5, size=n_particles)
# Initializes particle velocities with a uniform distribution ranging from -2.5 to 2.5.

# Kernel Density Estimation for initial distribution
kde_initial = gaussian_kde(v_initial)
initial_density = kde_initial.evaluate(velocity_grid)
# gaussian_kde: Estimates the probability density function of the initial velocities using kernel density estimation.
# initial_density: Evaluates the estimated density on the defined velocity grid.

# Plotting initial distribution
plt.figure(figsize=(6, 6))
plt.plot(velocity_grid, initial_density, label='Initial', color='blue')
plt.ylim(0, 0.5)  # Set y-axis range from 0 to 0.4 for consistency
plt.legend()
plt.xlabel('Velocity')
plt.ylabel('Density')
plt.title('Initial Velocity Distribution')
plt.savefig('uniform_initial.png')
plt.show()
# Plots the initial velocity distribution and saves the figure as 'uniform_initial.png'.

# Copy of initial velocities for simulation
v = np.copy(v_initial)
# Creates a copy of the initial velocities to use in the collision simulation.

# List to store distributions at each time step
distribution_evolution = [initial_density]
# Initializes a list to store the density distributions at each time step, starting with the initial distribution.

# Define cells
cell_size = n_particles // n_cells
cells = np.array_split(np.arange(n_particles), n_cells)

# Plotting distribution at each time step
for step in range(1, time_steps + 1):
    for cell in cells:
        # Simulate the collision process for particles within this cell
        n_cell_particles = len(cell)
        partner_indices = np.random.choice(cell, size=n_cell_particles)
        v_partners = v[partner_indices]
        theta = np.random.uniform(-np.pi, np.pi, size=n_cell_particles)
        v[cell] = np.cos(theta) * v[cell] + np.sin(theta) * v_partners
        # Simulates collisions within the cell by randomly pairing particles and updating their velocities based on a random collision angle.
        
    # Compute the density after collisions
    distribution = gaussian_kde(v).evaluate(velocity_grid)
    distribution_evolution.append(distribution)
    # Computes the new velocity distribution after collisions using kernel density estimation and stores it.
    
# Calculate Maxwellian distribution over the same velocity grid
maxwellian_density = maxwellian_distribution(velocity_grid)
# Computes the Maxwellian distribution over the velocity grid for comparison with the final simulated distribution.

# Plot final distribution
plt.figure(figsize=(6, 6))
plt.plot(velocity_grid, distribution_evolution[-1], label='Final', color='red')
plt.ylim(0, 0.5)  # Set y-axis range from 0 to 0.4 to match the initial plot
plt.legend()
plt.xlabel('Velocity')
plt.ylabel('Density')
plt.title('Final Velocity Distribution (Maxwellian)')
plt.savefig('uniform_final_dsmc.png')
plt.show()
# Plots the final velocity distribution after all time steps and saves the figure as 'uniform_final_dsmc.png'.
