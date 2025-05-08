import matplotlib.pyplot as plt

x1,y1 = map(int, input("Enter x1,y1 separated by space:").split())
x2,y2 = map(int, input("Enter x2,y2 separated by space:").split())

dx = x2-x1
dy = y2-y1
x = x1
y = y1
m = dy/dx

while (x,y)<=(x2,y2):
    plt.scatter(x,y)
    if m<1:
        p = 2*dy - dx
        if p<0:
            x = x + 1
            y = y
            p = p + 2*dy
        else:
            x = x + 1
            y = y + 1
            p = p + 2*dy - 2*dx
    else:
        p = 2*dx - dy
        if p<0:
            x = x
            y = y + 1
            p = p + 2*dx
        else:
            x = x + 1
            y = y + 1
            p = p + 2*dx - 2*dy

plt.show()