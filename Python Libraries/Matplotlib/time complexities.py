import matplotlib.pyplot as plt
from math import log2

data = [i for i in range(1,101)]
data_logarithmic = [log2(i) for i in range(1,101)]
data_quasilinear = [i*log2(i) for i in range(1,101)]

plt.plot(data, data, label="linear")
plt.plot(data, data_logarithmic, label="logarithmic")
plt.plot(data, data_quasilinear, label="quasilinear")

plt.xticks([10*i for i in range(0,11)])

plt.legend()
plt.show()