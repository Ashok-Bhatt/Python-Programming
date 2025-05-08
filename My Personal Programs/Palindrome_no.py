num=int(input("Enter the number that you want to verify whether it is palindrome or not:"))
if num<0:
    print("Please! Enter only zero or positive number.")
else:
    str_num=str(num)
    z=""
    for i in range(len(str_num)):
        z+=str_num[-(i+1)]
    print("The reverse of provided number is:",int(z))
    if str_num==z:
        print("The provided number is a palindrome.")
    else:
        print("The provided number is not a palindrome.")