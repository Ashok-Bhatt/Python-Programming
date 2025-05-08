# num1 defines the starting point of range of numbers 
# num 2 defines the ending point of range of numbers
num1 = int(input("Enter the starting number of the range:"))
num2 = int(input("Enter the ending number of the range:"))
print("The prime numbers in the given range are:")
if num2>=num1:
    for i in range(num1,num2+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
else:
    print("The ending index cannot be smaller than starting index.")