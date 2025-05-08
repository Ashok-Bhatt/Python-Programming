import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("company_sales_data.csv")

month = data.month_number
profit = data.total_profit

plt.plot(month, profit, color="red")

plt.xlabel('Month')
plt.ylabel('Number of Units Sold')
plt.title('Monthly Sales Data')
plt.xticks(month)
plt.show()