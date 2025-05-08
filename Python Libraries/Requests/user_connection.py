import requests
import json

url = "https://api.spoonacular.com/users/connect"
api_key = "36a010f1b6e04bb2b734e6dab8ee3040"
response_headers = {
    "Content-Type": "application/json"
}

response = requests.post(f"{url}?apiKey={api_key}", headers=response_headers)

if (response.status_code == 200):
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print("Error Occurred")