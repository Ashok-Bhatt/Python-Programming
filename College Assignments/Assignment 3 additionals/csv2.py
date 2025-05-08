import csv
import os

os.chdir('Assignment 3 additionals')
with open("item details.csv",newline='') as filename:
    reader = csv.reader(filename)
    print(f"{'Item No.': <10}{'Name': <30}{'Price': <10}{'Category': <20}")
    for i, row in enumerate(reader):
        if i>=10:
            break
        no, name, price, category = row
        print(f"{no: <10}{name: <30}{price: <10}{category: <20}")