import matplotlib.pyplot as plt
import numpy as np
import math as mt

def plotting(x, color, style):
    xlist = x[:,0]
    ylist = x[:,1]
    plt.plot(xlist, ylist, color=color, linestyle=style)

def translation(x, t):
    y = x + t
    return y

def scaling(x, s):
    y = x*s
    return y

def rotation(x, tita):
    rad = mt.radians(tita)
    y = np.empty((5,2), dtype=int)
    for i in range(len(y)):
        y[i][0] = x[i][0]*mt.cos(rad) - x[i][1]*mt.sin(rad)
        y[i][1] = x[i][0]*mt.sin(rad) + x[i][1]*mt.cos(rad)
    return y

points = np.array([[1,1],[1,5],[5,5],[5,1],[1,1]])
plotting(points, "red", "solid")

translated_points = translation(points, np.array(np.array([2,6])))
plotting(translated_points, "blue", "dashed")

scaled_points = scaling(points, np.array(np.array([2,3])))
plotting(scaled_points, "green", "dashed")

rotated_points = rotation(points, 60)
plotting(rotated_points, "magenta", "dashed")

plt.legend(["Before Transformation", "After Translation", "After Scaling", "After Rotation"])
plt.xlim(-10,20)
plt.ylim(0,30)
plt.show()