import numpy as np

print("Input:")
array1 = np.arange(1,26).reshape(5,5)
print(array1)

print("\nOutput1:")
print(array1[2:5,1:5])

print("\nOutput2:")
print(array1[4,4])

print("\nOutput3:")
print(array1[0:3,1:2])

print("\nOutput4:")
print(array1[4])

print("\nOutput5:")
print(array1[3:5])