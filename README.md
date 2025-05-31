# Satellite Tracker and Visualization

A comprehensive system for processing satellite TLE (Two-Line Element) data and visualizing satellite orbits in real-time 3D.

## Overview

This project consists of two main components:
1. A Python backend for processing satellite TLE data
2. A React/Three.js frontend for real-time 3D visualization

## Backend Features

- Process TLE data from text files
- Calculate satellite positions using orbital elements
- Generate time series data for satellite trajectories
- Extract TLE data from various online sources

## Frontend Features

- 🌍 Realistic Earth visualization with procedural textures
- 🛰️ Real-time satellite orbit visualization using actual orbital parameters
- 🎨 Color-coded satellites with orbital trails
- 🎮 Interactive camera controls
- ⚡ Adjustable simulation speed
- 📊 Detailed satellite information panel
- 🌟 Dynamic starfield background
- 💫 Atmospheric glow effect

## Project Structure

```
satellite_tracker/
├── data/                  # Data directory for input/output files
├── src/
│   ├── utils/            # Utility functions
│   │   └── orbital_utils.py
│   └── processing/       # Data processing modules
│       ├── data_processor.py
│       └── tle_extractor.py
├── tests/                # Test files
├── main.py              # Main entry point
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Installation

### Backend Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd satellite_tracker
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Frontend Setup

The frontend is deployed at [ahlam.fyi/space](https://ahlam.fyi/space) and uses:
- React
- Three.js
- PapaParse (for CSV data parsing)
- Tailwind CSS

## Usage

### Backend Processing

1. Run the main script to process TLE data:
```bash
python main.py
```

This will:
- Extract TLE data from online sources
- Process the TLE data
- Generate time series data for satellite positions
- Save results to CSV files

### Frontend Visualization

The visualization is available at [ahlam.fyi/space](https://ahlam.fyi/space) with the following features:

#### Controls
- Move mouse to rotate the camera view
- Use the speed slider to control orbital motion speed
- Click on satellites in the info panel to select them
- Toggle play/pause to control the simulation

#### Technical Details

##### Earth Visualization
- Procedurally generated Earth texture with continents and oceans
- Atmospheric glow effect
- Realistic lighting and shadows

##### Satellite System
- Each satellite is represented by a 3D cube with unique colors
- Orbital trails showing the satellite's path
- Real-time position updates based on orbital mechanics
- Color-coded information panel with satellite details

## Output Files

- `data/processed_satellite_data.csv`: Processed satellite data with orbital elements
- `data/satellite_positions.csv`: Time series data of satellite positions

## Dependencies

### Backend
- numpy: Numerical computing
- pandas: Data manipulation
- astropy: Astronomical calculations
- skyfield: Satellite position calculations
- requests: HTTP requests for TLE data

### Frontend
- React: UI framework
- Three.js: 3D graphics
- PapaParse: CSV parsing
- Tailwind CSS: Styling

## Performance Considerations

- Efficient use of Three.js geometries and materials
- Optimized orbital calculations
- Limited trail points to maintain performance
- Proper cleanup of Three.js resources on component unmount

## Notes
- The visualization requires a CSV file with satellite data in the specified format
- The visualization is optimized for modern browsers with WebGL support
- The Earth texture is procedurally generated and may vary slightly between renders

