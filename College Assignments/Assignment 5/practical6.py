import numpy as np

vector1 = np.arange(0,21)
print("Vector before: ", end=" ")
print(vector1)

for i in range(20):
    if vector1[i]>=9 and vector1[i]<=15:
        vector1[i] = -vector1[i]

print("Vector after : ", end=" ")
print(vector1)