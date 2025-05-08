from tkinter import *

root1 = Tk()
width = 800
height = 400
X_MIN = 0
Y_MIN = 0
X_MAX = root1.winfo_screenwidth() - width
Y_MAX = root1.winfo_screenheight() - height

root1.geometry(f"{width}x{height}+{X_MAX//2}+{Y_MAX//2}")
root1.config(bg="green", borderwidth=5, relief=SUNKEN)
root1.attributes("-alpha", 0.5)
root1.resizable(False,False)
root1.mainloop()

root2 = Tk()
root2.geometry(f"{width}x{height}+{0}+{0}")
root2.config(bg="green", borderwidth=5, relief=SUNKEN)
root2.attributes("-alpha", 0.5)
root2.resizable(False,False)
root2.mainloop()

root3 = Tk()
root3.geometry(f"{width}x{height}+{X_MAX}+{0}")
root3.config(bg="green", borderwidth=5, relief=SUNKEN)
root3.attributes("-alpha", 0.5)
root3.resizable(False,False)
root3.mainloop()

root4 = Tk()
root4.geometry(f"{width}x{height}+{0}+{Y_MAX}")
root4.config(bg="green", borderwidth=5, relief=SUNKEN)
root4.attributes("-alpha", 0.5)
root4.resizable(False,False)
root4.mainloop()

root5 = Tk()
root5.geometry(f"{width}x{height}+{X_MAX}+{Y_MAX}")
root5.config(bg="green", borderwidth=5, relief=SUNKEN)
root5.attributes("-alpha", 0.5)
root5.resizable(False,False)
root5.mainloop()