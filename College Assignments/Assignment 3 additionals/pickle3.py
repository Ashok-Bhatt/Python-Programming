import pickle
import os

os.chdir("Assignment 3 additionals")

def countrec():
    filename.seek(0)
    cinema = pickle.load(filename)
    counter = 0
    for i in cinema:
        if float(i["CGPA"])>7.5:
            print("Admission No.:",i["Admission No."])
            print("Name:",i["Name"])
            print("CGPA:",i["CGPA"], end="\n\n")
            counter = counter + 1
    return counter

with open("STUDENTS.DAT","rb") as filename:
    print("No. of students scoring more than 7.5 CGPA:",countrec())