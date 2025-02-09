import json
import os 


data_folder = "data"
file_path = os.path.join(data_folder, "tle_data.txt")

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse data into chunks (Name, Line1, Line2)
satellites = []
for i in range(0, len(lines), 3):
    name = lines[i].strip()
    line1 = lines[i + 1].strip()
    line2 = lines[i + 2].strip()
    satellites.append({
        "Satellite Name": name,
        "Line1": line1,
        "Line2": line2
    })

# Print parsed satellite data
print("Satellites:", satellites)

# Save the data into a JSON file
output_file_path = os.path.join(data_folder, "satellite_data.json")


with open(output_file_path, 'w') as json_file:
    json.dump(satellites, json_file, indent=4)

print(f"Satellite data saved to {output_file_path}")
