import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("company_sales_data.csv")

month = data.month_number
toothpaste = data.toothpaste

plt.scatter(month, toothpaste, color="red")

plt.xlabel('Month')
plt.ylabel('Number of Toothpaste Sold')
plt.title('Monthly Toothpaste Sales Data')
plt.xticks(month)
plt.show()