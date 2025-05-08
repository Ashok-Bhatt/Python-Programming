import random

def boundary_color(x,y,old_digit, new_digit):

    if (polygon[x*10+y]==old_digit):
        polygon[x*10+y] = new_digit
        boundary_color(x+1,y,old_digit, new_digit)
        boundary_color(x-1,y,old_digit, new_digit)
        boundary_color(x,y+1,old_digit, new_digit)
        boundary_color(x,y-1,old_digit, new_digit)
        boundary_color(x-1,y-1,old_digit, new_digit)
        boundary_color(x+1,y+1,old_digit, new_digit)
        boundary_color(x-1,y+1,old_digit, new_digit)
        boundary_color(x+1,y-1,old_digit, new_digit)
        
polygon = ["@" if (x//10==0 or x//10==9) else "%" if (x%10==0 or x%10==9) else 0 for x in range(100)]
x,y = random.randint(1,8),random.randint(1,8)

print("Before applying algorithm:\n")
for i in range(10):
    for j in range(10):
        print(polygon[10*i+j],end=" ")
    print("")

boundary_color(x,y,0,"*")
print("\nAfter applying algorithm:\n")

for i in range(10):
        for j in range(10):
            print(polygon[10*i+j],end=" ")
        print("")

"""
def boundary_color(x,y,old_digit, new_digit):
    if (polygon[x][y]==old_digit):
        polygon[x][y] = new_digit
        boundary_color(x+1,y,old_digit, new_digit)
        boundary_color(x-1,y,old_digit, new_digit)
        boundary_color(x,y+1,old_digit, new_digit)
        boundary_color(x,y-1,old_digit, new_digit)
        boundary_color(x-1,y-1,old_digit, new_digit)
        boundary_color(x+1,y+1,old_digit, new_digit)
        boundary_color(x-1,y+1,old_digit, new_digit)
        boundary_color(x+1,y-1,old_digit, new_digit)
        
polygon = [[3,1,5,1,8,1],
           [1,0,0,0,0,4],
           [3,0,0,0,0,4],
           [5,0,0,0,0,1],
           [1,0,0,0,0,2],
           [8,1,6,9,1,6]]

print("Before applying algorithm:\n")
for i in polygon:
    for j in i:
        print(j,end=" ")
    print("")

boundary_color(3,3,0,"*")

print("\nAfter applying algorithm:\n")
for i in polygon:
    for j in i:
        print(j,end=" ")
    print("")
"""