# Satellite Tracker

A Python package for processing and analyzing satellite TLE (Two-Line Element) data.

## Features

- Process TLE data from text files
- Calculate satellite positions using orbital elements
- Generate time series data for satellite trajectories

## Project Structure

```
satellite_tracker/
├── data/                  # Data directory for input/output files
├── src/
│   ├── utils/            # Utility functions
│   │   └── orbital_utils.py
│   └── processing/       # Data processing modules
│       └── data_processor.py
├── tests/                # Test files
├── main.py              # Main entry point
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Installation

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

## Usage

1. Place your TLE data file in the `data` directory as `tle_data.txt`. The file should contain satellite data in the following format:
```
SATELLITE NAME
TLE LINE 1
TLE LINE 2
```

2. Run the main script:
```bash
python main.py
```

This will:
- Process the TLE data
- Generate time series data for satellite positions

## Output Files

- `data/processed_satellite_data.csv`: Processed satellite data with orbital elements
- `data/satellite_positions.csv`: Time series data of satellite positions

## Dependencies

- numpy: Numerical computing
- pandas: Data manipulation
- astropy: Astronomical calculations
- skyfield: Satellite position calculations

## License

[Your chosen license] 