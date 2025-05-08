import re

string = "Shika scored 345 marks,Sonam scored 320 marks,Shuchi scored 315 marks,Divya scored 335 marks,Shraddha scored 350 marks,Shuchi scored 323 marks"

scorePattern1 = "[0-9]+"
scorePattern2 = "[A-Za-z]+ scored"

x = re.findall(scorePattern1, string)
print(x)

y = re.findall(scorePattern2, string)
for i in range(len(y)):
    y[i] = y[i][:-7]
print(y)

dict = {}
for i,j in zip(x,y):
    dict.update({i:j})
print(dict)