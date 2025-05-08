import requests
import json

url = "https://api.api-ninjas.com/v1/recipe"
headers = {
    'X-Api-Key': 'your_api_key'
}

response = requests.get(url, header=headers)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    prettified_data = json.loads(data, indent=4)

    print(prettified_data)

    with open("api_ninjas_recipe.txt", "w") as file:
        file.write(prettified_data)