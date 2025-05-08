import array as arr

def insertion_sort(unsorted_array):
    for i in range(1,len(unsorted_array)):
        key = unsorted_array[i]
        j = i-1
        while j>=0 and unsorted_array[j]>key:
            unsorted_array[j+1] = unsorted_array[j]
            j = j-1
        unsorted_array[j+1] = key

array1 = arr.array("i",(map(int, input("Enter the array elements separated by space: ").split())))
print("\nArray before sorting:")
print(array1)

insertion_sort(array1)
print("\nArray after sorting:")
print(array1)