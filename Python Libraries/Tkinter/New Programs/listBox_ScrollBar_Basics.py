from tkinter import *

def add():
    global i
    list1.insert(ACTIVE, f"Element {i}")
    i = i + 1

i = 1
root = Tk()
root.geometry("500x400")

scroll = Scrollbar()
scroll.pack(side=RIGHT, fill=Y)

list1 = Listbox(root, yscrollcommand=scroll.set)
list1.pack(anchor="w", fill="both")
list1.insert(END,"Element 0")

scroll.config(command=list1.yview)
Button(text="ADD", command=add).pack(anchor="w")

root.mainloop()