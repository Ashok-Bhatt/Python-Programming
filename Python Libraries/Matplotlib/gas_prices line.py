import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv("gas_prices.csv")
print(gas)

plt.figure(figsize=(10,6))
plt.title("Gas prices (over years) in USD")
plt.xlabel("Prices in USD")
plt.ylabel("Countries")

# To maually plot each country's price vs year plot
# plt.plot(gas.Year, gas.USA, "r.-", label="USA")
# plt.plot(gas.Year, gas.Canada, "b.-", label="Canada")
# plt.plot(gas["Year"], gas["France"], "g.-", label="France")

for country in gas:
    if country != "Year":
        plt.plot(gas.Year, gas[country], marker=".", label=country)

plt.xticks(gas.Year[::2].tolist()+[2010,2012,2014])

plt.legend()
plt.show()