import re

string = "xabcy"

x = re.findall("x.*?y$",string)
if x:
    print("Match found")
else:
    print("Match not found")