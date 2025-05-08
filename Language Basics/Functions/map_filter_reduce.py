num_list=[1,2,3,4,5,6,7,8,9]

even_list=list(filter(lambda x:x%2==0,num_list))
print("The filtered list is given by:",even_list)

double_list=list(map(lambda x:x*2,num_list))
print("The mapped list is given by:",double_list)

import functools
reduced_number=list(functools.reduce(lambda x,y:x+y,num_list))