import numpy as np
import pandas as pd

name = pd.Series(['Anjali', 'Divya', 'Dhruv', 'John', 'Rishi', 'Saumil', 'Manan', 'Dhara', 'Kevin', 'Rahul'])
score = pd.Series([12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19])
attempts = pd.Series([1, 3, 2, 3, 2, 3, 1, 1, 2, 1])
qualify = pd.Series(['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'])
labels =  pd.Series(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

df = pd.DataFrame({"Name":name,"Score":score,"Attempts":attempts,"Qualify":qualify,"Labels":labels})
print("Required dataframe:")
print(df)

print("\nQuestion 1:")
print(df.head(3))

print("\nQuestion 2:")
print(df.iloc[:,0:2])

print("\nQuestion 3:")
print(df.iloc[[0,2,4,5],0:2])

print("\nQuestion 4:")
print(df[df["Attempts"]>2])

print("\nQuestion 5:")
print(df[df["Score"].isna()])

print("\nQuestion 6:")
print(df[(df["Attempts"]<2) & (df["Score"]>15)])

print("\nQuestion 7:")
df.loc[df["Labels"]=="d","Score"] = 11.5
print(df[df["Labels"]=="d"])

print("\nQuestion 8:")
print(df.Attempts.sum())

print("\nQuestion 9:")
print(df.Score.mean())

print("\nQuestion 10:")
print("After adding the new row:")
df.loc[len(df)] = ["Suresh", 15.5, 1, "yes", "k"]
print(df)
print("After removing the new row:")
df.drop(df[df.Name == "Suresh"].index, inplace=True)
print(df)

print("\nQuestion 11:")
print("Sorting dataframe by name in descending order:")
df1 = df.sort_values(by=["Name"], ascending=False)
print(df1)
print("Sorting dataframe by score in ascending order:")
df2 = df.sort_values(by=["Score"])
print(df2)

print("\nQuestion 12:")
df = df.replace(["yes", "no"], ["True", "False"])
print(df)

print("\nQuestion 13:")
df[df.Name == "Dhara"] = "Liza"
print(df)

print("\nQuestion 14:")
del df["Attempts"]
print(df)

print("\nQuestion 15:")
print("Addition of Score and Attempts:")
print(score.add(other = attempts))
print("Multiplication of Score and Attempts:")
print(score.multiply(other = attempts))
print("Subtraction of Score and Attempts:")
print(score.subtract(other = attempts))
print("Division of Score and Attempts:")
print(score.divide(other = attempts))