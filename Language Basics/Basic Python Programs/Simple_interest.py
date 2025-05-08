principle=float(input("Enter the principle amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the no. of years:"))

interest=(principle*rate*time)/100
print("The simple interest is:",interest)
print("The final amount is:",interest+principle)