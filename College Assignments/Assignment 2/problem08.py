import re

string = "1,2 ka 4"

x = re.findall("\d",string)
if x:
    print("Match found")
else:
    print("Match not found")