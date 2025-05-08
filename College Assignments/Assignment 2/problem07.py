import re

string = "Toss the glass, boss"

x = re.findall("\Bss",string)
if x:
    print("Match found")
else:
    print("Match not found")