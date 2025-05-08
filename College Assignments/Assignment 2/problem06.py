import re

str_6 = "Mike likes his new bike"

x = re.findall("ike$",str_6)

if x:
    print("Match found")
else:
    print("Match not found")