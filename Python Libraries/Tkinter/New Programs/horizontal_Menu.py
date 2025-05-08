from tkinter import *

def func1():
    print("File dabane se kuch naah hoga!")

def func2():
    print("Edit dabane se kuch naah hoga!")

root = Tk()

mainmenu = Menu(root)
mainmenu.add_command(label="File", command=func1)
mainmenu.add_command(label="Edit", command=func2)
root.config(menu=mainmenu)

root.mainloop()