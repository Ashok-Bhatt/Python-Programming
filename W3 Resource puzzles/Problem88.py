# Write a Python program to find an integer (n >= 0) with the given number of even and odd digits

odd=int(input("Enter the number of odd digits in required number:"))
even=int(input("Enter the number of even digits in required number:"))

if ((odd<0)|(even<0))|((odd==0)&(even==0)):
    print("Invalid Input!")
else:
    list_even=["0","2","4","6","8"]
    list_odd=["1","3","5","7","9"]
    import random
    list2_odd=[]
    i=1
    while i<=odd:
        list2_odd.append(random.choice(list_odd))
        i+=1
    list2_even=[]
    j=1
    while j<=even:
        list2_even.append(random.choice(list_even))
        j+=1

    list2=list2_odd+list2_even
    random.shuffle(list2)
    str_list2=""
    for i in list2:
        str_list2+=i
    result=int(str_list2)
    print("The required number is:",result)