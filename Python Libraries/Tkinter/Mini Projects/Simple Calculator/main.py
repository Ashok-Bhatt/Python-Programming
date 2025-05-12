from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            scvalue.set(str(eval(scvalue.get())))
        except:
            scvalue.set("Error")
    elif text=="C":
        scvalue.set("")
    else:
        if (scvalue.get()=="Error" or scvalue.get()=="0"):
            scvalue.set("")
        scvalue.set(scvalue.get() + text)
        
numbers = [str(i) for i in range(1,10)]
operators = ["+", "-", "*", "/", ".", "=", "C", "0", "00"]

root = Tk()
root.geometry("500x750+5+5")
root.iconbitmap("C:\\Users\\Ashok Bhatt\\Desktop\\Projects\\Simple Calculator (Python Tkinter)\\calculator.ico")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")

# Screen Part where results will be displayed
screen_frame = Frame(root, borderwidth=5, padx=5, pady=5, relief=SUNKEN)
screen_frame.pack(fill=X, padx=5, pady=5)

screen = Entry(screen_frame, textvariable=scvalue, font ="lucida 40 bold", justify="right", background="#0d6")
screen.pack()
# -------------- Screen Part Ends ----------------------

# Body that will contain the buttons
button_frame = Frame(root, borderwidth=5, padx=5, pady=5, relief=SUNKEN)
button_frame.pack(fill=X, padx=5, pady=5)

for row in range(6):
    button_row = Frame(button_frame, padx=5, pady=5)
    button_row.pack(fill=X, padx=5, pady=5, side="top")

    for col in range(3):
        if (row<=2):
            index = (2-row)*3 + col
            button = Button(button_row, text=numbers[index], padx=20, pady=20, background="black", foreground="white", font="lucida 10 bold")
            button.pack(padx=30, side="left")
            button.config(height=2, width=2)
            button.bind("<Button-1>", click)
        else:
            index = (row-3)*3 + col
            button = Button(button_row, text=operators[index], padx=20, pady=20, background="black", foreground="white", font="lucida 10 bold")
            button.pack(padx=30, side="left")
            button.config(height=2, width=2)
            button.bind("<Button-1>", click)

# --------------- Body Part ends ----------------------

root.mainloop()