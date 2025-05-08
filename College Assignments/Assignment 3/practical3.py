import csv

list1 = [["Name","Age","Language"],["Ashok Bhatt",18,"Javascript and Python"],["Shivam Patel",18,"Python and C++"],["Meet Patel",19,"Javascript and Java"]]

with open("practical3.csv","w+", newline="") as newfile:
    w = csv.writer(newfile)
    for i in list1:
        w.writerow(i)
    
    newfile.seek(0)
    
    r = csv.reader(newfile)
    for i in r:
        print(i)