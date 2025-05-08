import requests
import json
import sys

api_key = "36a010f1b6e04bb2b734e6dab8ee3040"

id = int(input("Enter the id of recipe: "))
include_nutrition = False
number = 1000
url = f"https://api.spoonacular.com/recipes/{id}/similar?apiKey={api_key}&number={number}"
headers = {"Content-Type": "application/json"}

response = requests.get(url, headers=headers)
data = response.json()

if response.status_code == 200:
    prettified_data = json.dumps(data, indent=4)

    print(sys.getsizeof(data))
    print(sys.getsizeof(prettified_data))

    with open("recommended_recipes_response.txt", "w") as file:
        file.write(prettified_data)
else:
    print("Error")