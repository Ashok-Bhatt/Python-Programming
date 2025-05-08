import matplotlib.pyplot as plt

y = [20, 95, 90, 60]
x = ["RCB", "MI", "CSK", "GT"]

plt.bar(x,y)

plt.xlabel("IPL Team")
plt.ylabel("Strength")
plt.title("Strength of IPL Teams")
plt.show()