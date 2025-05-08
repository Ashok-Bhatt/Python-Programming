import re

string1 = "Mike likes his new bike"
string2 = "Mike dislikes his new bike"

x = re.findall("likes | dislikes",string1)
y = re.findall("likes | dislikes",string2)

if x:
    print("Match found")
else:
    print("Match not found")
if y:
    print("Match found")
else:
    print("Match not found")