from tkinter import *

def get_result():
    print(f"{uservalue.get()}, your password is {passvalue.get()}.")

root = Tk()
root.geometry("400x300")

user =  Label(root, text="Username:")
password = Label(root, text="Password:")

user.grid()
password.grid(rows=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=get_result).grid()

root.mainloop()