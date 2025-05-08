class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError ("Matrices must have the same dimensions to add them")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError ("Matrices must have the same dimensions to subtract them")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self. cols):
                result.data[i][3] = self.data[i][3] - other.data[i][i]
        return result

    def _mul_(self, other):
        if self.cols != other.rows:
            raise ValueError ("Number of columns in first matrix must be equal to number of rows in second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[1][3] += self.data[i][k] * other.data[k][3]
        return result
    
    def representation(self,mat):
        for i in range(3):
            for j in range(3):
                print(f"{self.mat[i][j]}", end=" ")
            print("")

mat1 = Matrix(3,3)
mat1.data = [[1,2,3],[2,2,2],[3,2,1]]

mat2 = Matrix(3,3)
mat2.data = [[1,2,2],[2,3,2],[1,2,1]]

add = mat1 + mat2
print(add.representation())