# write a python program that accepts the list of integers and check the length of the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the said list.

list1=str(input("Enter the list of numbers separated by the commas:"))
list2=list1.split(",")
print(list2)

length_list2=len(list2)
fifth_list2=list2[4]
print("The length of the given list is:",length_list2)
print("The fifth element of the list is:",fifth_list2)
if (length_list2==8) and (list2.count(fifth_list2)==3):
    print("Well Done Bro! Condition Verified.")
else:
    print("No Bro! The length of the list should be 8 and fifth element should occur thrice in the given list.")