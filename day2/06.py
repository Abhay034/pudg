import requests
import pandas as pd
import time

# URL of the API endpoint
url = "https://api.open-notify.org/iss-now.json"

# List to store the data
data = []

# Number of records you want to collect
num_records = 100

for i in range(num_records):
    try:
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response
        iss_data = response.json()
        
        # Extract the latitude, longitude, and timestamp
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        timestamp = iss_data['timestamp']
        
        # Append the data to the list
        data.append({
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude
        })
        
        # Wait for a few seconds before the next request to avoid overwhelming the server
        time.sleep(5)  # 5-second delay between requests

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        break

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('iss_location_data.csv', index=False)

print("Data collection completed. Saved to 'iss_location_data.csv'.")
