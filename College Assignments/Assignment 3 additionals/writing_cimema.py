import pickle
import os

os.chdir("Assignment 3 additionals")

cinema_list = [{"MNO":"1","MNAME":"Ravi Talkies","MTYPE":"Tragedy"},{"MNO":"2","MNAME":"PVR Cinema","MTYPE":"Sci Fiction"},{"MNO":"3","MNAME":"Mahesh Talkies","MTYPE":"Comedy"},{"MNO":"4","MNAME":"Prakash Studios","MTYPE":"Comedy"}]

with open("CINEMA.DAT","wb") as filename:
        pickle.dump(cinema_list,filename)