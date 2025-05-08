import csv
file = open("CSV/data.csv")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
for i in rows:
    print(i)