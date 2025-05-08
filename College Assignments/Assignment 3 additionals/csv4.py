import csv
import os

os.chdir('Assignment 3 additionals')
with open("item details.csv",newline='') as filename, open("highly.csv",newline='',mode='w') as output:
    reader = csv.reader(filename)
    writer = csv.writer(output)
    for i, row in enumerate(reader):
        no, name, price, category = row
        if i>=10:
            break
        elif int(price)>250:
            writer.writerow(row)