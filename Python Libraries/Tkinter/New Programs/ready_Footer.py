from tkinter import *

root = Tk()
root.geometry("400x300")
root.geometry("+500+200")

label1 = Label(text="Ready!", font=("Bahnschrift Light Condensed", 15, "bold"), background="#6666aa")
label1.pack(fill=X, side="bottom")

root.mainloop()