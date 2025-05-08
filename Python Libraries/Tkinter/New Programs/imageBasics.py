from tkinter import *
from PIL import Image, ImageTk

# -------------------------For .png files--------------------
root1 = Tk()
root1.geometry("1200x1000")

image1 = PhotoImage(file="New Programs/Geekbit 5.png")
label1 = Label(image=image1)
label1.pack(anchor="nw", padx=50, pady=50)

label2 = Label(text="My Geekbit 5", font="Arial 25 italic")
label2.pack(anchor="nw", padx=50)

root1.mainloop()



# --------------------------For .jpg files--------------------
root2 = Tk()
root2.geometry("1200x1000")

image1 = Image.open("New Programs\sample.jpg")
image1 = image1.resize((200,400))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("New Programs\Geekbit 5.png").resize((200,200))
photo2 = ImageTk.PhotoImage(image2)

label1 = Label(image=photo1)
label1.pack(anchor="nw")

label2 = Label(image=photo2)
label2.pack(anchor="nw")

root2.mainloop()