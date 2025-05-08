import pickle
import os

os.chdir("Assignment 3 additionals")

employment = [{"Employment No.":"1250","Name":"Ashok Bhatt","Salary":"30000"},{"Employment No.":"1251","Name":"Shivam Patel","Salary":"29000"},{"Employment No.":"1252","Name":"Jainil Patel","Salary":"35000"},{"Employment No.":"1253","Name":"Priyansh Dabhi","Salary":"32000"},{"Employment No.":"1254","Name":"Narendra Samanta","Salary":"26500"}]

with open("empl.itm","wb") as filename:
    pickle.dump(employment,filename)