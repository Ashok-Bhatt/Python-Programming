
from datetime import date
from random import randint
from tkinter import *


def get_random_color():

    color1 = "#"
    color2 = "#"
    digits = [chr(i+48) for i in range(10)] + [chr(i+65) for i in range(6)]

    for _ in range(6):
        digit = randint(0,15)
        color1 = color1 + digits[digit]
        color2 = color2 + digits[15-digit]

    return [color1, color2]


subject_schedule = {
    "TOC": [date(2023, 12, 11), date(2024, 1, 24)],
    "Compiler": [date(2024, 1, 25), date(2024, 2, 22)],
    "Digital": [date(2024, 1, 3), date(2024, 2, 9)],
    "C Prog": [date(2024, 2, 12), date(2024, 3, 15)],
    "DS": [date(2024, 2, 23), date(2024, 3, 30)],
    "Stats": [date(2024, 1, 30), date(2024, 3, 25)],
    "Algebra": [date(2024, 3, 25), date(2024, 4, 15)],
    "CN": [date(2024, 4, 12), date(2024, 6, 12)],
    "OS": [date(2024, 6, 13), date(2024, 8, 2)],
    "DM": [date(2024, 6, 13), date(2024, 8, 14)],
    "DBMS": [date(2024, 8, 5), date(2024, 10, 11)],
    "Algo": [date(2024, 8, 16), date(2024, 10, 16)],
    "Aptitude": [date(2024, 9, 13), date(2024, 10, 25)],
    "COA": [date(2024, 10, 14), date(2024, 11, 29)],
}

subject_color_list = [get_random_color() for _ in range(14)]
months = {0: ["Jan", 31], 1: ["Feb", 29], 2: ["Mar", 31], 3: ["Apr", 30], 4: ["May", 31], 5: ["Jun", 30], 6: ["Jul", 31], 7: ["Aug", 31], 8: ["Sep", 30], 9:["Oct", 31], 10:["Nov", 30], 11:["Dec", 31],}

terminal_dates = [date(2023, 12, 11), date(2024, 11, 29)]
HEIGHT = 700
WIDTH = 1200
GRAY = "#dddddd"
BLACK = "#000000"

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}+50+50")
root.title("Gate Classes Timeline")
root.configure(bg=GRAY)

timeline_picture = Canvas(root, height=600, width=1150)

# creating the month columns
y1 = 50
y2 = (date(2023, 12, 31) - terminal_dates[0]).days*1.6 + y1
y0 = (y1+y2)/2

timeline_picture.create_rectangle(0, y1, 100, y2)
timeline_picture.create_text(50, y0, text="DEC", font=("courier", 10, "bold"))
timeline_picture.create_line(0, y2, 1150, y2, fill="#aaa")

for i in range(12):
    y1 = y2
    y2 = y1 + months[i][1]*1.6
    y0 = (y1+y2)/2
    timeline_picture.create_rectangle(0, y1, 100, y2)
    timeline_picture.create_text(50, y0, text=months[i][0], font=("courier", 10, "bold"))
    timeline_picture.create_line(0, y2, 1150, y2, fill="#aaa")


# writing the subject names as the column names
for index, subject in enumerate(subject_schedule):

    x1 = index*70 + 100
    x2 = x1 +70
    x0 = (x1+x2)/2
    timeline_picture.create_rectangle(x1, 0, x2, 50, fill=subject_color_list[index][0])
    timeline_picture.create_rectangle(x1, 0, x2, 600)
    timeline_picture.create_text(x0, 25, text=subject, font=("courier", 10), fill=subject_color_list[index][1])


# Creating the subject timelimes
for index, subject in enumerate(subject_schedule):

    x1 = index*70 + 100
    x2 = x1 + 70
    y1 = ((subject_schedule[subject][0] - terminal_dates[0]).days)*1.5 + 50
    y2 = ((subject_schedule[subject][1] - terminal_dates[0]).days)*1.5 + 50
    timeline_picture.create_rectangle(x1, y1, x2, y2, fill=subject_color_list[index][0])


timeline_picture.pack(padx=50, pady=50)

root.mainloop()