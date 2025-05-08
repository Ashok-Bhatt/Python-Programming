from functools import *
list1 = [2,3,4,5,6,7,8,9,12]
minimum = reduce(lambda x,y: x if x<y else y, list1)
print(minimum)
maximum = reduce(lambda x,y: x if x>y else y, list1)
print(maximum)