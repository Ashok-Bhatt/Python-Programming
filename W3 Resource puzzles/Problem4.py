# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

"""
E.g.: 
No. of piles : 4
The each pile will contain 4, 6, 8 and 10 stones:
"""

num_pile=int(input("Enter the number of pile:"))
if num_pile<=0:
    print("The number of pile cannot be zero or negative.")
else:
    i=1
    num_stones=num_pile
    sum_stones=0
    while i<=num_pile:
        print("The number of stones in pile {} is: {}".format(i,num_stones))
        i+=1
        sum_stones+=num_stones
        num_stones+=2
    print("Hence the minimum number of stones possible for given situation is:",sum_stones)