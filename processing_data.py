import pandas as pd
from skyfield.api import EarthSatellite, load

# File path to your .txt file containing TLE data
file_path = "data/tle_data.txt"

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse data into chunks (Name, Line1, Line2)
satellites = []
for i in range(0, len(lines), 3):
    name = lines[i].strip()
    line1 = lines[i + 1].strip()
    line2 = lines[i + 2].strip()
    satellites.append((name, line1, line2))

# Load Skyfield timescale
ts = load.timescale()

# Extract satellite parameters
satellite_info = []
for name, line1, line2 in satellites:
    satellite = EarthSatellite(line1, line2, name, ts)
    satellite_info.append({
        "Satellite Name": satellite.name,
        "NORAD ID": satellite.model.satnum,
        "Inclination (°)": satellite.model.inclo,
        "RAAN (°)": satellite.model.nodeo,
        "Eccentricity": satellite.model.ecco,
        "Arg. of Perigee (°)": satellite.model.argpo,
        "Mean Anomaly (°)": satellite.model.mo,
        "Mean Motion (revs/day)": satellite.model.no_kozai,
        "Epoch": satellite.epoch.utc_iso()
    })

# Convert to a DataFrame
df = pd.DataFrame(satellite_info)

# Display the structured DataFrame
print(df)

# Save the data into a JSON file
# Save the structured data to a CSV file
output_path = "data/processed_satellite_data.csv"
df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")
