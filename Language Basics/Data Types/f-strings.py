# String Formatting:
me = "ashok"
txt="this is %s"%me
print(txt)
a = "my name is {} {}."
b="Bhatt"
c = a.format(me,b)
print(c)

# F-String (started in python 3.6):
# More convenient than string formatting.

import math
str = f"{me} finds the value of cos 90 to be {math.cos(3.14)}"
print(str)

# String formatting with some specific decimal points:
# This method follows the rules of decimal round off
price1=34
price2=34.23546
print(f"The price of x is {price1:.1f} and of y is {price2:.2f}")