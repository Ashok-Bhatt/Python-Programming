import numpy as np

array1 = np.empty((4,4), dtype=int)

print("Given array:")
print(array1)

array2 = array1.copy()
array2[0] = array1[3]
array2[3] = array1[0]

print("\nRequired array:")
print(array2)