import requests
import json

# MET API endpoint for search
api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'

# Define the search parameters
search_params = {
    'q': 'van gogh',
    'isOnView': True,
    'hasImages': True
}

# Make a GET request to The MET's API
response = requests.get(api_url, params=search_params)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Pretty-print the resulting JSON with an indentation of 2
    pretty_json = json.dumps(data, indent=2)
    print(pretty_json)
else:
    print("Error: Unable to retrieve data from The MET API")