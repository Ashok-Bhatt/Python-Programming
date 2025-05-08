from tkinter import *

height = 500
width = 800

root = Tk()
root.geometry(f"{width}x{height}")

canvas1 = Canvas(height=height, width=width)
canvas1.pack()

canvas1.create_arc(100, 100, 200, 50, extent=90, fill="red")
canvas1.create_polygon(100,100, 150,100, 200,150, 200,200, 150,250, 100,250, 50,200, 50,150)

root.mainloop()