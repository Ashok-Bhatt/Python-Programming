import matplotlib.pyplot as plt

x = ["Python", "JavaScript", "C", "C++", "Java"]
y = [95, 85, 75, 80, 90]

plt.bar(x,y,color="y")

plt.grid()
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.show()