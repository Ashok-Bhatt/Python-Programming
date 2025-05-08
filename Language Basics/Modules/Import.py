from math import factorial
print(factorial(3))

import random as rand
animal=["Elephant","Giraffe","Rhinoceros","Hippopatamous","Deer"]
print(f"{rand.choice(animal)} is a herbivores animal.")
print(f"{animal[rand.randint(0,4)]} is also a herbivores animal.")

from math import fabs as abs
print("The absolute value of -4 is:",abs(-4))

# To import every function from math module: from math import *
import math
print("The hcf of 12 and 8 is:",math.gcd(12,8))

print(dir(math))
print(math.nan,type(math.nan))

import Mathematics
print("Quadratic Equation:4x^2-4x+1")
Mathematics.poly_sqrt(4,-4,1)