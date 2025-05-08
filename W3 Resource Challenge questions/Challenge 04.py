# Write a Python program to check if a number is a perfect square

num=int(input("Enter the number:"))

if num<0:
    print("Please! Enter only whole number.")
else:
    i=0
    while i*i<=num:
        i=i+1
    i=i-1
    if num==i*i:
        print(f"{num} is a perfect square.")
    else:
        print(f"{num} is not a perfect square.")