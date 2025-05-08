from tkinter import *

def hello():
    print("Hello Sir")

root = Tk()
root.geometry("600x400")

frame = Frame(root, borderwidth=5, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw",padx=5)

b1 = Button(frame, foreground="red", text="Click",background="black", command=hello)
b1.pack(side=LEFT,padx=5)

b2 = Button(frame, foreground="red", text="Click",background="black")
b2.pack(side=LEFT,padx=5)

b2 = Button(frame, foreground="red", text="Click",background="black")
b2.pack(side=LEFT,padx=5)

root.mainloop()