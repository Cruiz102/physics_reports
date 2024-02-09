import matplotlib.pyplot as plt
import numpy as np
voltages = {
    2.7: [(17, 11), (17, 16), (17, 5)],
    2.0: [(14, 11), (14, 12), (14.3, 15)],
    0.8: [(9, 11), (8, 17), (9, 1)]
}

# Create a new figure with the adjusted size
fig, ax = plt.subplots(figsize=(24, 20))

# Define the grid size
grid_size = (24, 20)

from scipy.interpolate import interp1d

# Create a new figure with the adjusted size
fig, ax = plt.subplots(figsize=(24, 20))

# Define the grid size and extended range of y values for plotting the curves
grid_size = (24, 20)
y_extended = np.linspace(0, grid_size[0], 300)



plate = plt.Rectangle((1,14/2 - 5), 0.5, 15, color='red', alpha=0.5)  # Width of 0.5 to make it visible as a line
ax.add_patch(plate)

plate = plt.Rectangle((21, 14/2 - 5), 0.5, 15, color='blue', alpha=0.5)  # Width of 0.5 to make it visible as a line
ax.add_patch(plate)
# Fit and plot a curve for each voltage level, checking for duplicates
for v, points in voltages.items():
    # Check if there are duplicate x values
    x_values = [p[0] for p in points]
    if len(x_values) != len(set(x_values)):  # Duplicates detected
        # Sort points based on y for horizontal interpolation
        points = sorted(points, key=lambda point: point[1])
        x_coords, y_coords = zip(*points)
        # Create interpolation function over y
        curve_fit = interp1d(y_coords, x_coords, kind='quadratic', fill_value="extrapolate")
        # Calculate the x values from the fitted curve over the extended y range
        x_fit = curve_fit(y_extended)
        y_fit = y_extended
    else:
        # No duplicates, proceed as usual with vertical interpolation
        # Sort points based on x for vertical interpolation
        points = sorted(points, key=lambda point: point[0])
        x_coords, y_coords = zip(*points)
        # Create interpolation function over x
        curve_fit = interp1d(x_coords, y_coords, kind='quadratic', fill_value="extrapolate")
        # Calculate the y values from the fitted curve over the original x range
        x_fit = np.linspace(min(x_coords), max(x_coords), 300)
        y_fit = curve_fit(x_fit)
    
    # Plotting the fitted curve
    ax.plot(x_fit, y_fit, label=f'Fitted Curve for {v} Volts')

    # Re-plotting the original points to keep them in the foreground
    ax.scatter(x_coords, y_coords, label=f'V: {v} Volts Points', s=100, zorder=5)

# Setting grid lines like graph paper
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Set the limits and labels to match the grid size
plt.xlim(0, grid_size[1])
plt.ylim(0, grid_size[0])
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Physics Lab Measurements: Configuration 3')

# Set the aspect of the plot to be equal
ax.set_aspect('equal')
plt.xlim(0, 24)
plt.ylim(0, 20)
# Add a legend
plt.legend()

# Show the plot with the new style
plt.show()