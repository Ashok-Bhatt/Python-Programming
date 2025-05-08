from tkinter import *
from random import choice

HEIGHT = 600
WIDTH = 1000
WHITE = "#dddddd"
root = None
button_window = None

def create_main_window():

    global root
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+50+50")
    root.title("Grid Screen")


def create_button_window():

    global button_window
    button_window = Tk()
    button_window.geometry(f"200x100+1100+50")
    button_window.title("Grid Generating Window")

    grid_generator = Button(button_window, text="Generate Grid", command=generate_grid)
    grid_generator.pack(padx=10, pady=10)


def get_random_color():

    color = "#"
    digit_list = [str(i) for i in range(0,10)] + [chr(i+97) for i in range(0,6)]

    for digits in range(0,6):
        color = color + choice(digit_list)
    
    return color


def generate_grid():
    try:
        for i in range(0,8):
            for j in range(0,10):
                frame_color = get_random_color()
                color_frame = Frame(root, height=HEIGHT/8, width=WIDTH/10, background=frame_color)
                color_frame.grid(row=i, column=j)
    except:
        create_main_window()
        generate_grid()


create_main_window()
create_button_window()
root.mainloop()
button_window.mainloop()