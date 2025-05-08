import requests
import json

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



    with open("response.txt", "w") as file:
        file.write(pretty_json)

    with open("response_count.txt", "a") as file:
        file.write(f"{params['q']} : {data['count']}" + "\n")

    if data['count'] > 20:
        print(data["_links"]["next"]["href"])

        new_response = requests.get(data["_links"]["next"]["href"], params=params)
        new_data = new_response.json()
        pretty_json = json.dumps(new_data, indent=4)

        with open("response2.txt", "w") as file:
            file.write(pretty_json)
else:
    print(f"Error: {response.status_code}")