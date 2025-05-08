from bs4 import BeautifulSoup
import re
import requests
import json
import time

# Getting the json data form the website
url = "https://api.edamam.com/api/recipes/v2"
params = {
    "type": "public",
    "q": input("Search: "),
    "app_id": "b2b7df57",
    "app_key": "a1969304e2cba59af8fffdd102d9e570",
}

response = requests.get(url, params=params)

if response.status_code == 200:

    data = response.json()
    pretty_json = json.dumps(data, indent=4)
    no_of_recipes = min(20, data["count"])

    for i in range(no_of_recipes):
        try:
            print(data["hits"][i]["recipe"]["url"])
            recipe_data = requests.get(data["hits"][i]["recipe"]["url"])
            soup = BeautifulSoup(recipe_data.text, "lxml")
            paragraphs = soup.find_all("p")
            file_text = ""

            for index, paragraph in enumerate(paragraphs):
                paragraph = paragraph.getText().strip()
                paragraph = "-"*50 + str(index+1) + "-"*50 + "\n" + paragraph
                file_text = file_text + paragraph
                
            with open(f"recipe_data/recipe_{i+1}.txt", "w") as file:
                file.write(file_text)
        except Exception as e:
            print("Error occurred!")
else:
    print(f"Error: {response.status_code}")