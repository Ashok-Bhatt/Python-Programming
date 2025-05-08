x = int(input("Enter the number between 1 and 9:"))

if x<1 or x>9:
    raise ValueError("The value should be between 1 and 9.")
else:
    print(x)