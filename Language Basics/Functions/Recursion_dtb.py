string=""
def decimal_to_binary(n):
    global string
    if n == 1:
        string = "1" + string
        print(string)
    else:
        string = str(n%2) + string
        decimal_to_binary(n//2)

num = int(input("Enter the decimal number whose binary you want:"))
if num<0:
    print("Please! Enter the whole number.")
else:
    print(f"The binary of {num} is",end=" ")
    decimal_to_binary(num)