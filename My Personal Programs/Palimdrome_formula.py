num=int(input("Enter the number which you want to check whether it's palimdrome or not:"))
if num<0:
    print("The number should be only positive.")
else:
    count=0
    num2=num
    while num2<1:
        num2/=10
        count+=1
    i=1
    reverse=0
    while i<=count:
        reverse+=(num//(10**(count-1-i)))*(i)
        num
        i+=1
        num%=(10**(count-1-i))
print("The reverse of a given number is:",reverse)
if reverse==num:
    print("The given number is a palimdrome.")
else:
    print("The given number is not an palimdrome")