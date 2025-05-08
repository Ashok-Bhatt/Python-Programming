# Write a Python program to check a given list of integers where the sum of the first i integers is i. 

list1=str(input("Enter the list of integers separated by commas:"))
list2=list1.split(",")
list2=list(map(lambda x:int(x),list2))
print("The entered list is given by:",list2)

for i in range(len(list2)):
    if sum(list2[:i+1])!=i+1:
        print("The sum of first i integers is not i.")
        break
else:
    print("The sum of first i integers is i.")