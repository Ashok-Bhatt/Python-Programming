from tkinter import *
from PIL import Image,ImageTk
import os
from datetime import date

os.chdir("C:/Users/Ashok Bhatt/Desktop/Python Programming Work/Python Libraries/Tkinter/New Programs/NewsPaper Task/Photos")

imageToText = {}
for image in os.listdir(os.getcwd()):

    text = ""
    path = os.getcwd()[:-6] + "Info/" + image[:-3] + "txt"

    with open(path) as filename:
        for line in filename:
            text = text + line.replace("\n","\t\t")
    imageToText[image] = text

root = Tk()
root.geometry("1400x600")
root.geometry("+50+50")
root.title("Breaking News - Ashok Bhatt's Coding Profile")

header = Label(text="Ashok  News  Express", font="Georgia 25 bold italic underline", background="#ddd")
header.pack(fill=X)

intro = Label(text=f"Date: {date.today()}", background="#ddd")
intro.pack(anchor="ne")

for element in imageToText.keys():

    photo1 = Image.open(element).resize((200,140))
    image1 = ImageTk.PhotoImage(photo1)
    label1 = Label(image = image1, background="#ddd")
    label1.photo = image1
    label1.pack(fill=X)

    label2 = Label(text = imageToText[element], background="#ddd")
    label2.pack(fill=X)

root.mainloop()