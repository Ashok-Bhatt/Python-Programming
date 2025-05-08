import array as arr

def merge(arr, s, e):

    mid = (s+e)//2

    len1 = mid - s + 1
    len2 = e - mid

    array1 = [None]*len1
    array2 = [None]*len2

    for i in range(len1):
        array1[i] = arr[s+i]

    for i in range(len2):
        array2[i] = arr[mid+1+i]
    
    index1 = 0
    index2 = 0
    counter = s

    while (index1<len1 and index2<len2):
        if array1[index1] < array2[index2]:
            arr[counter] = array1[index1]  
            index1 = index1 + 1
        else:
            arr[counter] = array2[index2]  
            index2 = index2 + 1
        counter = counter + 1

    while (index1<len1):
        arr[counter] = array1[index1]
        index1 = index1 + 1
        counter = counter + 1

    while (index2<len2):
        arr[counter] = array2[index2]
        index2 = index2 + 1
        counter = counter + 1

def merge_sort(arr, s, e):

    if s>=e:
        return
    
    mid = (s+e)//2

    merge_sort(arr, s, mid)
    merge_sort(arr, mid+1, e)
    merge(arr, s, e)

array1 = arr.array("i",(map(int, input("Enter the array elements separated by space: ").split())))

print("\nArray before sorting:")
print(array1)

merge_sort(array1, 0, len(array1)-1)

print("\nArray after sorting:")
print(array1)