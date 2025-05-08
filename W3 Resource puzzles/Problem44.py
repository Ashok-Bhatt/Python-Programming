# Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum even value and its index. 
# In the case of a tie, return the smallest index. If there are no even numbers, the answer is []

# list1 is the string which contains list elements separated by the comma which will be splitted and then stored in list2
list1=input("Enter the list elements separated by comma:")
# list2 will contain all the elements splitted from list1 by comma
list2=list1.split(",")
for i in range(len(list2)):
    list2[i]=int(list2[i])
print("The list enetered by the user is:",list2)

# list3 is an empty list, which will be stored by the even numbers present in list2
list3=[]
for i in list2:
    if i%2==0:
        list3.append(i)
print("The list contained even numbers from user's list is given by:",list3)

if list3==[]:
    print(list3)
else:
    min_value=min(list3)
    print(f"The smallest even value from the list is {min_value} and it's index is {list3.index(min_value)}")