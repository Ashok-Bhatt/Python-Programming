from tkinter import *

content = "Ashok Bhatt \n"*1000

root = Tk()
root.geometry("1000x600")

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text1 = Text(root, yscrollcommand=scroll.set)
text1.pack(fill=BOTH)

scroll.config(command=text1.yview)
text1.insert(END, content)

root.mainloop()