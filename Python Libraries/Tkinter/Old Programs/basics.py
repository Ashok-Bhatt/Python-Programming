from tkinter import *

root = Tk()

root.title("First Tkinter Project")

#WidthxHeight
root.geometry("800x600")
root.minsize(200,75)
root.maxsize(1200,900)

label = Label(text= "Ashok is such a nice person.")
label.pack()

root.mainloop()