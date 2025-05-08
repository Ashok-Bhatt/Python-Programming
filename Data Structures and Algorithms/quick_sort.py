import array as arr

def swap(arr,x,y):

    temporary = arr[x]
    arr[x] = arr[y]
    arr[y] = temporary

def partition(arr, s, e):

    cnt = 0
    pivot = s

    for i in range(s+1,e+1):
        if arr[i] <= arr[pivot]:
            cnt = cnt + 1

    pivot = s + cnt
    swap(arr, pivot, s)

    i = s
    j = e
    while (i<pivot and j>pivot):
        while (arr[i] < arr[pivot]):
            i = i + 1
        while (arr[j] > arr[pivot]):
            j = j - 1
        if (i<pivot and j>pivot):
            swap(arr, i, j)

    return pivot

def quick_sort(arr, s, e):

    if s>=e:
        return
    
    p = partition(arr, s, e)

    quick_sort(arr, s, p-1)
    quick_sort(arr, p+1, e)

array1 = arr.array("i",map(int, input("Enter the array elements separated by space: ").split()))

print("\nArray before sorting:")
print(array1)

quick_sort(array1, 0, len(array1)-1)

print("\nArray after sorting:")
print(array1)