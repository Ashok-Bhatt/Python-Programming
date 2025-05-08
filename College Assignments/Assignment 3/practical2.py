import csv

with open("employment.csv","w", newline="") as newfile:
    w = csv.writer(newfile)
    w.writerow(["Employment No.","Name","Salary"])

    for i in range(5):
        employment = input(f"\nEnter your Employment number of employment {i+1}:")
        name = input("Enter your name of employee:")
        salary = int(input("Enter your salary of employee:"))

        if salary>=5000:
            employment_list = [employment,name,salary]
            w.writerow(employment_list)