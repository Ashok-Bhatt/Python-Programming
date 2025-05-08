# Write a Python program to check if a given positive integer is a power of two.

num=int(input("Enter the number:"))

if num<=0:
    print("PLease enter only positive integer.")
else:
    import math
    power=math.log(num)/math.log(2)
    if power%1==0:
        print(f"{num} is the power of 2 i.e. {num}=2^{int(power)}.")
    else:
        print(f"{num} is not the power of 2.")