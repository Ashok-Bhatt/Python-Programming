# Write a Python program to find four positive even integers whose sum is a given integer

num=int(input("Enter the even integer:"))

if num%2!=0:
    print("There's no way to find four positive even integers whose sum is odd.")
else:
    if num<0:
        print("There's no way to find four positive even integers whose sum is negative number.")
    else:
        import random
        list1=[]
        for count in range(3):
            element=((random.randint(0,num/2))*2)
            list1.append(element)
            num-=element
        else:
            list1.append(num)
print("The list containing four positive even integers whose sum is entered number is given by:",list1)