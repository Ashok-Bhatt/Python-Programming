import pickle
import os

os.chdir("Assignment 3 additionals")

with open("CINEMA.DAT","rb") as filename:
    filename.seek(0)
    cinema = pickle.load(filename)
    for i in cinema:
        if i["MTYPE"]=="Comedy":
            print("Cinema NO.:",i["MNO"])
            print("Cinema NAME:",i["MNAME"])
            print("Cinema Type:",i["MTYPE"], end="\n\n")