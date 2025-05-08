import re

string = "ash ketchum vs ashok bhatt"
print("String:",string)

# NOTE: match method scans obly from the beginning of the string
# direct letters
pattern1 = "ash"
print("Result 1:",re.match(pattern1,string))

# square brackets ------> Each square bracket denotes the singlr bracket
pattern2 = "[a-z]sh "
print("Result 2:",re.match(pattern2,string))

pattern3 = "[ash][ash]"
print("Result 3:",re.match(pattern3,string))

# search method:
pattern4 = "ashok"
print("Result 4:",re.search(pattern4,string))

# findall method:
pattern5 = "[ash]"
print("Result 5:",re.findall(pattern5,string))

pattern6 = "ash"
print("Result 6:",re.findall(pattern6,string))

# split method:
pattern7 = "ash"
print("Result 7:",re.split(pattern7,string))

# sub method:
