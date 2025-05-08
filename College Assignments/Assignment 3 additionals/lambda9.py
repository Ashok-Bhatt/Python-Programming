list1 = [34,5,7,8,21,12,13,33,43,41,55,56,90,87,43,2]
y = list(map(lambda y: y ** 2,filter(lambda x:x%2,list1 )))
print(y)