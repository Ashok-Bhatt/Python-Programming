from tkinter import *
from prettytable import PrettyTable

def printData():
    name = userEntry.get()
    password = passEntry.get()

    myTable = PrettyTable(["Name","Password"])
    myTable.add_row([name,password])
    print(myTable)
    
root = Tk()
root.geometry("300x200")

user = Label(text="Name")
password = Label(text="Password")

user.grid(row=0, column=0, sticky="w", padx=10)
password.grid(row=1, column=0, sticky="w", padx=10)

uservalue = StringVar()
passvalue = StringVar()

userEntry = Entry(textvariable=uservalue)
passEntry = Entry(textvariable=passvalue)

userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

submit = Button(text="Submit", command=printData).grid(row=2)

root.mainloop()