from tkinter import *


def get_lowest_time():

    try:
        with open("low_time.txt", "r") as file:
            lowest_time = file.read()
    except:
        with open("low_time.txt", "w") as file:
            file.write("1000")
            lowest_time = "1000"
    
    return lowest_time


def update_lowest_time():

    global lowest_time

    # checking game_is_on is necessary because after game gets off the current time becomes "0" which will store wrong input
    if (int(current_time) < int(lowest_time) and game_is_on):
        lowest_time = current_time
        lowest_time_label.configure(text=lowest_time)
        with open("low_time.txt", "w") as file:
            file.write(current_time)


def start_timer():

    global current_time
    if game_is_on:
        current_time = str(int(current_time)+1)
        current_time_label.configure(text = current_time)
        root.after(1000, start_timer)


def verify_key(event):

    global character
    key = event.char

    # The key events are present in the lowercase alphabets
    if (game_is_on and key == chr(character-65+97)):
        character_position = alphabets.index(chr(character))
        if (character_position==13 or character_position==16):
            key_list[character_position].configure(background=GREEN, foreground=BLACK)
        else:
            key_list[character_position].configure(background=LIGHT_GREEN, foreground=BLACK)
        character = character + 1
        root.update()


def start_game():

    global game_is_on, character

    if not game_is_on:
        game_is_on = True
        root.after(1000, start_timer)
        while game_is_on and character<=90:
            word_label.configure(text=chr(character))
            root.update()
        update_lowest_time()
        refresh_game()
            

def refresh_game():
    
    global game_is_on, character, current_time

    game_is_on = False
    word_label.configure(text=" ")
    character = 65
    current_time = "0"
    current_time_label.configure(text=current_time)

    for index,key in enumerate(key_list):
        if (index==13 or index==16):
            key.configure(background=LIGHT_BLACK, foreground=WHITE)
        else:
            key.configure(background=BLACK, foreground=WHITE)


YELLOW = "#FFFFEC"
GREEN = "#00FF00"
BLACK = "#22092C"
WHITE = "#FFFFFF"
BLUE = "#3876BF"
LIGHT_BLACK = "#333156"
LIGHT_GREEN = "#D2E3C8"
GAP_BETWEEN_KEYS = 90

alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                    'Z', 'X', 'C', 'V', 'B', 'N', 'M']

positions = [[50+i*GAP_BETWEEN_KEYS, 200] for i in range(10)] + [[80+i*GAP_BETWEEN_KEYS, 300] for i in range(9)] + [[120+i*GAP_BETWEEN_KEYS, 400] for i in range(7)]

current_time = "0"
lowest_time = get_lowest_time()
character = 65
game_is_on = False
key_list = []       # It will contain all the label widgets after program execution starts


root = Tk()
root.geometry("1000x700+50+50")
root.resizable(False, False)
root.title("Typing Speed Test")
root.config(background=BLUE)

# --------------------------------  Setup for score screen ------------------------------
time_screen = Frame(root, background=YELLOW)
time_screen.pack(fill=X)

lowest_time_text = Label(time_screen, text = "Lowest Time:", background=YELLOW, font=("Courier", 20, "bold"))
lowest_time_text.grid(row=0, column=0)

lowest_time_label = Label(time_screen, text = lowest_time, background=YELLOW, font=("Courier", 20, "bold"))
lowest_time_label.grid(row=0, column=1)

current_time_text = Label(time_screen, text = "Current Time:", background=YELLOW, font=("Courier", 20, "bold"))
current_time_text.grid(row=1, column=0)

current_time_label = Label(time_screen, text = current_time, background=YELLOW, font=("Courier", 20, "bold"))
current_time_label.grid(row=1, column=1)

# -------------------------------- Setup for score screen ends here --------------------------------


# --------------------------------- Setup for word screen -------------------------------------

word_label = Label(root, text=" ", background=BLUE, font=("courier", 50, "bold"))
word_label.pack(fill=X)

# -------------------------------- Setup for word screen ends here -------------------------------------


# ------------------------------- Setup for key screen -----------------------------

# Inserting all the Label widgets into key list
for i in range(0, 26):
    if (i==13 or i==16):
        bgcolor = LIGHT_BLACK
    else:
        bgcolor = BLACK
    new_label = Label(root, text=alphabets[i], anchor="center", background=bgcolor, foreground=WHITE, font=("Courier", 20, "bold"), height=2, width=5)
    new_label.place(x=positions[i][0], y=positions[i][1])
    key_list.append(new_label)

# ------------------------------ Setup for key screen end here --------------------------
    

# ----------------------------- Setup for button screen ---------------------------------------
    
start_button = Button(text="Start", font=("Courier 20 bold"), command=start_game)
start_button.place(x=100, y=525)

refresh_button = Button(text="Refresh", font=("Courier 20 bold"), command=refresh_game)
refresh_button.place(x=780, y=525)

# ------------------------------ Setup for button screen ends here --------------------------

root.bind("<Key>", verify_key)
root.mainloop()