from tkinter import *

def location():
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(f"{width}x{height}")

root = Tk()
root.geometry("800x600")
root.title("Title of GUI")
root.configure(background="#bbb")

Button(text="Close", command=root.destroy).pack(anchor="nw", padx=5, pady=5)
Button(text="Location", command=location).pack(anchor="nw", padx=5, pady=5)

root.mainloop()