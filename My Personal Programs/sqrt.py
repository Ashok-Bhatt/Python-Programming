num=int(input("Enter the number whose square root you want to find to the nearest digit whole number:"))
i=0
while i**2<=num:
    i+=1
i-=1
print("The value of the square root to the nearest integer of the entered number is given by:",i)