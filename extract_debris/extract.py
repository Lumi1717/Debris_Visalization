import requests
import os


# List of URLs for different TLE data sources
urls = [
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-043&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-020&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-020&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-051&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-051&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1997-030&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?INTDES=1998-026&FORMAT=tle"


]

data_folder = "data"
output_file = os.path.join(data_folder, "tle_data.txt")

# Create the 'data' folder if it doesn't exist
os.makedirs(data_folder, exist_ok=True)

def fetch_tle(url):
    """Fetches TLE data from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()  # Return raw TLE data
    else:
        return f"Error: Failed to fetch data from {url}. HTTP Status Code: {response.status_code}\n"

# Fetch and write TLE data to a text file in the 'data' folder
with open(output_file, "w") as file:
    for url in urls:
        tle_data = fetch_tle(url)
        file.write(tle_data + "\n")  # Separate entries with a newline

print(f"TLE data saved to {output_file} successfully!")