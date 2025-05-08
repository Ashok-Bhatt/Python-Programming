import matplotlib.pyplot as plt

# On entering less number of elements in list, the graph could show floating point values
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]

# Shorthand method: [color][marker][line] e.g., "b*--"
plt.plot(x,y,"b*-",label="y=2x")

plt.title("First Graph in matplotlib", fontdict={"fontname":"serif", "fontsize":"15"})
plt.xlabel("x axis of the graph")
plt.ylabel("y axis of the graph")

# Used to assign the parameters on x and y axis of the graph
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.show()