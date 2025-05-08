"""
num1 and num2 are two numbers between which we want to find the sum of n natural numbers ,
sum of square of n natural numbers and sum of cube of n natural numbers
"""
num1=int(input("Enter the starting number:"))
num2=int(input("Enter the ending number:"))

if (num1<=0)|(num2<=0):
    print("Please enter only natural numbers.")
elif (num2<num1):
    print("Second number cannot be greater than first one.")
elif (num1==num2):
    print("The value of given number:",num1)
    print("The value of square of given number:",num1**2)
    print("The value of cube of given number:",num1**3)
else:
    if (num1==1):
        print("The sum of first {} natural numbers is {}.".format(num2,(num2)*(num2+1)/2))
        print("The sum of squares of first {} natural numbers is {}.".format(num2,(num2)*(num2+1)*(2*num2+1)/6))
        print("The sum of cubes of first {} natural numbers is {}.".format(num2,((num2)*(num2+1)/2)**2))
    else:
        print("The sum of natural numbers from {} to {} is {}".format(num1,num2,((num2)*(num2+1)/2-(num1)*(num1+1)/2+num1)))
        print("The sum of squares of natural numbers from {} to {} is {}".format(num1,num2,((num2)*(num2+1)*(2*num2+1)/6-(num1)*(num1+1)*(2*num1+1)/6+(num1)**2)))
        print("The sum of natural numbers from {} to {} is {}".format(num1,num2,(((num2)*(num2+1)/2)**2-((num1)*(num1+1)/2)**2+(num1)**3)))