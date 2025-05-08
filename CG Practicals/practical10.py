import matplotlib.pyplot as plt

def plot_polygon(p):
    for i in range(len(p)):
        plt.plot((p[i][0],p[(i+1)%len(p)][0]) , (p[i][1],p[(i+1)%len(p)][1]))

def find_intersection(first,second,side):
    slope = (first[1]-second[1])/(first[0]-second[0])

    if (side==1):
        xnew = xmin
        ynew = first[1] + slope*(xnew-first[0])
    elif (side==2):
        xnew = xmax
        ynew = first[1] + slope*(xnew-first[0])
    elif (side==3):
        ynew = ymin
        xnew = first[0] + (ynew-first[1])/slope
    else:
        ynew = ymax
        xnew = first[0] + (ynew-first[1])/slope
    
    return (xnew,ynew)

def check_region(x,y,z):
    first = 1
    second = 1

    if (z==1 and x[0]<xmin):
        first = 0
    elif (z==2 and x[1]>ymax):
        first = 0
    elif (z==3 and x[0]>xmax):
        first = 0
    elif (z==4 and x[1]<ymin):
        first = 0

    if (z==1 and y[0]<xmin):
        second = 0
    elif (z==2 and y[1]>ymax):
        second = 0
    elif (z==3 and y[0]>xmax):
        second = 0
    elif (z==4 and y[1]<ymin):
        second = 0
    
    return (first,second)

def leftside_clipping(p):
    points = []
    for i in range(len(p)):
        adding_points = check_region(p[i],p[(i+1)%len(p)], 1)
        if (adding_points == (1,1)):
            points.append(p[(i+1)%len(p)])
        elif (adding_points == (1,0)):
            intersection_point = find_intersection(p[i],p[(i+1)%len(p)], 1)
            points.append(intersection_point)
        elif (adding_points == (0,1)):
            intersection_point = find_intersection(p[i],p[(i+1)%len(p)], 1)
            points.append(intersection_point)
            points.append(p[(i+1)%len(p)])
    plt.plot(points)


points = [(-5,5) , (10,25) , (25,5)]

xmin = 0
ymin = 0
xmax = 20
ymax = 20

plt.plot((xmin, xmin),(ymin-20, ymax+20), color = "black")
plt.plot((xmax, xmax),(ymin-20, ymax+20), color = "black")
plt.plot((xmin-20, xmax+20),(ymax, ymax), color = "black")
plt.plot((xmin-20, xmax+20),(ymin, ymin), color = "black")

leftside_clipping(points)

plt.xticks([x for x in range(-20,41,10)])
plt.yticks([x for x in range(-20,41,10)])
plt.show()