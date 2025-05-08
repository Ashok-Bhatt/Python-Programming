import csv
list1 = []
sum = 0 

with open("invoice.csv","r") as newfile:
    w = csv.reader(newfile)

    for index,element in enumerate(w):
        list1.append(element)
        if index>0:
            sum = sum + int(list1[index][2])

for i in list1[1:]:
    print(f"{i[1]} : {i[2]}")
print(f"Total: {sum}")