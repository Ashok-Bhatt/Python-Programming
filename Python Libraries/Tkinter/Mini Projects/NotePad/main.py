from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter.messagebox as tmsg
import os

file = None

def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0,END)

def open_file():

    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files","*.*"),("Text Document","*.txt")])

    if file=="":
        file = None
    else:
        root.title(os.path.basename(file))
        textarea.delete(1.0, END)
        with open(file,"r") as filename:
            textarea.insert(1.0, filename.read())

def save_file():
    
    global file
    file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All files","*.*"),("Text Document","*.txt")])
    if file == "":
        file = None
    else:
        with open(file,"w") as filename:
            filename.write(textarea.get(1.0,END))
        root.title(os.path.basename(file))

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Hello User", "This notepad Application is created by Ashok Bhatt")

root = Tk()
root.geometry("1000x600+100+50")
root.title("Untitled - Notepad")
root.iconbitmap("notepad.ico")

# --------------------- Header Section of NotePad -------------------------
header = Menu(root, background="#333")

file = Menu(header, tearoff=FALSE)
file.add_command(label="New", command=new_file)
file.add_command(label="Open", command=open_file)
file.add_command(label="Save", command=save_file)
file.add_command(label="Exit", command=quit)
header.add_cascade(label="File", menu=file)

edit = Menu(header, tearoff=FALSE)
edit.add_command(label="Cut", command=cut)
edit.add_command(label="Copy", command=copy)
edit.add_command(label="Paste", command=paste)
header.add_cascade(label="Edit", menu=edit)

help = Menu(header, tearoff=FALSE)
help.add_command(label="About", command=about)
header.add_cascade(label="Help", menu=help)

root.config(menu=header)
# ----------------------- Header Section of NotePad Ends Here --------------------------

# ----------------------- Creating the text area of Notepad ----------------------------

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

textarea = Text(root, yscrollcommand=scroll.set, font=("lucida", 15, "bold"))
textarea.pack(fill=BOTH, expand=TRUE)

scroll.config(command=textarea.yview)
# ----------------------- Text Area part ends here -------------------------------------

root.mainloop()