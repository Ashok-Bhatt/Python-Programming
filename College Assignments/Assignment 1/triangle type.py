class Triangle():

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

class Type(Triangle):

    def type_of_triangle(self):
        if (self.side1 == self.side2 == self.side3):
            return "Given triangle is a equilateral triangle."
        elif (self.side1!=self.side2 and self.side1!=self.side3 and self.side2!=self.side3):
            return "Given triangle is a scalene triangle."
        else:
            return "Given triangle is a isosceles triangle."
    
x = int(input("Enter the first side of the triangle:"))
y = int(input("Enter the second side of the triangle:"))
z = int(input("Enter the third side of the triangle:"))

my_triangle = Type(x,y,z)
print(my_triangle.type_of_triangle())