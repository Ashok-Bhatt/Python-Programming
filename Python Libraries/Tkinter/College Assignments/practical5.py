from tkinter import *


def store_data():
    
    with open("employee_data.txt", "a") as file:
        name = emp_name.get()
        know_c = c_value.get()
        know_java = java_value.get()
        know_python = python_value.get()
        
        json_data = f'''
employee : {{
    name: {name},
    languages known: {{
        "C Language" : {know_c},
        "Java Language" : {know_java},
        "Python Language" : {know_python}
    }}
}}
        '''
        file.write(json_data)
        root.destroy()


def clear_data():

    global emp_name, c_value, java_value, python_value

    emp_name.set("")
    c_value.set(False)
    java_value.set(False)
    python_value.set(False)


root = Tk()
root.geometry("900x600")
root.config(padx=250, pady=100)

Label(root, text="Employee Details", font="timesnewroman 20 bold").grid(row=0, column=0, columnspan=6, sticky="n", pady=20)

Label(root, text="Employee Name", font="timesnewroman 10").grid(row=1, column=3, columnspan=3, sticky="w", padx=20)

Label(root, text="Programming Languages Known", font="timesnewroman 10").grid(row=2, column=0, columnspan=3, sticky="e", padx=20, pady=20)

emp_name = StringVar()
emp_name_entry = Entry(textvariable=emp_name, width=35).grid(row=2, column=3, columnspan=3, sticky="e", padx=20, pady=20)

c_value = BooleanVar()
c_check = Checkbutton(variable=c_value).grid(row=3,column=0, sticky="w")
c_label = Label(root, text="C").grid(row=3, column=0, sticky="n")

java_value = BooleanVar()
java_check = Checkbutton(variable=java_value).grid(row=3,column=1, sticky="w")
java_label = Label(root, text="Java").grid(row=3, column=1, sticky="n")

python_value = BooleanVar()
python_check = Checkbutton(variable=python_value).grid(row=3,column=2, sticky="w")
python_label = Label(root, text="Python").grid(row=3, column=2, sticky="n")

okay_button = Button(root, text="Okay", command=store_data).grid(row=3, column=3)
cancel_button = Button(root, text="Cancel", command=clear_data).grid(row=3, column=5)

root.mainloop()