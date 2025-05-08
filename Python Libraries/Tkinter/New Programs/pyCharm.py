from tkinter import *

root = Tk()

Title = Label(text="PyCharm", font="arial 20 bold", background="#ccc")
Title.pack(fill=X)

Line1 = Label(text="Create Name Project", font="serif 14", background="#9999ff", borderwidth=1)
Line1.pack(fill=X)

Line2 = Label(text="Open", font="serif 14", background="#9999ff", borderwidth=1)
Line2.pack(fill=X)

Line3 = Label(text="Check out your version control", font="serif 14", background="#9999ff", borderwidth=1)
Line3.pack(fill=X)

root.mainloop()