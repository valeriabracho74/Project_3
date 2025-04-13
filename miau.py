import json
import numpy as np
import matplotlib.pyplot as plt

class YunlinFarmVisualizer:
    def __init__(self, boundary_file="polygonyunlin.geojson", cables_file="linecables.geojson", turbines_file="pointgenerator.geojson"):
        self.boundary_file = boundary_file
        self.cables_file = cables_file
        self.turbines_file = turbines_file
        self.boundary_array = self._load_boundary()
        self.cables_array = self._load_cables()
        self.turbines_array = self._load_turbines()

    def _load_boundary(self):
        with open(self.boundary_file, 'r') as f:
            geojson = json.load(f)
        for feature in geojson["features"]:
            if feature["geometry"]["type"] == "Polygon":
                coords = feature["geometry"]["coordinates"][0]
                return np.array(coords)
        return np.array([])

    def _load_cables(self):
        with open(self.cables_file, 'r') as f:
            geojson = json.load(f)
        cables = []
        for feature in geojson["features"]:
            if feature["geometry"]["type"] == "LineString":
                coords = feature["geometry"]["coordinates"]
                for i in range(len(coords) - 1):
                    x1, y1 = coords[i]
                    x2, y2 = coords[i + 1]
                    cables.append([x1, y1, x2, y2])
        return np.array(cables)

    def _load_turbines(self):
        with open(self.turbines_file, 'r') as f:
            geojson = json.load(f)
        points = []
        for feature in geojson["features"]:
            if feature["geometry"]["type"] == "Point":
                x, y = feature["geometry"]["coordinates"]
                points.append([x, y])
        return np.array(points)

    def plot(self):
        plt.figure(figsize=(10, 8))

        if self.boundary_array.size > 0:
            plt.plot(self.boundary_array[:, 0], self.boundary_array[:, 1], 'b-', label='Wind Farm Boundary')

        for idx, line in enumerate(self.cables_array):
            x1, y1, x2, y2 = line
            label = 'Inter-Array Cables' if idx == 0 else None
            plt.plot([x1, x2], [y1, y2], color='gray', alpha=0.7, label=label)

        if self.turbines_array.size > 0:
            plt.scatter(self.turbines_array[:, 0], self.turbines_array[:, 1], color='orange', label='Turbines', zorder=5)

        plt.title("Yunlin Wind Farm: Boundary, Cables, and Turbines")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.axis('equal')
        plt.grid(True)
        plt.legend()
        plt.show()

    def get_arrays(self):
        return self.boundary_array, self.cables_array, self.turbines_array

    def save_arrays(self, prefix="yunlin"):
        np.save(f"{prefix}_boundary.npy", self.boundary_array)
        np.save(f"{prefix}_cables.npy", self.cables_array)
        np.save(f"{prefix}_turbines.npy", self.turbines_array)
        print("Arrays saved as .npy files.")

if __name__ == "__main__":
    visualizer = YunlinFarmVisualizer()
    boundary, cables, turbines = visualizer.get_arrays()
    print("Boundary shape:", boundary.shape)
    print("Cables shape:", cables.shape)
    print("Turbines shape:", turbines.shape)
    visualizer.plot()
    visualizer.save_arrays()
