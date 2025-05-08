list1=[]
ans="Y"
while ans=="Y":
    ans=input("Do you want to add element to the list?")
    if ans=="Y":
        element=input("Enter the student name:")
        list1.append(element)
    else:
        print("The final list is:",list1)