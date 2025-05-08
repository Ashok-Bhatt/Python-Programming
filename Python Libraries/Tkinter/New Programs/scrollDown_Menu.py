from tkinter import *
import tkinter.messagebox as tmsg

def func_new():
    tmsg.showinfo("User","New File Created")    # return value will be ok

def func_save():
    x = tmsg.askquestion("Save","Do you want to save this file?")
    if x=="yes":
        msg = "File Saved!"
    else:
        msg = "File not Saved!"
    tmsg.showinfo("User",msg)

def func_undo():
    x = tmsg.askretrycancel("Bunana hai Candidate Master", "Sorry nahi bann sakte CodeForces mai Candidate Master.")
    if x:
        print("Retry mat kar Pith jayega")
    else:
        print("Sahi kia tere bass ki nahi hai competative programming. Tu gfg leetcode hie kar le.")

def func_redo():
    x = tmsg.askyesnocancel("Hey user!","Do you want to share your experience?")
    print(x)
    if x==True:     # True
        print("Wow!")
    elif x==False:  # False
        print("Not Sharing")
    else:           # None
        print("No comments")

def func_cut():
    tmsg.showwarning("Warning","Isse Accha copy paste kar aur phir isse hatta.")

root = Tk()
root.geometry("600x400")
mainmenu = Menu(root)

file = Menu(mainmenu, tearoff=False)
file.add_command(label="New File", command=func_new)
file.add_command(label="Save", command=func_save)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=file)

edit = Menu(mainmenu)
edit.add_command(label="Undo", command=func_undo)
edit.add_command(label="Redo", command=func_redo)
edit.add_separator()
edit.add_command(label="Cut", command=func_cut)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=edit)

root.mainloop()