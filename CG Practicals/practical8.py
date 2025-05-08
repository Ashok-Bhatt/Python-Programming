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
    y = x * s
    return y

def rotation(x, tita):
    rad = mt.radians(tita)
    y = np.empty((5,2), dtype=int)
    for i in range(len(y)):
        y[i][0] = x[i][0]*mt.cos(rad) - x[i][1]*mt.sin(rad)
        y[i][1] = x[i][0]*mt.sin(rad) + x[i][1]*mt.cos(rad)
    return y

def composite_transformation(x, transformations):
    y = x.copy()
    for transformation in transformations:
        if transformation[0] == 'translation':
            y = translation(y, transformation[1])
        elif transformation[0] == 'scaling':
            y = scaling(y, transformation[1])
        elif transformation[0] == 'rotation':
            y = rotation(y, transformation[1])
    return y

points = np.array([[1,1],[1,5],[5,5],[5,1],[1,1]])
plotting(points, "red", "solid")

transformations = [
    ('translation', np.array([2, 6])),
    ('scaling', np.array([2, 3])),
    ('rotation', 60)
]

transformed_points = composite_transformation(points, transformations)
plotting(transformed_points, "blue", "dashed")

plt.legend(["Before Transformation", "After Composite Transformation"])
plt.show()