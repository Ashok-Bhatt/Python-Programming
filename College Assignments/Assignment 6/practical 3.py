import pandas as pd

dict1 = {'name': ['Vinay', 'Kushal', 'Aman'], 'age' : [22, 25, 24], 'occ' : ['engineer', 'doctor', 'accountant']}
dataframe1 = pd.DataFrame(dict1, index=[1,2,3])
print(dataframe1)