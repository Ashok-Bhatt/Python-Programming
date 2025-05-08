import requests
import json

api_key = "36a010f1b6e04bb2b734e6dab8ee3040"
url = "http://www.foodista.com/recipe/YZL84J6K/curry-fish-with-peas/"
encoded_url = requests.utils.quote(url, safe='')

headers = {"Content-Type": "application/json"}

response = requests.get(f"https://api.spoonacular.com/recipes/extract?url={encoded_url}&apiKey={api_key}", headers=headers)
data = response.json()

if response.status_code == 200:
    prettified_data = json.dumps(data, indent=4)

    with open("extracted_recipe.txt", "w") as file:
        file.write(prettified_data)
else:
    print("Error:", response.status_code, response.text)