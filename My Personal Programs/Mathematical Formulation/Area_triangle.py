# first,second and third denotes the length of all three sides of a triangle
first=float(input("Enter the first side of triangle:"))
second=float(input("Enter the second side of triangle:"))
third=float(input("Enter the third side of triangle:"))

if (first<=0)|(second<=0)|(third<=0):
    print("Come On Bro! The length of side of triangle cannot be zero or negative.")
else:
    semi=(first+second+third)/2
    area=((semi)*(semi-first)*(semi-second)*(semi-third))**(0.5)
    print("The area of triangle as per given parameters is:",area)