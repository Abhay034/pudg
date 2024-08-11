import requests
import json

url = "https://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data=1, indent=4))
else:
    print(f"Failed to retrive data. HTTP status code: {response.status_code}")