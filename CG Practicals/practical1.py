import matplotlib.pyplot as plt
from math import ceil

x1,y1 = map(int, input("Enter x1,y1 separated by space:").split())
x2,y2 = map(int, input("Enter x2,y2 separated by space:").split())

dx = x2-x1
dy = y2-y1
x = x1
y = y1

if abs(dx)>abs(dy):
    step = abs(dx)
else:
    step = abs(dy)

while (x,y)<=(x2,y2):
    plt.scatter(ceil(x),ceil(y))
    x = x + dx/step
    y = y + dy/step

plt.show()