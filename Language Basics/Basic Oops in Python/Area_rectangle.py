class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect1 = Rectangle(5, 10)
rect2 = Rectangle(15, 20)
rect3 = Rectangle(30, 40)
print("Area of rectangle 1:", rect1.area())
print("Area of rectangle 2:", rect2.area())
print("Area of rectangle 3:", rect3.area())