num = int(input("Enter the number:"))

y = lambda x: (x >= 10 and x <= 20)
if y(num):
    print(f"{num} is between 10 and 20.")
else:
    print(f"{num} is not between 10 and 20.")