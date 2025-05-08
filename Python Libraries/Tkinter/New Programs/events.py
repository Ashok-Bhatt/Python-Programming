def location(event):
    print(f"You clicked the button at X={event.x} and Y={event.y}")

from tkinter import *

root = Tk()
root.title("Events in Tkinter")
root.geometry("800x500")

button1 = Button(root, text="Click")
button1.pack()

button1.bind("<Button-1>", location)
button1.bind("<Double-1>", quit)

root.mainloop()