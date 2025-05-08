import csv
list1 = []

with open("employment.csv","r") as newfile:
    w = csv.reader(newfile)

    for i in w:
        list1.append(i)
    
print(f"The no of entries in a data is {len(list1) - 1}.\n")
print("All the enteries are as follows:")
for i in list1[1:]:
    print(f"Employment No.: {i[0]}      Name:{i[1]}     Salary:{i[2]}")