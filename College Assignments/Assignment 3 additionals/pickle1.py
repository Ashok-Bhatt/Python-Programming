import pickle
import os

os.chdir('Assignment 3 additionals')
ingredients = ["sugar","tea leaves","milk","water","ginger"]

with open("ingredients.bin", "wb") as f:
    pickle.dump(ingredients, f)

with open("ingredients.bin", "rb") as f:
    ingredients = pickle.load(f)

print(ingredients)