from tkinter import *
import time

def upload():
    statusvar.set("Busy..")
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready Now")

root = Tk()
root.geometry("450x300")
root.title("Status Bar")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w", padx=10)
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack() 

root.mainloop()