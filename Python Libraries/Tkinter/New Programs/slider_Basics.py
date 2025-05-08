from tkinter import *
import tkinter.messagebox as tmsg

def getDollars():
    tmsg.showinfo("Money Transferred!", f"Your account is credited with {slider1.get()} dollars.")

root = Tk()
root.geometry("500x350")

label1 = Label(root, text="How much money do you want?")
label1.pack(anchor="nw")

slider1 = Scale(root, from_=0, to=100, orient="horizontal", tickinterval=25)
slider1.set(50)
slider1.pack(anchor="nw")

Button(root, text="Get Dollars", command=getDollars).pack(anchor="nw")

root.mainloop()