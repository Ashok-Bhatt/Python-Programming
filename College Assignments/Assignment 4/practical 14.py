import numpy as np

matrix1 = np.arange(1,10).reshape(3,3)
print(matrix1)
print("Standard Deviation:",np.var(matrix1)**(1/2))