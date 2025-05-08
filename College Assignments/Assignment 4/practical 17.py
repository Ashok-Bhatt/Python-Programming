import numpy as np

matrix1 = np.arange(1,10).reshape(3,3)
print(matrix1)

print(f"\nColumn    Min       Max")
for i in range(3):
    print(f"{i+1:<10}{np.min((matrix1[0:3,i])):<10}{np.max((matrix1[0:3,i])):<10}")

print(f"\nRow       Min       Max")
for i in range(3):
    print(f"{i+1:<10}{np.min((matrix1[i])):<10}{np.max((matrix1[i])):<10}")

    """ 
    print(f"Column {i+1}: \nMinimum:{np.min((matrix1[0:3,i]))} and Maximum:{np.max((matrix1[0:3,i]))}")
    print(f"Row {i+1}: \nMinimum:{np.min((matrix1[i]))} and Maximum:{np.max((matrix1[i]))}\n")
     """