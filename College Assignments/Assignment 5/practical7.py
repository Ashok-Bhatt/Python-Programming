import pandas as pd

day = ["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7","Day 8","Day 9","Day 10"]
total_customers = [24,45,12,34,17,23,20,30,32,48]
total_bill = [30000, 60000, 20000, 30000, 30000, 20000, 25000, 40000, 35000, 70000]
total_tip = [1500, 3000, 1800, 1500, 2000, 1000, 2300, 5000, 3000, 1200]

dict1 = {"Customers":total_customers, "Bill":total_bill, "Tip":total_tip}
dataframe1 = pd.DataFrame(dict1, index=day)
print("Given DataFrame:")
print(dataframe1)

print("\nTop 3 data entries:")
print(dataframe1.head(3))
print("\nBottom 2 data entries:")
print(dataframe1.tail(2))

print("\nInformation about columns:")
print(dataframe1.info())

print("\nWithout describe function:")
print("        Customers      Bill           Tip")
print(f"Min     {min(total_customers):<15}{min(total_bill):<15}{min(total_tip)}")
print(f"Max     {max(total_customers):<15}{max(total_bill):<15}{max(total_tip)}")
print(f"Count   {len(total_customers):<15}{len(total_bill):<15}{len(total_tip)}")

print("\nWith describe function:")
print(dataframe1.describe())