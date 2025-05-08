import matplotlib.pyplot as plt
import numpy as np

# On entering less number of elements in list, the graph could show floating point values
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]

# To resize the graph
# Should be kept before using plot function, else it will generate another plot
plt.figure(figsize=(6,4), dpi=150)

# To see the label component, it is mandatory to use legend() function
# color name can be specified in hexadecimal value or using key name, but cannot be specifies in rgb format
# All possible values for linestyle attribute: '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(x, y, label="y=2x", color="#2222ff", linestyle="dashed", linewidth=2, marker=".", markersize=5, markeredgecolor="black")

num = np.arange(0,3,0.25)
plt.plot(num, num**2, "g.--", label="y=x^2")

plt.title("First Graph in matplotlib", fontdict={"fontname":"serif", "fontsize":"15"})
plt.xlabel("x axis of the graph")
plt.ylabel("y axis of the graph")

# Used to assign the scales on x and y axis of the graph
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])

plt.legend()

# To save the the plot
# plt.savefig("SamplePlot.png", dpi=150)

plt.show()