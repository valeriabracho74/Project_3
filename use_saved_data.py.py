import numpy as np
import matplotlib.pyplot as plt

# Load previously saved arrays
boundary = np.load("yunlin_boundary.npy")
cables = np.load("yunlin_cables.npy")
turbines = np.load("yunlin_turbines.npy")

# Print shapes
print("Boundary shape:", boundary.shape)
print("Cables shape:", cables.shape)
print("Turbines shape:", turbines.shape)

# Plot
plt.figure(figsize=(10, 8))

# Plot boundary
plt.plot(boundary[:, 0], boundary[:, 1], 'b-', label="Wind Farm Boundary")

# Plot cables
for i, line in enumerate(cables):
    x1, y1, x2, y2 = line
    label = "Inter-Array Cables" if i == 0 else None
    plt.plot([x1, x2], [y1, y2], color='gray', alpha=0.7, label=label)

# Plot turbines
plt.scatter(turbines[:, 0], turbines[:, 1], color='orange', label="Turbines", zorder=5)

plt.title("Loaded Wind Farm Arrays")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
