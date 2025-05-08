import re

string = "https://www.google.com/news/football-insider/wp/2021/03/05/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

pattern = "20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]"

x = re.findall(pattern, string)
print(x)