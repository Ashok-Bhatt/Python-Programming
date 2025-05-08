import re

string = "Mike likes his new bike"

x = re.findall("ike.*s",string)

if x:
    print("Match found")
else:
    print("Match not found")