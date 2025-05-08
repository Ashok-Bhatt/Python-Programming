import matplotlib.pyplot as plt

x = [3,6,9,12]
y=[12,9,6,3]

plt.plot(x,y,color="y",marker = "*")
plt.plot(y,x,color="g",marker = "o")

plt.legend(["line 1","line 2"])
plt.show()