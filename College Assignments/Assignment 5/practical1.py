import numpy as np

array1 = np.array([[5,3,7,1],
                   [1,2,4,5],
                   [6,5,8,1],
                   [5,7,2,9]])

array2 = np.array([[5,3,7,1],
                   [1,2,4,5],
                   [6,5,8,1],
                   [5,7,2,9]])

print("Inputed array:")
print(array1)

for i in range(2):
    for j in range(4):
        temp = array1[i,j]
        array1[i,j] = array1[3-i, j]
        array1[3-i,j] = temp

print("\nArray after swapping the rows:")
print(array1)

for i in range(4):
    for j in range(2):
        temp = array2[i,j]
        array2[i,j] = array2[i, 3-j]
        array2[i, 3-j] = temp

print("\nArray after swapping the columns:")
print(array2)