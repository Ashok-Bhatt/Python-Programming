import re

str_1 = "My Name is Lakhan"
str_2 = "Name is Lakhan"

x = re.findall("^My",str_1)
y = re.findall("^My",str_2)

if x:
    print("Match Found")
else:
    print("Match Not Found")

if y:
    print("Match Found")
else:
    print("Match Not Found")