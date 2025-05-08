# Write a Python program to check if an integer is the power of another integer.

num1=int(input("Enter the first number which is your assumed base:"))
num2=int(input("Enter the second number which is your assumed result:"))

if num1<=0 or num2<=0:
    print("PLease! Enter only natural numbers.")
else:
    import math
    power=math.log(num2)/math.log(num1)
    if power%1==0:
        print(f"{num2} is the power of {num1} i.e. {num2}={num1}^{int(power)}.")
    else:
        print(f"{num2} is not the power of {num1}.")