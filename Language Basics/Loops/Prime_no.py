num=int(input("Enter the number which you want to check whether it is prime or not:"))

if num<=0:
    print("The concept of prime number is applicable to only natural numbers.")
elif num==1:
    print("1 is neither a prime number nor a composite number. 1 is a special number.")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
        else:
            continue
    else:
        print(f"{num} is a prime number.")