class Triangle():
    no_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False
    
x = int(input("Enter the first angle of the triangle:"))
y = int(input("Enter the second angle of the triangle:"))
z = int(input("Enter the third angle of the triangle:"))

my_triangle = Triangle(x,y,z)

print(f"The number of sides of a triangle is {my_triangle.no_of_sides}")

if my_triangle.check_angles():
    print("The sum of angles of a triangle is 180.")
else:
    print("The sum of angles of a triangle is not 180.")