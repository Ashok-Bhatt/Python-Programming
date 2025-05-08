from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Placed!", f"We have received your order for {var.get()}.")

dishes = ["Dosa","Samosa","Kachori","Paratha"]

root = Tk()
root.geometry("800x600")

var = StringVar()
var.set("None")

Label(root, text="What do you want to eat? Plaese select your order", font="lucida 19 bold", justify=LEFT, padx=10).pack()

for i in range(4):
    radio = Radiobutton(root, text=dishes[i], padx=5, variable=var, value=dishes[i]).pack(anchor="w")

Button(text="Order Now", padx=5, pady=5, command=order).pack(anchor="w")

root.mainloop()