# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.

num=int(input("Enter the number:"))
str_num=str(num)

list_num=[]
for i in str_num:
    if int(i)%2!=0:
        list_num.append(int(i))

product_list=1
for i in list_num:
    product_list*=i

if product_list==1:
    print("Sorry Bro! But your number does not contain any odd number.\nHence required product is 0.")
else:
    print("The required product is:",product_list)