import matplotlib.pyplot as plt
import numpy as np

num = np.arange(0,5,0.2)
plt.plot(num[:10],num[:10]**2,"b*--",label="y=x^2")
plt.plot(num[9:],num[9:]**2,"r",label="y=x^2")

plt.title("First Graph in matplotlib", fontdict={"fontname":"serif", "fontsize":"15"})
plt.xlabel("x axis of the graph")
plt.ylabel("y axis of the graph")

# Used to assign the parameters on x and y axis of the graph
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.show()