import csv
header = []
file = open("CSV/data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)