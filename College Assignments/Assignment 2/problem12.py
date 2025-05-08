import re

pattern = "[1-z]_[a-z]"
string = "my nam_e is as_hok 1_f."

x = re.findall(pattern, string)
print(x)