import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa data.csv")

madrid = fifa.loc[fifa.Club == "Real Madrid"]["Overall"]
england = fifa.loc[fifa.Club == "New England Revolution"]["Overall"]

labels = ["Real Madrid","New England Revolution"]

plt.title("Professional Soccer Team Comparison")
plt.style.use("ggplot")

boxes = plt.boxplot([madrid,england], labels=labels, patch_artist = True)

for box in boxes["boxes"]:
    box.set(color= "#0000FF", linewidth =2)     # edge color
    box.set(facecolor = "#00FFFF")

plt.show()