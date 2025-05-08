import array as arr

def selection_sort(unsorted_array):
    for i in range(0,len(unsorted_array)-1):
        minimum = unsorted_array[i]
        for j in range(i+1,len(unsorted_array)):
            if unsorted_array[j]<minimum:
                temporary = minimum
                unsorted_array[i] = unsorted_array[j]
                unsorted_array[j] = temporary
                #minimum = unsorted_array[i]

array1 = arr.array("i",(map(int, input("Enter the array elements separated by space: ").split())))
print("\nArray before sorting:")
print(array1)

selection_sort(array1)
print("\nArray after sorting:")
print(array1)