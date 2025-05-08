import random

def boundary_color(x,y,fill_digit, boundary_digit):

    if (polygon[x*10+y]!=boundary_digit and polygon[x*10+y]!=fill_digit):
        polygon[x*10+y] = fill_digit
        boundary_color(x+1,y,fill_digit, boundary_digit)
        boundary_color(x-1,y,fill_digit, boundary_digit)
        boundary_color(x,y+1,fill_digit, boundary_digit)
        boundary_color(x,y-1,fill_digit, boundary_digit)
        boundary_color(x-1,y-1,fill_digit, boundary_digit)
        boundary_color(x+1,y+1,fill_digit, boundary_digit)
        boundary_color(x-1,y+1,fill_digit, boundary_digit)
        boundary_color(x+1,y-1,fill_digit, boundary_digit)
        
polygon = ["*" if (x//10==0 or x//10==9 or x%10==0 or x%10==9) else 0 for x in range(100)]
x,y = random.randint(1,8),random.randint(1,8)

print("Before applying algorithm:\n")
for i in range(10):
    for j in range(10):
        print(polygon[10*i+j],end=" ")
    print("")

boundary_color(x,y,"#","*")
print("\nAfter applying algorithm:\n")

for i in range(10):
        for j in range(10):
            print(polygon[10*i+j],end=" ")
        print("")

"""
def boundary_color(x,y,fill_digit, boundary_digit):
    if (polygon[x][y]!=boundary_digit and polygon[x][y]!=fill_digit):
        polygon[x][y] = fill_digit
        boundary_color(x+1,y,fill_digit, boundary_digit)
        boundary_color(x-1,y,fill_digit, boundary_digit)
        boundary_color(x,y+1,fill_digit, boundary_digit)
        boundary_color(x,y-1,fill_digit, boundary_digit)
        boundary_color(x-1,y-1,fill_digit, boundary_digit)
        boundary_color(x+1,y+1,fill_digit, boundary_digit)
        boundary_color(x-1,y+1,fill_digit, boundary_digit)
        boundary_color(x+1,y-1,fill_digit, boundary_digit)
        
polygon = [[1,1,1,1,1,1],
           [1,0,0,0,0,1],
           [1,0,0,0,0,1],
           [1,0,0,0,0,1],
           [1,0,0,0,0,1],
           [1,1,1,1,1,1]]

print("Before applying algorithm:\n")
for i in polygon:
    for j in i:
        print(j,end=" ")
    print("")

boundary_color(3,3,8,1)

print("\nAfter applying algorithm:\n")
for i in polygon:
    for j in i:
        print(j,end=" ")
    print("")
"""