import re

string = "sea shells sea shells on the sea shore"
print("String:",string)

# Special sequence
pattern1 = "\s"
print("Result1:", len(re.findall(pattern1,string)))

# Any characters
pattern2 = "..e.."
print("Result2:", re.findall(pattern2,string))

# Starts with and ends with or 0/0+ occurances
pattern3 = "^sea"
print("Result3:", re.findall(pattern3,string))

pattern4 = "e$"
print("Result4:", re.findall(pattern4,string))

pattern5 = "se*"
print("Result5:", re.findall(pattern5,string))

pattern6 = "..e.."
print("Result6:", re.findall(pattern6,string))

# Big Brackets:
string1 = "my name is Ashok Bhatt, currently pursuing B.Tech CSE and my mobile number is 9998523878."
print("\nNew String:",string1)

# NOTE: "*" denotes 0/0+ occurances
#       "+" denotes 1/1+ occurances
#       "?" denotes 0/1 occurances

pattern7 = "[0-9]"
print("Result7:", re.findall(pattern7,string1))

pattern8 = "[^0-9a-zA-z ]"
print("Result8:", re.findall(pattern8,string1))

pattern9 = "[0-9]+"
print("Result9:", re.findall(pattern9,string1))

pattern10 = "[0-9]+"
print("Result9:", re.findall(pattern9,string1))