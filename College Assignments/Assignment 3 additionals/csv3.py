import csv
import os

os.chdir('Assignment 3 additionals')
with open("item details.csv",newline='') as filename:
    reader = csv.reader(filename)
    item_no = int(input("Enter the item number:"))
    for i, row in enumerate(reader):
        no, name, price, category = row
        if i+1==item_no:
            print(f"Item No.: {no}")
            print(f"Name: {name}")
            print(f"Price: {price}")
            print(f"Category: {category}")
            break