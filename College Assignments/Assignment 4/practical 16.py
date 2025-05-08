import numpy as np

matrix1 = np.arange(1,10).reshape(3,3)
print(matrix1)
for i in range(3):
    print(f"Column {i+1}: {np.sum((matrix1[0:3,i]))}")
    print(f"Row {i+1}: {np.sum((matrix1[i]))}")