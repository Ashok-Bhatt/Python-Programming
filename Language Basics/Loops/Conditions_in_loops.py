for i in range(5):
    print(i+1,end=" ")
else:
    print("\nLoop exits.")

for i in range(5):
    print(i+1,end=" ")
    if i==2:
        break
else:
    print("The loop exits.")

print("")
num=int(input("Enter the range upto which you want to find the prime numbers:"))
if num<=0:
    print("The concept of prime numbers is not valid for the negative numbers or zero.")
elif num==1:
    print("1 is neither prime nor consonent number.It is a special number.")
else:
    print("The prime numbers in the given range are:",end=" ")
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")