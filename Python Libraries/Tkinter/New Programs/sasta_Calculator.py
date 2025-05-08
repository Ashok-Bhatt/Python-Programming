from tkinter import *
from random import randint

def addition():
    x = randint(1,10)
    y = randint(1,10)
    result = x + y
    print(f"x={x}   y={y}       =========>      Addition:{result}")

def subtraction():
    x = randint(1,10)
    y = randint(1,10)
    result = x - y
    print(f"x={x}   y={y}       =========>      Subtraction:{result}")

def multiplication():
    x = randint(1,10)
    y = randint(1,10)
    result = x * y
    print(f"x={x}   y={y}       =========>      Multiplication:{result}")

def division():
    x = randint(1,10)
    y = randint(1,10)
    result = x / y
    print(f"x={x}   y={y}       =========>      Division:{result}")

root = Tk()
root.geometry("800x500")

add = Button(text="ADD", background="black", foreground="white", font="verdana 15 bold", padx=5, pady=2, command=addition)
add.pack(side=LEFT, pady=5, padx=20, anchor="nw")

sub = Button(text="SUB", background="black", foreground="white", font="verdana 15 bold", padx=5, pady=2, command=subtraction)
sub.pack(side=LEFT, pady=5, padx=20, anchor="nw")

mul = Button(text="MUL", background="black", foreground="white", font="verdana 15 bold", padx=5, pady=2, command=multiplication)
mul.pack(side=LEFT, pady=5, padx=20, anchor="nw")

div = Button(text="DIV", background="black", foreground="white", font="verdana 15 bold", padx=5, pady=2, command=division)
div.pack(side=LEFT, pady=5, padx=20, anchor="nw")

root.mainloop()