import csv
list1 = []

with open("employment.csv","r") as newfile:
    w = csv.reader(newfile)

    for i in w:
        list1.append(i)

print("First three enteries are as follows:")
for i in list1[1:4]:
    print(f"Employment No.: {i[0]}      Name:{i[1]}     Salary:{i[2]}")