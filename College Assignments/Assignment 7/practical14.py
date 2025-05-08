import matplotlib.pyplot as plt
import random as rd

for i in range(75):
    plt.scatter(rd.randint(1,50), rd.randint(1,50), color="black")

plt.show()