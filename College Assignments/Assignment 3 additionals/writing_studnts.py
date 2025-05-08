import pickle
import os

os.chdir("Assignment 3 additionals")

cinema_list = [{"Admission No.":"1","Name":"Ashok Bhatt","CGPA":"8.91"},{"Admission No.":"2","Name":"NArendra Samanta","CGPA":"8.13"},{"Admission No.":"2","Name":"Jainil Patel","CGPA":"8.34"},{"Admission No.":"4","Name":"Priyansh Dabhi","CGPA":"7.13"},{"Admission No.":"5","Name":"Shivam Patel","CGPA":"7.34"}]

with open("STUDENTS.DAT","wb") as filename:
    pickle.dump(cinema_list,filename)