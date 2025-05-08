def fibonacci(num):
    """
fibonacci function is used to print required number of fibonacci terms
    """
    print(f"The first {num} fibonacci terms are:")
    i=0
    print(i,end=" ")
    j=1
    print(j,end=" ")
    no=2
    while no<num:
        k=i+j
        no+=1
        print(k,end=" ")
        i=j
        j=k
    print("")

def grade(web,python,maths,rpro):
    """
grade function is used to calculate the grade from the provided marks
    """
    percentage=(web+python+maths+rpro)*100/400
    print(f"You have scored {percentage}% in your first semester exam.")
    if percentage>70:
        print("You are passed with distinction.")
    elif percentage>60:
        print("You are passed with First Class.")
    elif percentage>50:
        print("You are passed with Second Class.")
    elif percentage>40:
        print("You are passed with Pass Class.")
    else:
        print("You are failed.")

def prime(num):
    """
prime is a function which states whether a number is prime or not
    """
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

choice=0
while choice!=4:
    print("\nOur provided services:\n1.To generate the fibonacci series\n2.To generate the grade from marks\n3.To check whether the number is prime number or not.\n4.Exit\n")
    choice=int(input("Enter the number to access the service:"))

    if choice==1:
        num=int(input("Enter the number of fibonacci terms required:"))
        fibonacci(num)

    elif choice==2:
        web=int(input("Enter the marks of Web Technology:"))
        python=int(input("Enter the marks of Programming in Python-1:"))
        maths=int(input("Enter the marks of Discrete Maths with Python:"))
        rpro=int(input("Enter the marks of R Programming for Data Science:"))
        grade(web,python,maths,rpro)

    elif choice==3:
        num=int(input("Enter the number which you want to check whether it's prime or not:"))
        prime(num)

    elif choice==4:
        print("\nThanks for using our services.")
        
    else:
        print("Invalid service number.")