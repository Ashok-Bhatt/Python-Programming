def poly_sqrt(a,b,c):
    descriminant=((b)**2)-(4*a*c)
    if descriminant<0:
        print("Your quadratic equation does not have any real root.")
    elif descriminant==0:
        root=-b/(2*a)
        print("Following equarion has unique root that is:",root)
    else:
        root1=(-b+(descriminant)**(0.5))/(2*a)
        root2=(-b-(descriminant)**(0.5))/(2*a)
        print("The roots for quadratic equation are:{} and {}.".format(root1,root2))

if __name__=="__main__":
    poly_sqrt(1,4,1)