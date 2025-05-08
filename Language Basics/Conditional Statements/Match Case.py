score=int(input("Enter the number:"))
match score:
    case 1:
        print("The number is 1.")
    case 2:
        print("The number is 2.")
    case _:
        print("The number is neither 1 nor 2.")

# providing the conditionals in the default case

x=int(input("Enter the number:"))
match x:
    case 1:
        print("The number is 1.")
    case 2:
        print("The number is 2.")
    case _ if x==3:
        print("The number is 3.")
    case _:
        print("The number is neither 1 nor 2 nor 3.")