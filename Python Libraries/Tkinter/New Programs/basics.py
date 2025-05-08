from tkinter import *

root = Tk()

root.geometry("500x400")
root.minsize(125,100)
root.maxsize(1000,800)

x1 = Label(text = "First Label")
x2 = Label(text = "Second Label")
x2.pack()
x1.pack()
root.mainloop()