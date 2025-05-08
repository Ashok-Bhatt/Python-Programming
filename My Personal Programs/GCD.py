# num1 and num2 are two numbers whose GCD we want to find
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

def prime_factorization(num,list):
    """
    prime_factorization is used to get the list containing prime factors of a given number
    """
    i=2
    j=num
    while j!=1:
        if j%i==0:
            list.append(i)
            j=j/i
        else:
            i+=1
    print("The list prime factorization of {} is given by:{}".format(int(num),list))

if (num1<=0)|(num2<=0):
    print("Please enter only natural numbers:")
else:
    list1=[]
    list2=[]
    prime_factorization(num1,list1)
    prime_factorization(num2,list2)
    hcf=1
    for i in list1:
        if i in list2:
            hcf=hcf*i
            list2.remove(i)
    print("hcf({},{})={}".format(num1,num2,hcf))