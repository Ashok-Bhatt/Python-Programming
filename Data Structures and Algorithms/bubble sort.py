import array as arr

def bubble_sort(array1):
    for i in range(len(array1)-1):
        flag = 0
        for j in range(0,len(array1)-i-1):
            if array1[j]>array1[j+1]:
                temporary = array1[j]
                array1[j] = array1[j+1]
                array1[j+1] = temporary
                flag = 1
        if flag==0:
            break

array1 = arr.array("i",(map(int, input("Enter the array elements separated by space: ").split())))
print("\nArray before sorting:")
print(array1)

bubble_sort(array1)
print("\nArray after sorting:")
print(array1)