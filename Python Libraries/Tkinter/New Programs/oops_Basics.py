from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("880x500")
    
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(fill=X, side="bottom")

    def click(self):
        print("Button Clicked!")

    def createButton(self, iptext):
        Button(text=iptext, command=self.click).pack()

if __name__ == "__main__":
    window = GUI()
    window.status()
    window.createButton("Click Here")
    window.mainloop()