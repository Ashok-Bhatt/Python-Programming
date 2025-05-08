# Write a Pyhton program to compute and return the square root of a given 'integer'

num=int(input("Enter the number whose square root you want to find:"))

if num<0:
    print("Negative numbers cannot have square root.")
else:
    i=0
    while i*i<=num:
        i+=1
    print(f"The sqaure root of {num} to the nearest integer is {i-1}.")