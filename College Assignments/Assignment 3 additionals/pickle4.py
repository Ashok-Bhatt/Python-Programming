import pickle
import os

os.chdir("Assignment 3 additionals")

empl_list = []
with open("empl.itm","rb") as filename:
    filename.seek(0)
    employment = pickle.load(filename)
    for i in employment:
        if i["Employment No."]=="1251":
            i["Salary"] = str(int(i["Salary"])+2000)
        empl_list.append(i)
        print(i)

with open("empl.itm","wb") as filename:
    filename.seek(0)
    pickle.dump(empl_list, filename)