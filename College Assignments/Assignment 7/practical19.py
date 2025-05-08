import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")

months = data.month_number
bathingsoap = data.bathingsoap

plt.bar(months , bathingsoap, color="red")

plt.xticks(months)
plt.show()