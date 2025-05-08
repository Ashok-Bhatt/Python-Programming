from tkinter import *

root = Tk()
root.geometry("900x600")
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

Label(root, text="Student Name", foreground="green", background="cyan", height=3, width=40, anchor="se", borderwidth=10, relief=SUNKEN).grid(row=0, column=0, sticky="n")

Label(text="Student Name", foreground="green", background="cyan", height=3, width=40, anchor="se", borderwidth=10, relief=SUNKEN).grid(row=0, column=2, sticky="n")

Label(text="Student Name", foreground="green", background="cyan", height=3, width=40, anchor="se", borderwidth=10, relief=SUNKEN).grid(row=1, column=1)

Label(text="Student Name", foreground="green", background="cyan", height=3, width=40, anchor="se", borderwidth=10, relief=SUNKEN).grid(row=2, column=0, sticky="s")

Label(text="Student Name", foreground="green", background="cyan", height=3, width=40, anchor="se", borderwidth=10, relief=SUNKEN).grid(row=2, column=2, sticky="s")

root.mainloop()