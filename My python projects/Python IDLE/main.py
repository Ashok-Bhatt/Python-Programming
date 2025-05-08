from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import os

def change_mode():

    global current_mode,mode_image
    if current_mode == dark_mode:
        current_mode = light_mode
        options.configure(bg="white")
        mode.configure(background="white")
        open_button.configure(background="white")
        save_button.configure(background="white")
        run_button.configure(background="white")
        console.configure(background="white", foreground="black")
        textarea.configure(background="white", foreground="black")
    else:
        current_mode = dark_mode
        options.configure(bg="black")
        mode.configure(background="black")
        open_button.configure(background="black")
        save_button.configure(background="black")
        run_button.configure(background="black")
        console.configure(background="black", foreground="white")
        textarea.configure(background="black", foreground="white")

    new_photo = Image.open(current_mode).resize((100, 100))
    mode_image = ImageTk.PhotoImage(new_photo)
    mode.configure(image=mode_image)


def open_file():
    global file_path
    file_path = askopenfilename(defaultextension=".py", filetypes=[("Python Files","*.py")])
    if file_path=="":
        file_path = None
        root.title("No File Opened")
    else:
        root.title(os.path.basename(file_path))
        with open(file_path, "r") as file:
            code = file.read()
            textarea.delete(1.0,END)
            textarea.insert(1.0 , code)


def save_file():
    global file_path
    if file_path==None:
        file_path = asksaveasfilename(defaultextension=".py", filetypes=[("Python Files","*.py")])
        if file_path=="":
            file_path = None
            root.title("No File Opened")
        else:
            root.title(os.path.basename(file_path))
            with open(file_path,"w") as file:
                file.write(textarea.get(1.0,END))
    else:
        with open(file_path,"w") as file:
            file.write(textarea.get(1.0,END))


def run_file():
    if file_path != None:
        command = f'python "{file_path}"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=TRUE)
        result, error = process.communicate()
        console.insert(END,result.decode())
        console.insert(END,error.decode())


# File paths for images required for light and dark mode
dark_mode = "C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Python IDLE\\Images\\dark.png"
light_mode = "C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Python IDLE\\Images\\light.png"

# File paths required for icon, save, open and run
icon_path = "C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Python IDLE\\Images\\logo.png"
open_path = "C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Python IDLE\\Images\\open.png"
save_path = "C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Python IDLE\\Images\\save.png"
run_path = "C:\\Users\\Ashok Bhatt\\Desktop\\Python Programming Work\\Python Libraries\\Tkinter\\New Programs\\Python IDLE\\Images\\run.png"

file_path = None
current_mode = dark_mode

root = Tk()
root.geometry("1400x600+50+50")
root.resizable(TRUE,FALSE)
root.title("No File Opened")
root.iconbitmap(icon_path)

# -------------------------- Creating the leftmost sidebar of IDE which contains features like save, open, run, etc.
options = Frame(root, bg="black", relief="sunken", borderwidth=5)

# For file opening option
open_file_photo = Image.open(open_path).resize((100,100))
open_file_image = ImageTk.PhotoImage(open_file_photo)
open_button = Button(options, image=open_file_image, background="black", relief="flat", command=open_file)
open_button.pack(side=TOP, anchor="nw", padx = 25, pady=10)

# For File saving option
save_file_photo = Image.open(save_path).resize((100,100))
save_file_image = ImageTk.PhotoImage(save_file_photo)
save_button = Button(options, image=save_file_image, background="black", relief="flat", command=save_file)
save_button.pack(side=TOP, anchor="nw", padx = 25, pady=10)

# For Option to run the python file
run_file_photo = Image.open(run_path).resize((100,100))
run_file_image = ImageTk.PhotoImage(run_file_photo)
run_button = Button(options, image=run_file_image, background="black", relief="flat", command=run_file)
run_button.pack(side=TOP, anchor="nw", padx = 25, pady=10)

# For setting Light/Dark Mode
mode_photo = Image.open(current_mode).resize((100,100))
mode_image = ImageTk.PhotoImage(mode_photo)
mode = Button(options, image=mode_image, background="black", relief="flat", command=change_mode)
mode.pack(side=TOP, anchor="nw", padx = 25, pady=10)

options.pack(side=LEFT, anchor="nw", fill=Y)
# -------------------------- Leftmost sidebar created -------------------------------------

# -------------------------- Contains the Text Area for writing python code ----------------
input = Frame(root)

textarea = Text(input, background="black", foreground="white", font="lucida", padx=15, pady=5, width=60)
textarea.pack(anchor="nw", fill=Y, expand=TRUE)

input.pack(side=LEFT, anchor="nw", fill=Y, expand=TRUE)
# -------------------------- Text Editor ends here -----------------------------------------

# -------------------------- Console part of the program ------------------------------------
output = Frame(root, relief="sunken", borderwidth=5)

console = Text(output, background="black", foreground="white", font="lucida", padx=15, pady=5)
console.pack(anchor="nw", fill=Y, expand=TRUE)

output.pack(side=LEFT, anchor="nw", fill=Y, expand=TRUE)
# ---------------------------- Console Part ends here ----------------------------------------

root.mainloop()