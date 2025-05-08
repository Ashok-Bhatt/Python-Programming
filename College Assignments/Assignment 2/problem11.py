import re

string = "a ab abb abbb"
pattern = "ab{2,3}"
x = re.search(pattern, string)

if (x):
    print("Match found")
else:
    print("Match not found")