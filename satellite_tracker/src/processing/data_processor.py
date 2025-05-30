import pandas as pd
from skyfield.api import EarthSatellite, load

def process_tle_data(file_path):
    """
    Process TLE data from a text file and convert it to a structured DataFrame.
    
    Args:
        file_path (str): Path to the TLE data file
        
    Returns:
        pandas.DataFrame: Processed satellite data
    """
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
    return df

def generate_time_series(tle_data, time_interval=3600, num_steps=24):
    """
    Generate time series data for satellite positions.
    
    Args:
        tle_data (pandas.DataFrame): DataFrame containing TLE data
        time_interval (int): Time interval in seconds
        num_steps (int): Number of time steps to generate
        
    Returns:
        pandas.DataFrame: Time series data of satellite positions
    """
    import datetime
    import skyfield.api as sf
    
    ts = sf.load.timescale()
    time_series_data = []

    def generate_tle_lines(row):
        tle1 = f"1 {int(row['NORAD ID']):05d}U {datetime.datetime.now().strftime('%y%j')}   0.00000000  00000-0  00000-0 0  0000"
        tle2 = (f"2 {int(row['NORAD ID']):05d} "
                f"{float(row['Inclination (°)']):8.4f} {float(row['RAAN (°)']):8.4f} "
                f"{float(row['Eccentricity']):07.7f} {float(row['Arg. of Perigee (°)']):8.4f} "
                f"{float(row['Mean Anomaly (°)']):8.4f} {float(row['Mean Motion (revs/day)']):11.8f}")
        return tle1, tle2

    def tle_to_cartesian(tle1, tle2, time):
        satellite = sf.EarthSatellite(tle1, tle2, "Satellite", ts)
        geometric = satellite.at(time)
        return geometric.position.km

    for _, row in tle_data.iterrows():
        satellite_name = row['Satellite Name']
        epoch = row['Epoch']
        tle1, tle2 = generate_tle_lines(row)

        try:
            initial_time = ts.from_datetime(datetime.datetime.fromisoformat(epoch.replace('Z', '+00:00')))

            for i in range(num_steps):
                curr_time = initial_time + (i * time_interval / (24 * 3600))
                x, y, z = tle_to_cartesian(tle1=tle1, tle2=tle2, time=curr_time)

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

    return pd.DataFrame(time_series_data) 