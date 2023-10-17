import requests
import json

# MET API endpoints
search_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'
object_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'

# Search for "Van Gogh" related objects on view with images
search_params = {
    'q': 'van gogh',
    'isOnView': True,
    'hasImages': True
}
# Make a GET request to The MET's API to retrieve object IDs
response = requests.get(search_url, params=search_params)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Initialize a list to store object titles
    object_titles = []

    # Retrieve more details for each object and extract the title
    for object_id in data['objectIDs']:
        object_response = requests.get(f'{object_url}{object_id}')
        if object_response.status_code == 200:
            object_data = object_response.json()
            title = object_data.get('title', 'Title not available')
            object_titles.append(title)

    # Print the list of object titles
    for title in object_titles:
        print(title)
else:
    print("Error: Unable to retrieve data from The MET API")

