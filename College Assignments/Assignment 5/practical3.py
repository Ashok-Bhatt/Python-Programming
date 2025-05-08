import numpy as np

array1 = np.arange(1,13).reshape(3,4)
print("Initial array:")
print(array1)

array1[0][3] = 14

for i in range(3):
    for j in range(4):
        if array1[i][j] < 5:
            array1[i][j] = 111

for i in range(3):
    for j in range(4):
        if array1[i][j] > 7:
            array1[i][j] = 1111

print("\nArray after some operations:")
print(array1)