from tkinter import *

is_dark = False

def change_mode():
    global is_dark
    if is_dark:
        button1.configure(image=light_mode)
        root.configure(bg="white")
    else:
        button1.configure(image=dark_mode)
        root.configure(bg="black")
    is_dark = not(is_dark)

root = Tk()
root.geometry("350x500")
root.title("Dark vs Light Mode")
root.resizable
root.configure(bg="white")

light_mode = PhotoImage(file="C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Appearance Mode\\Images\\light.png")
dark_mode = PhotoImage(file="C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Appearance Mode\\Images\\dark.png")

button1 = Button(image=light_mode, command=change_mode)
button1.pack(side = TOP, pady=20)

root.mainloop()