import re

string = 'Mani roll no 101 with id mani.butwall@itmbu.ac.in, Sonam roll no 102 with id sonam23@gmail.com, Shuchi roll no 103 with id shuchi234@gmail.com,Divya roll no 104 with id divya.patel@yahoo.com,Shraddha roll no 105 with id shr222@yahoo.co.in,Shuchi roll no 106 with id shuchi2021@rediffmail.in'

pattern1 = '10[0-9]'
pattern2 = '[A-Z][a-z]+'
pattern3 = '[a-zA-Z0-9@.]+.com|[a-zA-Z0-9@.]+.in'

x = re.findall(pattern1, string) # number
y = re.findall(pattern2, string) # name
z = re.findall(pattern3, string) # email

yx = {}
yz = {}
xz = {}
for i,j,k in zip(x,y,z):
    yx.update({j:i})
    yz.update({j:k})
    xz.update({i:k})

print(f"Roll no. are: {x}")
print(f"\nName of candidates are: {y}")
print(f"\nMail ID are: {z}")
print(f"\nDictionary for Roll no. and Name is: {yx}")
print(f"\nDictionary for Roll no. and Mail ID is: {xz}")
print(f"\nDictionary for Name and Mail ID is: {yz}")