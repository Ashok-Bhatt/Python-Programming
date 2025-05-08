num = int(input("Enter the number whose prime factorization you want to find:"))

if num<=0:
    print("Please! Enter only natural numbers.")
elif num==1:
    print("1 =",1)
else:
    factor_list=[]
    prime_factor = 2
    number=num
    while number!=1:
        if number % prime_factor==0:
            factor_list.append(prime_factor)
            number = number / prime_factor
        else:
            prime_factor+=1
    print(f"{num} = ",end="")
    for index,factors in enumerate(factor_list):
        if index==len(factor_list)-1:
            print(factors)
        else:
            print(factors,end=" X ")