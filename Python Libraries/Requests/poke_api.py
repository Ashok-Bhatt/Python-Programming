import requests

url = "https://api.edamam.com/api/recipes/v2"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data.get("abilities"))
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")