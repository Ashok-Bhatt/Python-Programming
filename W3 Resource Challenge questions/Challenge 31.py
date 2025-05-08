# Write a Python program to add two binary numbers

bin1 = int(input("Enter the first binary number:"))
bin2 = int(input("Enter the second number:"))

def binary_to_decimal(num,sum):
    length = 1 
    while  num>=1:
        sum += 2**(length-1)
        length += 1
        num = num//10

sum1=0
sum2=0
num1 = binary_to_decimal(bin1,sum1)
num2 = binary_to_decimal(bin2,sum2)

num = sum1 + sum2
print(f"The addition of binary numbers {bin1} and {bin2} is {bin(num)} in binary.")