import matplotlib.pyplot as plt

x = [1,2]
y = [3,5]
z = [8,1]

plt.plot(x, y, color="red")
plt.plot(y, z, color="green")
plt.plot(z, x, color="blue")

plt.legend(["line1","line2","line3"])
plt.show()