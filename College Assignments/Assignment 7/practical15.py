import matplotlib.pyplot as plt

pp = [22, 25, 22, 12, 25, 27, 28, 25, 21, 25]
dsa = [28, 18, 18, 22, 24, 29, 28, 25, 16, 29]

plt.scatter([x for x in range(10)], pp, color='r')
plt.scatter([x for x in range(10)], dsa, color = 'g')

plt.legend(["PP-II","DSA-I"])
plt.xticks([x for x in range(10)])
plt.yticks([x for x in range(0,31,3)])
plt.show()