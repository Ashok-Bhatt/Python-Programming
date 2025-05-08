from tkinter import *

root = Tk()
root.geometry("800x600")

frame1 = Frame(root, bg="yellow", borderwidth=5, relief=SUNKEN)
frame1.pack(side=LEFT, fill="y")

label1 = Label(frame1, text="My Project-Text Editor", bg="green", padx=20,pady=20)
label1.pack(padx=10,pady=50)

frame2 = Frame(root, bg="red", borderwidth=5, relief=SUNKEN)
frame2.pack(side=TOP, fill="x")

label2 = Label(frame2, text="Title Bar of Text Editor", bg="grey", padx=5,pady=5, fg="white", font="serif 10 bold")
label2.pack()

root.mainloop()