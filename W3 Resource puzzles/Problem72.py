# Write a Python program to find the indices of three numbers that sum to 0 in a given list of numbers.

list1=input("Enter the elements of list separated by comma:")
list2=list1.split(",")
for i in range(len(list2)):
    list2[i]=int(list2[i])
print("The entered list is given by:",list2)

for i in range(len(list2)):
    for j in range(i):
        for k in range(j):
            if list2[i]+list2[j]+list2[k]==0:
                print("The indices of number whose sum is zero are: {}, {} and {}.".format(i,j,k))
else:
    print("There's no situation when the sum of any three numbers in the list was zero.")