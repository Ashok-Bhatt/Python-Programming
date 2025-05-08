# Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
# "4 mod 34" means we should get remainder 4 on dividing som number with 34

num=int(input("Enter the number:"))
if (num>=4**4) and (num%34==4):
    print("The number is greater than 4^4 and return remainder 4 on dividing with 34.")
else:
    print("The number is less than 4^4 or does not return remainder 4 on dividing with 34.")