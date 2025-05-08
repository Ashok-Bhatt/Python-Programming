from tkinter import *

def changeWindowSize():
    root.geometry(f"{x_value.get()}x{y_value.get()}")

root = Tk()
root.geometry("300x200")

x_coord = Label(text="Enter width: ").grid(row=0, column=0, sticky="w")
y_coord = Label(text="Enter height: ").grid(row=1, column=0, sticky="w")

x_value = IntVar()
y_value = IntVar()

x_entry = Entry(textvariable = x_value).grid(row=0, column=1)
y_entry = Entry(textvariable = y_value).grid(row=1, column=1)

button1 = Button(text="Change", command=changeWindowSize).grid(row=2, column=0, sticky="w")

root.mainloop()