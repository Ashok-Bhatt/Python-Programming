from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("400x300")
root.minsize(200,150)
image = Image.open("C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\sample.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()