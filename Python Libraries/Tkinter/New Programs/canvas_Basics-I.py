from tkinter import *

root = Tk()
root.geometry("1000x700")

canvas1 = Canvas(root, height = 600, width = 900, background="#000")
canvas1.place(x=25, y=25)

canvas1.create_line(50, 50, 850, 50, fill="#fff")
canvas1.create_line(850, 50, 50, 550, fill="#fff")
canvas1.create_line(50, 550, 850, 550, fill="#fff")
canvas1.create_line(50, 50, 850, 550, fill="#fff")

canvas2 = Canvas(root, height=200, width=300, background="#0f0")
canvas2.place(x=300, y=300)
canvas2.create_rectangle(25, 25, 275, 175, fill="#f0f")

canvas3 = Canvas(root, height=400, width=600, background="#f0f")
canvas3.place(x=100, y=100)
canvas3.create_oval(25, 25, 500, 300, fill="#0f0")

canvas3.create_text(200, 200, text = "Tkinter Text")

root.mainloop()