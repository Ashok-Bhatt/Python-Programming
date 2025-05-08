import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")

profit = data.total_profit

plt.hist(profit, bins=[x for x in range(150000, 450000, 20000)])
plt.show()

""" 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

total_profit = 'total_profit'

plt.hist(data[total_profit])

plt.xlabel(total_profit)
plt.ylabel('Frequency')
plt.title('Total profit of each month')

plt.show() """