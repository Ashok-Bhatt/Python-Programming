import re

string = "abbbreviation"

x = re.findall("abbb",string)
if x:
    print("Match found")
else:
    print("Match not found")