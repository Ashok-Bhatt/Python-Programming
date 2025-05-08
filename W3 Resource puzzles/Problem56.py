# Write a Python program to find an integer exponent x such that a^x = n

base=int(input("Enter the base:"))
num=int(input("Enter the number obtained on calculating a^b:"))

import math
power=math.log(num)/math.log(base)
print("The value of power is:",power)