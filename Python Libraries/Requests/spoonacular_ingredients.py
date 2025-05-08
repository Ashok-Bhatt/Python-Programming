import requests
import json

api_key = "36a010f1b6e04bb2b734e6dab8ee3040"

id = int(input("Enter the id of ingredient: "))
unit = "grams"
amount = "250"

url = f"https://api.spoonacular.com/food/ingredients/{id}/information?unit={unit}&amount={amount}&apiKey={api_key}"
headers = {"Content-Type": "application/json"}

response = requests.get(url, headers=headers)
data = response.json()

if response.status_code == 200:
    prettified_data = json.dumps(data, indent=4)

    with open("spoonacular_ingredients.txt", "w") as file:
        file.write(prettified_data)
else:
    print("Error")