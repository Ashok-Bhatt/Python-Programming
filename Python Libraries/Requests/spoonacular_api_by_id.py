import requests
import json

api_key = "36a010f1b6e04bb2b734e6dab8ee3040"

id = int(input("Enter the id of recipe: "))
include_nutrition = True
url = f"https://api.spoonacular.com/recipes/{id}/information?apiKey={api_key}&includeNutrition={include_nutrition}"
headers = {"Content-Type": "application/json"}

response = requests.get(url, headers=headers)
data = response.json()

if response.status_code == 200:
    prettified_data = json.dumps(data, indent=4)

    with open("spoonacular_api_by_id_response.txt", "w") as file:
        file.write(prettified_data)
else:
    print("Error")