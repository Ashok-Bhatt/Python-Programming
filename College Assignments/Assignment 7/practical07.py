import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [4,3,2,1]

plt.plot(x,y,color="red",linewidth=2)
plt.plot(y,x,color="green",linewidth=4)

plt.legend(["line 1","line 2"])
plt.show()