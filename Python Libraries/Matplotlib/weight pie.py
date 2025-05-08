import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa data.csv")

fifa.Weight = [int(x.strip("lbs")) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa.loc[fifa.Weight >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ["light", "light_medium", "medium", "medium_heavy", "heavy"]
explode = [.3,.3,0,0,.3]

plt.title("Weight Distribution of FIFA Players (in lbs)")
plt.style.use("ggplot")
plt.pie(weights, labels=labels, autopct="%.2f", pctdistance=.9, explode=explode)

plt.show()