from tkinter import *

def close():
    root.destroy()

def maximize():
    root.attributes("-fullscreen", True)
    root.geometry("+0+0")

def minimize():
    root.geometry("1200x50")

root = Tk()
root.geometry("1200x700")
root.geometry("+25+25")
root.title("Visual Studios")

# -------------------------------------- Title Bar ---------------------------------------
title_bar = Frame(root, background="#ddd")
title_bar.pack(fill=X)

file = Label(title_bar, text="File", background="#ddd")
file.pack(padx=10, pady=3, side="left")

edit = Label(title_bar, text="Edit", background="#ddd")
edit.pack(padx=10, pady=3, side="left")

selection = Label(title_bar, text="Selection", background="#ddd")
selection.pack(padx=10, pady=3, side="left")

view = Label(title_bar, text="View", background="#ddd")
view.pack(padx=10, pady=3, side="left")

go = Label(title_bar, text="Go", background="#ddd")
go.pack(padx=10, pady=3, side="left")

run = Label(title_bar, text="Run", background="#ddd")
run.pack(padx=10, pady=3, side="left")

search = Label(title_bar, text="Search", background="#bbb", padx=200)
search.pack(padx=100, pady=3, side="left")

close = Button(title_bar, text="X ", background="#ddd", command=close)
close.pack(padx=5, pady=3, side="right")

maxi = Button(title_bar, text="[]", background="#ddd", command=maximize)
maxi.pack(padx=5, pady=3, side="right")

mini = Button(title_bar, text="- ", background="#ddd", command=minimize)
mini.pack(padx=5, pady=3, side="right")

# ------------------------------------- File Menu
files = Frame(root, background="#eee", borderwidth="5", relief=SUNKEN)
files.pack(side=LEFT, fill=Y)

prog1 = Label(files, text="Program 1.py", background="#eee", borderwidth=1, relief=SOLID, font="TimesNewRoman 15")
prog1.pack(padx=3, pady=1)

prog2 = Label(files, text="Program 2.py", background="#eee", borderwidth=1, relief=SOLID, font="TimesNewRoman 15")
prog2.pack(padx=3, pady=1)

prog2 = Label(files, text="Program 3.py", background="#eee", borderwidth=1, relief=SOLID, font="TimesNewRoman 15")
prog2.pack(padx=3, pady=1)

prog2 = Label(files, text="Program 4.py", background="#eee", borderwidth=1, relief=SOLID, font="TimesNewRoman 15")
prog2.pack(padx=3, pady=1)

# -------------------------------------- Footer of VS Code -----------------------------
footer = Frame(root, background="#eee", borderwidth="5", relief=SUNKEN)
footer.pack(side=BOTTOM, anchor="sw", fill=X)

footer_top = Frame(footer, background="#eee")
footer_top.pack(anchor="ne", fill=X)

footer_body = Frame(footer, background="#eee")
footer_body.pack(anchor="ne", fill=X)

problem = Label(footer_top, text="PROBLEMS", background="#eee", font="serif 10 italic")
problem.pack(padx=10, pady=3, side=LEFT)

console = Label(footer_top, text="DEBUG CONSOLE", background="#eee", font="serif 10 italic")
console.pack(padx=10, pady=3, side=LEFT)

terminal = Label(footer_top, text="TERMINAL", background="#eee", font="serif 10 italic underline")
terminal.pack(padx=10, pady=3, side=LEFT)

terminal_body = Frame(footer_body, background="#eee")
terminal_body.pack(pady=100, side="bottom", anchor="s")

root.mainloop()