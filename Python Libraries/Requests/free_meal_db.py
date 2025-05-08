import requests
import json

""" Search by recipe name:
https://www.themealdb.com/api/json/v1/1/search.php?s=rice """

url = "https://www.themealdb.com/api/json/v1/1/random.php"

for _ in range(100):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prettified_data = json.dumps(data, indent=4)
        with open("free_meal_db_response.txt", "w") as file:
            file.write(prettified_data)
        try:
            with open("random_receipes.txt", "a") as file:
                file.write(data["meals"][0]["strMeal"] + "\n")
        except UnicodeDecodeError as e:
            print(e)
        except Exception as e:
            print(e)