import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
d = 2.0  # distance between charges
sigma = 1.0  # charge density
epsilon_0 = 8.854e-12  # electric constant

# Define the positions of the point charges
point_charge_pos = (d / 2, 0)  # Position of the positive point charge
point_charge_neg = (-d / 2, 0)  # Position of the negative point charge

xlim = ylim = -5, 5

# Define a mesh grid of points
x, y = np.meshgrid(np.linspace(*xlim, 200), np.linspace(*ylim, 200))

# Calculate the electric field at each point on the grid
Ex, Ey = np.zeros_like(x), np.zeros_like(y)
V = np.zeros_like(x)  # Potential

# Function to calculate electric field and potential due to a single charge
def electric_field_potential(q, r0, x, y):
    dx = x - r0[0]
    dy = y - r0[1]
    r_squared = dx**2 + dy**2
    r = np.sqrt(r_squared)
    Ex = q * dx / (r_squared * r)
    Ey = q * dy / (r_squared * r)
    V = q / (4 * np.pi * epsilon_0 * r)
    return Ex, Ey, V

# Add the electric field and potential contribution from the positive point charge
q_pos = sigma  # Charge of the positive point charge
Ex_pos, Ey_pos, V_pos = electric_field_potential(q_pos, point_charge_pos, x, y)
Ex += Ex_pos
Ey += Ey_pos
V += V_pos

# Add the electric field and potential contribution from the negative point charge
q_neg = -sigma  # Charge of the negative point charge
Ex_neg, Ey_neg, V_neg = electric_field_potential(q_neg, point_charge_neg, x, y)
Ex += Ex_neg
Ey += Ey_neg
V += V_neg

# Normalize the electric field vectors (for better visualization)
E_magnitude = np.sqrt(Ex**2 + Ey**2)
Ex_normalized = Ex / E_magnitude
Ey_normalized = Ey / E_magnitude

# Visualize the electric field lines and equipotential lines
fig, ax = plt.subplots(figsize=(8, 8))
# Plot the electric field lines
ax.streamplot(x, y, Ex_normalized, Ey_normalized, color='blue', density=2, arrowstyle='->', arrowsize=1.5)
# Plot the equipotential lines
contour = ax.contour(x, y, V, levels=50, colors='red', linewidths=0.5)

ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_title('Electric Field and Equipotential Lines of Two Point Charges')
ax.set_aspect('equal')

# Plot the point charges
ax.plot(point_charge_pos[0], point_charge_pos[1], 'ro', markersize=8)  # Positive charge
ax.plot(point_charge_neg[0], point_charge_neg[1], 'ko', markersize=8)  # Negative charge

plt.show()
