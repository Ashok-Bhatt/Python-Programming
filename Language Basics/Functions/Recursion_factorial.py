def factorial(num):
    """
    The factorial function helps to find the factorial of a required number.
    The number should be only zero or positive number.
    """
    if (num<0):
        txt="Please! Enter only zero or positive number. Negative numbers don't have factorial."
        return txt
    if (num==0) or (num==1):
        return 1
    else:
        return num*factorial(num-1)
    
num=int(input("Enter the number whose factorial you want to find:"))

if num>=0:
    print("The factorial of a given number is:",factorial(num))
else:
    print(factorial(num))