import re

pattern = "[0-9]+"
string = "The best board game ever is 2048. In this game, we need to match the numbers and double them until you get 2048 block. However you can create the number till 65536."

x = re.findall(pattern, string)
print(x)