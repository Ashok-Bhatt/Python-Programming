from tkinter import *

root = Tk()

root.geometry("800x400")
Label(root, text="Welcome to Ashok Courrior Services.", font="verdana 20 bold").grid(row=0, column=3)

name = Label(text="Name:")
phone = Label(text="Phone:")
gender = Label(text="Gender:")
emergency = Label(text="Emergency Contact:")
mode = Label(text="Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
mode.grid(row=5, column=2)

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
mode_value = StringVar()



root.mainloop()