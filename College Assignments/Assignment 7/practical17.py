import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")

months = data.month_number
toothpaste = data.toothpaste

plt.scatter(months, toothpaste, color="black")
plt.show()