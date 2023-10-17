import json
import os

# Path to the source JSON file
source_file = 'week_5/Artworks.json'

# Create the 'res' subfolder if it doesn't exist
res_folder = 'week_5/res'
os.makedirs(res_folder, exist_ok=True)

# Open and read the source JSON file
with open(source_file, 'r') as json_file:
    data = json.load(json_file)

    # Group by nationality and create separate JSON files
    for entry in data:
        nationalities = entry.get('Nationality', ['Unknown'])
        for nationality in nationalities:
            sanitized_nat = nationality.replace('/', '_')

            # Create a JSON file for each nationality
            file_path = os.path.join(res_folder, f'{sanitized_nat}.json')
            with open(file_path, 'w', newline='') as nat_file:
                json.dump([entry], nat_file, indent=2)
                
