import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# Given data for voltages and their corresponding points
voltages = {
    1.5: [(15, 10), (14.2, 12), (15, 5.8)],
    1.2: [(12-5, 10), (9-5, 6), (10-5, 15)],
    1.9: [(19, 14), (19, 5), (18, 10)]
}

# Create a new figure with the adjusted size
fig, ax = plt.subplots(figsize=(24, 20))

# Define the grid size
grid_size = (24, 20)

# Define extended range of x values for plotting the curves
y_extended = np.linspace(0, grid_size[0], 300)

# Add plates for visualization
ball = plt.Circle((3, 10), 1, color='blue', fill=True, alpha=0.5)
ax.add_patch(ball)

ball = plt.Circle((21, 10), 1, color='blue', fill=True, alpha=0.5)
ax.add_patch(ball)


# Define a wider range for y values to extrapolate the curves
y_min, y_max = -5, 25  # Extended beyond the original grid size for demonstration
y_extended = np.linspace(y_min, y_max, 300)

# Fit and plot a curve for each voltage level
for v, points in voltages.items():
    # Sort points based on y for vertical interpolation
    points = sorted(points, key=lambda point: point[1])
    x_coords, y_coords = zip(*points)

    # Interpolate y as a function of x using a quadratic fit
    # Create interpolation function over y
    curve_fit = interp1d(y_coords, x_coords, kind='quadratic', fill_value='extrapolate')

    # Calculate the x values from the fitted curve over the extended y range
    y_fit = y_extended
    x_fit = curve_fit(y_fit)
    
    # Plotting the fitted curve
    ax.plot(x_fit, y_fit, label=f'Fitted Curve for {v} Volts')

    # Re-plotting the original points to keep them in the foreground
    ax.scatter(x_coords, y_coords, label=f'V: {v} Volts Points', s=100, zorder=5)

# Setting grid lines like graph paper
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Set the limits and labels to match the grid size
plt.xlim(0, 24)
plt.ylim(0, 20)
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Physics Lab Measurements: Configuration 3')

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Add a legend
plt.legend()

# Show the plot with the new style
plt.show()
