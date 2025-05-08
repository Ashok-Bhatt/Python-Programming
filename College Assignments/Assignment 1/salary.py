class Outofrange(Exception):
    pass

def check_salary():
    try:
        salary = int(input("Enter the salary: "))
        if 5000 <= salary <= 10000:
            print("You salary is valid")
        else: 
            raise Outofrange
    except Outofrange:
        print("Your salary should vary between 5k to 10k")

check_salary()