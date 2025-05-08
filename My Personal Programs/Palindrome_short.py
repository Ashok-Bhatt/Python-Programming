num=int(input("Enter the number that you want to check whether it is palindrome or not:"))
str_num=str(num)
if num<0:
    print("Please! Enter only positive number or zero:")
else:
    reverse_num=str_num[::-1]
    reverse=int(reverse_num)
    print("The reverse of given number is:",reverse)
if num==reverse:
    print("The given number is palindrome.")
else:
    print("The given number is not a palindrome.")