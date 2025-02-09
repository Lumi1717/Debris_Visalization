import pandas as pd
import skyfield.api as sf
import numpy as np
import datetime

# Load the satellite data from the CSV file
tle_data = pd.read_csv('data/processed_satellite_data.csv')

def generate_tle_lines(row):
    """
    Generate TLE lines (tle1, tle2) from the dataset row.
    """
    # TLE line 1
    tle1 = f"1 {int(row['NORAD ID']):05d}U {datetime.datetime.now().strftime('%y%j')}   0.00000000  00000-0  00000-0 0  0000"
    
    # TLE line 2
    tle2 = (f"2 {int(row['NORAD ID']):05d} "
            f"{float(row['Inclination (°)']):8.4f} {float(row['RAAN (°)']):8.4f} "
            f"{float(row['Eccentricity']):07.7f} {float(row['Arg. of Perigee (°)']):8.4f} "
            f"{float(row['Mean Anomaly (°)']):8.4f} {float(row['Mean Motion (revs/day)']):11.8f}")
    return tle1, tle2

def tle_to_cartesian(tle1, tle2, time):
    """
    Converts TLEs to Cartesian coordinates using Skyfield.

    Args:
        tle1: Line 1 of the TLE.
        tle2: Line 2 of the TLE.
        time: Skyfield time object.

    Returns:
        A tuple containing the x, y, and z coordinates in kilometers.
    """
    ts = sf.load.timescale()
    satellite = sf.EarthSatellite(tle1, tle2, "Satellite", ts)
    geometric = satellite.at(time)
    position_km = geometric.position.km
    return position_km

# Parameters
time_interval = 3600  # 1 hour in seconds
num_steps = 24  # Generate positions for 24 hours

# Prepare a list to store the time series data
time_series_data = []
ts = sf.load.timescale()

# Iterate through the rows of the DataFrame
for _, row in tle_data.iterrows():
    satellite_name = row['Satellite Name']
    epoch = row['Epoch']

    # Generate TLE lines
    tle1, tle2 = generate_tle_lines(row)

    try:
        # Parse epoch and create initial Skyfield time object
        initial_time = ts.from_datetime(datetime.datetime.fromisoformat(epoch.replace('Z', '+00:00')))

        for i in range(num_steps):
            curr_time = initial_time + (i * time_interval / (24 * 3600))  # Add time interval in days

            # Compute Cartesian coordinates
            x, y, z = tle_to_cartesian(tle1=tle1, tle2=tle2, time=curr_time)

            # Append data to the time series
            time_series_data.append({
                'time': curr_time.utc_iso(),
                'satellite_name': satellite_name,
                'x': x,
                'y': y,
                'z': z
            })
    except ValueError as e:
        print(f"Error processing satellite {satellite_name}: {e}")
        continue

# Create a DataFrame and save it as a CSV file
time_series_df = pd.DataFrame(time_series_data)
time_series_df.to_csv('data/satellite_positions.csv', index=False)
print(time_series_df)
