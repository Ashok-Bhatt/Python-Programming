import numpy as np

array1 = np.array(([2,5,1,8],[6,9,1,5],[1,0,4,7],[2,7,4,8]), dtype=int)
array2 = np.empty((4,4), dtype=int)

print("Array before any swapping:")
print(array1)

for i in range(4):
    array2[i] = array1[3-i]

print("\nArray after swapping the rows:")
print(array2)

for i in range(4):
    array2[:,i] = array1[:,3-i]

print("\nArray after swapping the columns:")
print(array2)