import re

string = "Toss the glass,boss"
pattern = re.findall("os.*s",string)

if pattern:
    print("Match found")
else:
    print("Match not found")