from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def perimeter():
        pass

    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius

    def area(self):
        return 3.14*(self.radius*self.radius)

class Triangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        hypotenuse = ((self.side1)**2 + (self.side2)**2)**0.5
        return self.side1 + self.side2 + hypotenuse

    def area(self):
        return 0.5*self.side1*self.side2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

    def area(self):
        return self.length*self.breadth

r = float(input("Enter the radius of the circle:"))

c1 = Circle(r)
print(f"The area of a circle is: {c1.area()}")
print(f"The perimeter of a circle is: {c1.perimeter()}")

side1 = float(input("\nEnter the first side of a triangle:"))
side2 = float(input("Enter the second side of a triangle:"))

t1 = Triangle(side1,side2)
print(f"The perimeter of a triangle is: {t1.perimeter()}")
print(f"The area of a triangle is: {t1.area()}")

length = float(input("\nEnter the length of a rectangle:"))
breadth = float(input("Enter the breadth of a rectangle:"))

r1 = Rectangle(length, breadth)
print(f"The perimeter of a rectangle is: {r1.perimeter()}")
print(f"The area of a rectangle is: {r1.area()}")