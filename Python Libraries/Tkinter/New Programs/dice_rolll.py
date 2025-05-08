from tkinter import *
from random import randint

def animation():

    dice_face = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685",]
    die1 = randint(0,5)
    die2 = randint(0,5)

    label1.configure(text = f"{dice_face[die1]} {dice_face[die2]}")
    label1.update()
    return [die1,die2]

def roll():
    label2.configure(text="")
    for i in range(10):
        ans = animation()
        root.after(100)
    label2.configure(text = f"Sum on dice: {ans[0]+ans[1] + 2}")
    
root = Tk()
root.geometry("800x600")
root.title("Dice Roll Program")
root.config(bg="white")

button1 = Button(text="Roll the dice!", height=5, width=30, font=10, command=roll).pack(padx=10, pady=10)
label1 = Label(text="", font=("lucida",100), bg="#fa0", height=1, width=3)
label1.pack(padx=20, pady=10, side=LEFT, anchor="nw")
label2 = Label(text="", font=("lucida",25), bg="#fa0", padx=20, pady=5, height=1, width=15)
label2.pack(padx=20, pady=10, side=LEFT, anchor="nw")
root.mainloop()