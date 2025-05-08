class Circle():
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius

    def area(self):
        return 3.14*(self.radius*self.radius)

r1 = float(input("Enter the radius of the circle:"))
c1 = Circle(r1)
print(f"The area of a circle is: {c1.area()}")
print(f"The perimeter of a circle is: {c1.perimeter()}")

r1 = float(input("\nEnter the radius of the circle:"))
c1 = Circle(r1)
print(f"The area of a circle is: {c1.area()}")
print(f"The perimeter of a circle is: {c1.perimeter()}")