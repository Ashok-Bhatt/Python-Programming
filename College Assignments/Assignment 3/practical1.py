import csv

with open("enrollment.csv","w", newline="") as newfile:
    w = csv.writer(newfile)
    w.writerow(["Enrollment No.","Name","Machine Leraning","Data Science","Data Structures and Algorithms","Advanced Web Development","Mobile Computing"])

    for i in range(5):
        employment = input(f"\nEnter your Enrollment number of student {i+1}:")
        name = input("Enter your name of student:")
        ml = int(input("Enter the marks of Machine Learning:"))
        ds = int(input("Enter the marks of Data Science:"))
        dsa = int(input("Enter the marks of Data Structures and Algorithms:"))
        awd = int(input("Enter the marks of Advanced Web Development:"))
        mc = int(input("Enter the marks of Mobile Computing:"))

        w.writerow([employment,name,ml,ds,dsa,awd,mc])