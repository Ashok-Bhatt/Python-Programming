list1=[1,4,2,7,3,6]
print("The list1 is given by:",list1)

# List can contain any another data type inside it
list2=["Ashok",True,2.3,6]
print("The mixed list2 is given by:",list2)
for i in range(len(list2)):
    print("The data type of element {} is {}.".format(i+1,type(list2[i])))

print("The sorted list1 is given by:",list1.sort())
print("The elements of list1 in descending order is given by:",list1.sort(reverse=True))
print("The reversed list1 is given by:",list1.reverse())
print("The index of 7 in list1 is given by:",list1.index(7))

# We can even typecast the range function into list data type as range function is also a data type of itself
print("The list containing all the numbers from 1 to 20 is:",list(range(1,21)))

repeated_list=[1,2,3,2,3,1]
print("The list before removing 1 is given by:",repeated_list)
repeated_list.remove(1)
print("The list after removing 1 is given by:",repeated_list)