a=float(input("Enter the coefficient of the x^2:"))
b=float(input("Enter the coefficient of the x:"))
c=float(input("Enter the coefficient of the constant term:"))

descriminant=((b)**2)-(4*a*c)
if descriminant<0:
    print("Your quadratic equation does not have any real root.")
elif descriminant==0:
    root=-b/(2*a)
    print("Following equarion has unique root that is:",root)
    print("Above value is approximately.")
else:
    root1=(-b+(descriminant)**(0.5))/(2*a)
    root2=(-b-(descriminant)**(0.5))/(2*a)
    print("The roots for quadratic equation are:{} and {}.".format(root1,root2))
    print("Above values are approximately.")