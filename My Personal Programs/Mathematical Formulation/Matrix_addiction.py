mat1=[
    [1,2,3],
    [4,1,3],
    [0,2,4]
]

mat2=[
    [2,4,1],
    [0,4,0],
    [1,3,2]
]

mat3=[[0,0,0],
      [0,0,0],
      [0,0,0]]

for row_index, row in enumerate(mat3):
    for element_index, element in enumerate(row):
        element = mat1[row_index][element_index] + mat2[row_index][element_index]
        mat3[row_index][element_index] = element

for i in mat3:
    for j in i:
        print(j,end=" ")
    print("")