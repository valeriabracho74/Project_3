# Yunlin Offshore Wind Farm Data Processor

This project extracts, visualizes, and stores structured data for the **Yunlin Offshore Wind Farm** based on exported data from [SeaImpact](https://sea-impact.com/offshore-wind-map/).

##  Project Overview

We work with three key variables exported from the SeaImpact interface:

- **Wind Farm Boundary** (`polygonyunlin.geojson`)
- **Inter-Array Cables** (`linecables.geojson`)
- **Wind Turbine Generator Points** (`pointgenerator.geojson`)

## Output

The program converts the above data into NumPy arrays:

| Variable | File Name                | Array Shape | Description                          |
|----------|--------------------------|-------------|--------------------------------------|
| Boundary | `yunlin_boundary.npy`    | (N, 2)      | Wind farm polygon (lon, lat)         |
| Cables   | `yunlin_cables.npy`      | (M, 4)      | Line segments: [x1, y1, x2, y2]       |
| Turbines | `yunlin_turbines.npy`    | (T, 2)      | Turbine positions (lon, lat)         |

## Visualization

The included script and notebook (`yunlin_full_analysis.ipynb`) plot:

- Wind Farm Boundary (blue)
- Inter-Array Cables (gray)
- Turbines (orange dots)

## How to Run

Run the main file:
```bash
python miau.py
```

This will:
- Load the geojson data
- Print array shapes
- Show the full layout plot
- Save `.npy` files with extracted arrays

You can reuse the arrays like this:

```python
import numpy as np

boundary = np.load("yunlin_boundary.npy")
cables = np.load("yunlin_cables.npy")
turbines = np.load("yunlin_turbines.npy")
```

## File Structure

```
├── miau.py
├── yunlin_full_analysis.ipynb
├── polygonyunlin.geojson
├── linecables.geojson
├── pointgenerator.geojson
├── yunlin_boundary.npy
├── yunlin_cables.npy
├── yunlin_turbines.npy
```

## Credits

Created by Valeria Lindado Bracho  
University of Massachusetts Boston | ENGIN 480-1
