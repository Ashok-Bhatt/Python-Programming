# Write a Python program to find the indices of the closest pair from a list of numbers

list1=input("Enter the list items separated by comma:")
list2=list1.split(",")
for i in range(len(list2)):
    list2[i]=float(list2[i])
print("The entered list is given by:",list2)

if len(list2)<=1:
    print("How could we find the pair of closest integers for list containing less than 2 elements.")
else:
    num1=list2[0]
    num2=list2[1]
    import math
    diff=math.fabs(num1-num2)
    for i in range(len(list2)):
        for j in range(len(i)-1):
            import math
            if math.fabs(i-j)<=diff:
                num1=list2[i]
                num2=list2[j]
    print(f"The indices of closest pair from a list of numbers are {num1} and {num2}.")