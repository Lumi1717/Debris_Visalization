import os
from src.processing.data_processor import process_tle_data, generate_time_series
from src.processing.tle_extractor import TLEExtractor

def main():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    
    # Extract TLE data
    urls = [
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-043&FORMAT=tle",
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-020&FORMAT=tle",
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-020&FORMAT=tle",
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-051&FORMAT=tle",
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-051&FORMAT=tle",
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-030&FORMAT=tle",
        "https://celestrak.org/NORAD/elements/gp.php?INTDES=1998-026&FORMAT=tle"
    ]
    
    extractor = TLEExtractor()
    if not extractor.extract_tle_data(urls):
        print("Failed to extract TLE data. Exiting...")
        return
    
    # Process TLE data
    tle_data = process_tle_data('data/tle_data.txt')
    tle_data.to_csv('data/processed_satellite_data.csv', index=False)

    
    # Generate time series data
    time_series_data = generate_time_series(tle_data)
    time_series_data.to_csv('data/satellite_positions.csv', index=False)
    
    print("Data processing complete. Output files:")
    print("- data/processed_satellite_data.csv")
    print("- data/satellite_positions.csv")

if __name__ == "__main__":
    main() 