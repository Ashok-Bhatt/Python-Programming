import matplotlib.pyplot as plt

middle = 0
left = 1
right = 2
bottom = 4
top = 8

def checkpoint(p):
    total = 0
    if (xmin<=p[0]<=xmax and xmin<=p[1]<=xmax):
        return total
    else:
        if xmin<=p[0]<=xmax:
            if p[1]>20:
                total = total + top
            else:
                total = total + bottom
        if ymin<=p[1]<=ymax:
            if p[0]>20:
                total = total + right
            else:
                total = total + left
    return total

def find_points(first, second):
    slope = (first[1]-second[1])/(first[0]-second[0])
    if (checkpoint(first) == 0):
        inside = first
        outside = second
    else:
        inside = second
        outside = first

    if (checkpoint(outside)==left):
        xnew = xmin
        ynew = inside[1] + slope*(xnew-inside[0])
    elif (checkpoint(outside)==right):
        xnew = xmax
        ynew = inside[1] + slope*(xnew-inside[0])
    elif (checkpoint(outside)==bottom):
        ynew = ymin
        xnew = inside[0] + (ynew-inside[1])/slope
    else:
        ynew = ymax
        xnew = inside[0] + (ynew-inside[1])/slope

    return ((xnew,ynew),inside,outside)

def check_line(x , y):
    first = checkpoint(x)
    second = checkpoint(y)
    if (first | second == 0):
        plt.plot((x[0],y[0]) , (x[1],y[1]) , color="red" , linestyle="solid")
    elif (first & second != 0):
        plt.plot((x[0],y[0]) , (x[1],y[1]) , color="blue" , linestyle="dashed")
    else:
        new_points = find_points(x,y)
        plt.plot((new_points[0][0], new_points[1][0]) , (new_points[0][1], new_points[1][1]) , color="red" , linestyle="solid")
        plt.plot((new_points[0][0], new_points[2][0]) , (new_points[0][1], new_points[2][1]) , color="blue" , linestyle="dashed")

xmin = 0
ymin = 0
xmax = 20
ymax = 20

plt.plot((xmin, xmin),(ymin-20, ymax+20), color = "black")
plt.plot((xmax, xmax),(ymin-20, ymax+20), color = "black")
plt.plot((xmin-20, xmax+20),(ymax, ymax), color = "black")
plt.plot((xmin-20, xmax+20),(ymin, ymin), color = "black")

check_line((10,10),(15,10))
check_line((-10,5),(-10,19))
check_line((-5,5),(10,6))
check_line((15,15),(20,25))

plt.xticks([x for x in range(-20,41,10)])
plt.yticks([x for x in range(-20,41,10)])
plt.show()