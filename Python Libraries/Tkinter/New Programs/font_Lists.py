from tkinter import *
from tkinter import font as Tkfont

root = Tk()
root.geometry("800x600")
font_list = sorted(list(Tkfont.families()))

Scrollbar1 = Scrollbar(root)
Scrollbar1.pack(side=RIGHT, fill=Y)

textbox1 = Text(root, yscrollcommand=Scrollbar1.set)
textbox1.pack(anchor="w", fill="both")

for element in font_list:
    font1 = Tkfont.Font(family=element, size=15, weight="bold")
    textbox1.tag_configure(element, font=font1)
    textbox1.insert(INSERT, element, element)
    textbox1.insert(INSERT, "\n\n")

Scrollbar1.config(command=textbox1.yview)

root.mainloop()