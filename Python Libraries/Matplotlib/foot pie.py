import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa data.csv")

left = fifa.loc[fifa["Preferred Foot"] == "Left"].count()[0]
right = fifa.loc[fifa["Preferred Foot"] == "Right"].count()[0]

labels = ["left","right"]
colors = ["green", "red"]

plt.pie([left,right], labels=labels, colors=colors, autopct="%.1f %%")

plt.title("Foot prefrences of players")

plt.show()