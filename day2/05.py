import requests

# URL of the API endpoint
url = "https://api.open-notify.org/iss-now.json"

try:
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    
    # Parse the JSON response
    data = response.json()
    
    # Extract the latitude, longitude, and timestamp
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    
    # Print the extracted values
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")

except requests.exceptions.ConnectionError:
    print("Failed to establish a connection to the server. Please check your network and try again.")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
