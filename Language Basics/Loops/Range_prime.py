# num defines the range of numbers for which you want to check whether is prime or not
num = int(input("Enter the number which will be the range:"))
print("The prime numbers in the given range are:",end=" ")
for i in range(2,num+1):
    # For this loop, we are taking the terminating point i, instead of taking it i+1 because the final value of j will be equal to i, and the number divides itself for sure. So, even a prime number will be considered as a composite number by the program
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")