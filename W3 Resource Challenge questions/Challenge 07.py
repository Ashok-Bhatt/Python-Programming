# Challenge 6: Write a Python program to check if a number is a power of a given base. (same as Challenge 5)

# Write a Python program to find a missing number from a list.

list_num=[2,5,7,5,8,3,9]
list_missing=[]

for i in range(min(list_num),max(list_num)+1):
    if i not in list_num:
        list_missing.append(i)

print("The missing elements in a given list are:",list_missing)