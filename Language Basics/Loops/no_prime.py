num = int(input("Enter the number of prime numbers you want:"))     # num defines the number of prime numbers required
if num<=0:
    print("The number of terms cannot be zero or negative.")
else:
    print(f"The first {num} prime numbers is/are:",end=" ")
    count=1
    i=2
    while count<=num:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
            count+=1
        i+=1