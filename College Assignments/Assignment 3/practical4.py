import csv

with open("practical3.csv","r") as newfile:
    w = csv.DictReader(newfile)
    x = list(w)

    print(x)