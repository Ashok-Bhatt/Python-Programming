from tkinter import *
import os

def store():

    os.chdir("C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Dance Form")
    with open("dance.txt","a") as filename:
        filename.write(namevalue.get() + "\n")
        filename.write(str(agevalue.get()) + "\n")
        filename.write(gendervalue.get() + "\n")

root = Tk()
root.geometry("300x200")

name = Label(text="Name").grid(row=0, column=0, sticky="w")
age = Label(text="Age").grid(row=1, column=0, sticky="w")
gender = Label(text="Gender").grid(row=2, column=0, sticky="w")

namevalue = StringVar()
agevalue = IntVar()
gendervalue = StringVar()

nameEntry = Entry(textvariable= namevalue).grid(row=0, column=1)
ageEntry = Entry(textvariable= agevalue).grid(row=1, column=1)
genderEnter = Entry(textvariable= gendervalue).grid(row=2, column=1)

submit = Button(text="Submit", command=store).grid(row=3, column=0)

root.mainloop()