from tkinter import *

root = Tk()

root.title("My GUI with Ashok")
root.geometry("1024x768")
root.minsize(900,600)

label = Label(text="Michaell Faraday invented the electric generator.\nHe has invented a lot of other thing too.", bg="black", fg="red",
              padx=20,pady=10,font="serif 25 bold", border=10, relief=SUNKEN)

#label.pack(side="left", anchor="nw", fill=X, padx=20, pady=20)
label.pack(side="top", fill=X, padx=20, pady=20)

root.mainloop()