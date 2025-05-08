from tkinter import *
from random import choice


def get_random_color():

    color = "#"
    digit_list = [str(i) for i in range(0,10)] + [chr(i+97) for i in range(0,6)]

    for digits in range(0,6):
        color = color + choice(digit_list)
    
    return color


def generate_bands():

    for widgets in root.winfo_children():
        widgets.destroy()
    
    for band in range(0, bands_value.get()):
        color1 = get_random_color()
        color2 = get_random_color()
        Label(root, width=4, background=color1).pack(side=LEFT, anchor="nw", fill=Y)
        Label(root, height=2, background=color2).pack(fill=X)


root = Tk()
root.geometry("900x600+50+50")

bands_value = IntVar()
bands_value.set(5)
bands_label = Label(root, text="Enter no of bands").grid(row=0, column=0, padx=10, pady=10)
bands_entry = Entry(textvariable=bands_value).grid(row=0, column=1, padx=10, pady=10)
generate_button = Button(text="Genrate Bands", command=generate_bands).grid(row=1, column=0, padx=10, pady=10)

root.mainloop()