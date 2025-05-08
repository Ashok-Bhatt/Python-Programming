# Write a Python program to test a list of ten integers between 0 and 99, which all differ by ten from one another. Return true or false.

list1=str(input("Enter the list of numbers separated by comma:"))
list2=list1.split(",")
print("The entered list is given by:",list2)
if (int(list2[0])>0 and int(list2[-1])<99):
    if len(list2)==10:
        for i in range(1,len(list2)):
            if int(list2[i])-int(list2[i-1])==10:
                if i==len(list2)-1:
                    print("Condition verified!")
                else:
                    continue
            else:
                if i==len(list2)-1:
                    print("The difference between each pair of consecutive elements should be 10.")
                else:
                    continue
    else:
        print("The number of elements should be 10, not more or not less.")
else:
    print("The elements of list is not in given range.")