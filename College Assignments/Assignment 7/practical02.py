import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("company_sales_data.csv")

month = data.month_number
profit = data.total_profit

plt.plot(month, profit, color="red", marker="o", linestyle="dotted", linewidth=3, markerfacecolor="red")

plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.xticks(month)
plt.legend(["Profit per month"], loc="lower right")
plt.show()