# Write a Python program to find the even-length words from a given list of words and sort them by length

list1=input("Enter the list elements separated by the commas:")
list2=list1.split(",")
print("The entered list is given by:",list2)

list3=[]
for i in list2:
    if len(i)%2==0:
        list3.append(i)
print("The list having elements with even number of letters is given by:",list3)

print("The required list is given by:",sorted(list3))