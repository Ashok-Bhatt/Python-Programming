import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")

months = data.month_number
facecream = data.facecream
facewash = data.facewash
toothpaste = data.toothpaste
bathingsoap = data.bathingsoap
shampoo = data.shampoo
moisturizer = data.moisturizer

plt.plot(months, facecream, color="red")
plt.plot(months, facewash, color="blue")
plt.plot(months, toothpaste, color="yellow")
plt.plot(months, bathingsoap, color="green")
plt.plot(months, shampoo, color="orange")
plt.plot(months, moisturizer, color="pink")

plt.legend(["Face Cream","Facing Wash","Toothpaste","Bathing Soap","Shampoo","Moisturizer"])
plt.show()