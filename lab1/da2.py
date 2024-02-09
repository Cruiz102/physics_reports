import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
d = 2.0  # distance between plates
sigma = 1.0  # charge density
epsilon_0 = 8.854e-12  # electric constant
n_charges = 50  # Define the number of charges on the plate

# Define the position of the single charge and the plate (make the plate narrower)
plate_width = d / 10  # Reduced width of the plate
y_charges_plate = np.linspace(-d, d, n_charges)
x_charges_plate = np.full_like(y_charges_plate, d / 2 + plate_width / 2)  # Position the plate at d/2

# Single charge position
x_single_charge, y_single_charge = -d/2, 0

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

# Add the contributions from the plate to the total electric field and potential
q_plate = sigma  # Charge on the plate
for x_plate, y_plate in zip(x_charges_plate, y_charges_plate):
    Ex_plate, Ey_plate, V_plate = electric_field_potential(q_plate, (x_plate, y_plate), x, y)
    Ex += Ex_plate
    Ey += Ey_plate
    V += V_plate

# Add the electric field and potential contribution from the single charge
q_single = -sigma  # Charge of the single charge
Ex_single, Ey_single, V_single = electric_field_potential(q_single, (x_single_charge, y_single_charge), x, y)
Ex += Ex_single
Ey += Ey_single
V += V_single

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
ax.set_title('Electric Field and Equipotential Lines of a Single Charge and a  Plate')
ax.set_aspect('equal')

# Add a rectangle to represent the narrow plate and a dot for the single charge
plate_patch = plt.Rectangle((d/2, -d), plate_width, 2*d, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(plate_patch)
ax.plot(x_single_charge, y_single_charge, 'ro')  # 'ro' for red dot

plt.show()
