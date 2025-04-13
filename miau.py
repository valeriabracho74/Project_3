import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import json
import pandas as pd

class GeoBoundary:
    def __init__(self, geojson_file):
        self.geojson = self._load_geojson(geojson_file)
        self.coords = self._extract_coordinates()
        self.polygon_array = np.array(self.coords)
        self.path = Path(self.polygon_array)

    def _load_geojson(self, filepath):
        with open(filepath, 'r') as f:
            return json.load(f)

    def _extract_coordinates(self):
        return self.geojson['features'][0]['geometry']['coordinates'][0]

    def get_array(self):
        return self.polygon_array

    def plot(self):
        x, y = self.polygon_array[:, 0], self.polygon_array[:, 1]
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, linestyle='-', marker='o', label='Boundary Polygon')
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.axis('equal')
        plt.grid(True)

    def contains_point(self, lon, lat):
        """
        Check if a given (longitude, latitude) point is inside the polygon.
        Returns True if the point is inside, False otherwise.
        """
        return self.path.contains_point((lon, lat))

    def load_turbines(self, csv_file):
        """
        Load turbine positions from a CSV file with columns: 'lon', 'lat'.
        Returns a DataFrame with an added 'inside' column (True/False).
        """
        df = pd.read_csv(csv_file)
        df['inside'] = df.apply(lambda row: self.contains_point(row['lon'], row['lat']), axis=1)
        return df

    def plot_turbines(self, df):
        inside = df[df['inside']]
        outside = df[~df['inside']]

        self.plot()  # draw the boundary first
        plt.scatter(inside['lon'], inside['lat'], color='green', label='Inside Turbines')
        plt.scatter(outside['lon'], outside['lat'], color='red', label='Outside Turbines')
        plt.legend()
        plt.title("Turbines Inside/Outside Boundary")
        plt.show()

if __name__ == "__main__":
    boundary = GeoBoundary("circle.geojson")
    print("Polygon array shape:", boundary.get_array().shape)
    boundary.plot()
    plt.title("Wind Farm Boundary Only")
    plt.show()

    # Example: Check if a turbine is inside the boundary
    sample_turbine_lon = 119.8500
    sample_turbine_lat = 25.3200
    is_inside = boundary.contains_point(sample_turbine_lon, sample_turbine_lat)
    print(f"Is turbine at ({sample_turbine_lon}, {sample_turbine_lat}) inside the polygon?", is_inside)

    # Generate and save dummy turbines for testing
    test_turbines = pd.DataFrame({
        'lon': [119.9, 120.1, 121.0, 118.9, 119.6],
        'lat': [24.8, 24.0, 23.5, 25.1, 24.6]
    })
    test_turbines.to_csv("turbines.csv", index=False)
    print("Dummy 'turbines.csv' created with sample coordinates.")

    # Load and plot turbines from CSV file
    turbines_df = boundary.load_turbines("turbines.csv")
    print("Turbine DataFrame with inside status:\n", turbines_df)
    boundary.plot_turbines(turbines_df)
