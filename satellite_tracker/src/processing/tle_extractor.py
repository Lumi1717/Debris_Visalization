import requests
import os
from typing import List, Optional

class TLEExtractor:
    """Class for extracting TLE data from various sources."""
    
    def __init__(self, data_folder: str = "data"):
        """
        Initialize the TLE extractor.
        
        Args:
            data_folder (str): Path to the data folder
        """
        self.data_folder = data_folder
        self.output_file = os.path.join(data_folder, "tle_data.txt")
        os.makedirs(data_folder, exist_ok=True)

    def fetch_tle(self, url: str) -> Optional[str]:
        """
        Fetch TLE data from the given URL.
        
        Args:
            url (str): URL to fetch TLE data from
            
        Returns:
            Optional[str]: TLE data if successful, None if failed
        """
        try:
            response = requests.get(url)
            response.raise_for_status() 
            return response.text.strip()
        except requests.RequestException as e:
            print(f"Error fetching data from {url}: {str(e)}")
            return None

    def extract_tle_data(self, urls: List[str]) -> bool:
        """
        Extract TLE data from multiple URLs and save to a file.
        
        Args:
            urls (List[str]): List of URLs to fetch TLE data from
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.output_file, "w") as file:
                for url in urls:
                    tle_data = self.fetch_tle(url)
                    if tle_data:
                        file.write(tle_data + "\n")
            print(f"TLE data saved to {self.output_file} successfully!")
            return True
        except Exception as e:
            print(f"Error saving TLE data: {str(e)}")
            return False

def main():
    """Main function to demonstrate TLE extraction."""
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

    extractor = TLEExtractor()
    extractor.extract_tle_data(urls)

if __name__ == "__main__":
    main() 