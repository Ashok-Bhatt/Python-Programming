# Given a list of numbers and a number to inject, write a Python program to create a list containing that number in between each pair of adjacent numbers

list1=input("Enter the list elements separated by comma:")
list2=list1.split(",")
num=int(input("Enter the number that lies between two elements:"))

for i in range(len(list2)):
    list2[i]=int(list2[i])
print("The entered list is given by:",list2)
print("The number that separates the list elements is:",num)

for i in range(1,2*len(list2)-1,2):
    list2.insert(i,num)
print("The newly created list is given by:",list2)