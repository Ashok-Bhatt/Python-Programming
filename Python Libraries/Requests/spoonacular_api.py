import requests
import json

api_key = "36a010f1b6e04bb2b734e6dab8ee3040"

recipe_name = input('Enter recipe name: ')
offset = 20
number = 25
add_recipe_information = True
add_recipe_nutrition = False
add_recipe_instruction = True

url = f"https://api.spoonacular.com/recipes/complexSearch?query={recipe_name}&offset={offset}&number={number}&addRecipeInformation={add_recipe_information}&addRecipeNutrition={add_recipe_nutrition}&addRecipeInstructions={add_recipe_instruction}"
headers = {"Content-Type": "application/json"}

response = requests.get(f"{url}&apiKey={api_key}", headers=headers)
data = response.json()

if response.status_code == 200:
    prettified_data = json.dumps(data, indent=4)

    with open("spoonacular_api_response.txt", "w") as file:
        file.write(prettified_data)
else:
    print("Error")