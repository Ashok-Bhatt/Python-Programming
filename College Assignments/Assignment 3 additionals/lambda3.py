num = int(input("Enter the number:"))

y = lambda x: x%2
if y(num):
    print(f"{num} is odd number.")
else:
    print(f"{num} is even number.")