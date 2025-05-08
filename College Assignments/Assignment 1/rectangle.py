class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

    def area(self):
        return self.length*self.breadth
    
length1 = float(input("Enter the length of a rectangle:"))
breadth1 = float(input("Enter the breadth of a rectangle:"))

r1 = Rectangle(length1, breadth1)
print(f"The perimeter of a rectangle is: {r1.perimeter()}")
print(f"The area of a rectangle is: {r1.area()}")

length2 = float(input("\nEnter the length of a rectangle:"))
breadth2 = float(input("Enter the breadth of a rectangle:"))

r2 = Rectangle(length2, breadth2)
print(f"The perimeter of a rectangle is: {r2.perimeter()}")
print(f"The area of a rectangle is: {r2.area()}")