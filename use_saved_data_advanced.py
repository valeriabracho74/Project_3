import numpy as np
import matplotlib.pyplot as plt

# Load saved arrays
boundary = np.load("yunlin_boundary.npy")
cables = np.load("yunlin_cables.npy")
turbines = np.load("yunlin_turbines.npy")

# Example 1: Calculate wind farm area
def polygon_area(coords):
    x = coords[:, 0]
    y = coords[:, 1]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

area = polygon_area(boundary)
print(f"Approximate Wind Farm Area: {area:.4f} degrees²")

# Example 2: Count cable segments and total length
def cable_lengths(array):
    return np.sqrt((array[:, 2] - array[:, 0])**2 + (array[:, 3] - array[:, 1])**2)

lengths = cable_lengths(cables)
print(f"Total Number of Cable Segments: {len(lengths)}")
print(f"Estimated Total Cable Length: {lengths.sum():.4f} degrees")

# Example 3: Plot turbines that lie near the western edge (longitude < median)
median_lon = np.median(boundary[:, 0])
west_turbines = turbines[turbines[:, 0] < median_lon]

plt.figure(figsize=(10, 8))
plt.plot(boundary[:, 0], boundary[:, 1], 'b-', label='Boundary')
for line in cables:
    plt.plot([line[0], line[2]], [line[1], line[3]], color='gray', alpha=0.6)
plt.scatter(turbines[:, 0], turbines[:, 1], c='orange', label='All Turbines')
plt.scatter(west_turbines[:, 0], west_turbines[:, 1], c='red', label='Western Turbines', marker='x')
plt.legend()
plt.title("Turbine Distribution & Cable Length Estimation")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.axis('equal')
plt.grid(True)
plt.show()
