# Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.

text=str(input("Enter the list items separated by comma:"))
list1=text.split(",")
print("The given list is:",list1)

set_last=set()
for i in list1[-1]:
    set_last.add(i)
set_last2=set()
for i in list1[-2]:
    set_last2.add(i)

if (set_last2!=set_last) and set_last2.issubset(set_last):
    print("Yes! The second last element is the proper substring of last element.")
else:
    print("No! The second last element is not the proper substring of last element.")