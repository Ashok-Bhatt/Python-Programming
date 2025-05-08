list1 = [x for x in range(35,56)]
y = list(filter(lambda x: x%5 == 0,list1 ))
print(y)