from tkinter import *
from PIL import Image,ImageTk
import os

os.chdir("Image Showdown")
image_list = os.listdir(os.getcwd())

def destroy_window(root, index):
    root.destroy()
    if (index < len(image_list)-1):
        show_image(index+1)

def show_image(index):
    root = Tk()
    root.geometry("500x400")
    root.geometry("+500+200")
    root.title(f"Geekbit{index+5}")

    image1 = Image.open(image_list[index]).resize((300,240))
    photo1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=photo1)
    label1.pack()

    label2 = Label(text=f"This is your hardely earned Geebit {index+5}.", font="sansserif 20 italic", foreground="#77ff77")
    label2.pack()

    root.after(2000, lambda: destroy_window(root, index))
    root.mainloop()

show_image(0)