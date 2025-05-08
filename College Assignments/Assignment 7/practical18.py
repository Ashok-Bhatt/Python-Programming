import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")

months = data.month_number
facecream = data.facecream
facewash = data.facewash

plt.bar(months -0.2, facecream, 0.4, color="red")
plt.bar(months +0.2, facewash, 0.4, color="blue")

plt.xticks(months)
plt.legend(["Face Cream","Face Wash"])
plt.show()