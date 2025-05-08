from tkinter import *
from mss import mss
from time import sleep
from tkinter import filedialog


def take_screenshot():

    root.wm_state("iconic")

    with mss() as sct:
        files = [('Png file', '*.png')]
        sct.shot(mon=0, output=f"{filedialog.asksaveasfilename(defaultextension='.png', filetypes=files)}")


root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Screenshot Taker")

button = Button(root, text="Take screenshot", command=take_screenshot)
button.pack()

root.mainloop()