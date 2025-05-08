import array as arr

def linear_search(array1, key):
    for index,element in enumerate(array1):
        if element==key:
            return index
    return -1

array1 = arr.array("i",[2,5,1,13,9,10,4,0])
print(array1)

key = int(input("Enter the element you want in an array:"))

position = linear_search(array1,key)
if (position==-1):
    print("Entered key is not present in the array.")
else:
    print(f"\nIndex of entered key: {position}")