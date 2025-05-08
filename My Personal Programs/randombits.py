import random;

string = ""
for i in range(15):
    string = string + str(random.choice([0,1]))

print(string)