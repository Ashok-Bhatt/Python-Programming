num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

try:
    result = num1/num2
    print(f"{num1}/{num2}={result}")
except Exception as e:
    print("Error occured:",e)
else:
    print("No exception occured.")
finally:
    print("Prrogram Ended.")