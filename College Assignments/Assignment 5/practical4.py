import numpy as np

array1 = np.zeros((5,6), dtype=int)
print("Given array:")
print(array1)

for i in range(5):
    for j in range(0,6,2):
        if i%2==0:
            array1[i][j] = 3
        else:
            array1[i][j] = 7

print("\nArray after operations:")
print(array1)