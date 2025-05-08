from tkinter import *

root = Tk()
root.geometry("600x600")

frame1 = Frame(root, background="#7777ff", borderwidth=10)
frame1.pack(anchor="nw", side="left", fill=Y)

label1 = Label(frame1, text="Frame show off!", borderwidth=2, relief=SUNKEN)
label1.pack()

root.mainloop()