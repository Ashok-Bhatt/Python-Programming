import matplotlib.pyplot as plt

def put_pixel(x,y):
    plt.scatter(x,y)
    plt.scatter(-x,y)
    plt.scatter(x,-y)
    plt.scatter(-x,-y)
    plt.scatter(y,x)
    plt.scatter(-y,x)
    plt.scatter(y,-x)
    plt.scatter(-y,-x)

#x1, y1 = map(int, input("Enter x and y coordinates of the circle separated by space:").split())
radius = int(input("Enter the radius of the circle:"))

x = 0
y = radius
p = 1-radius

while x<=y:
    # if (x1,y1)==(0,0):
    #     plt.scatter(x,y)
    # else:
    put_pixel(x,y)

    if p<0:
        x = x + 1
        y = y
        p = p + 2*(x) + 1
    else:
        x = x + 1
        y = y - 1
        p = p + 2*(x-y) + 1

plt.show()