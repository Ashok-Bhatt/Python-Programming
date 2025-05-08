import re

string = "Python Exam is on 27/05/21 and data structure is on 12/06/21, CG on 31/12/21 and C on 03/01/21"
pattern = "[0-3][0-9]/[0-1][0-9]/[0-9][0-9]"

print(re.findall(pattern, string))