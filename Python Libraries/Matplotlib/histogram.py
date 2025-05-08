import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv("fifa data.csv")
fifa.head(5)

bins = [10*x for x in range(1,11)]
plt.hist(fifa.Overall, bins=bins, color="#333333")

plt.xlabel("Skill Level")
plt.ylabel("Number of players")
plt.title("Distribution of Player Skills in FIFA 2018")

plt.xticks(bins)

plt.show()