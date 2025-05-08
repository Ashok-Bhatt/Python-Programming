from tkinter import *

def food_info(x):
    if x:
        return "You ordered your food in advance."
    return "You didn't ordered your food in advance."

def registration():
    print("Name: " , namevalue.get())
    print("Phone: " , phonevalue.get())
    print("Gender: " , gendervalue.get())
    print("Emergency: " , emergencyvalue.get())
    print("PayMode: " , payvalue.get())
    print(food_info(foodservicevalue.get()))

root = Tk()
root.geometry("500x400")

name = Label(text="Name").grid(row=0, column=0, sticky="w", padx=5, pady=3)
phone= Label(text="Phone No.").grid(row=1, column=0, sticky="w", padx=5, pady=3)
gender = Label(text="Gender").grid(row=2, column=0, sticky="w", padx=5, pady=3)
emergency = Label(text="Emergency").grid(row=3, column=0, sticky="w", padx=5, pady=3)
paymode = Label(text="Payment Mode").grid(row=4, column=0, sticky="w", padx=5, pady=3)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
payvalue = StringVar()

nameEntry = Entry(textvariable=namevalue).grid(row=0, column=1)
phoneEntry = Entry(textvariable=phonevalue).grid(row=1, column=1)
genderEntry = Entry(textvariable=gendervalue).grid(row=2, column=1)
emergencyEntry = Entry(textvariable=emergencyvalue).grid(row=3, column=1)
payEntry = Entry(textvariable=payvalue).grid(row=4, column=1)

food = Label(text="Do you want to book your meal in advance?")
food.grid(row=5, column=1,padx=5, pady=3)

foodservicevalue = BooleanVar()
foodservice = Checkbutton(textvariable=foodservicevalue)
foodservice.grid(row=5,column=0, sticky="e")

register = Button(text="Register", background="black", foreground="white", command=registration).grid(row=6, column=0)

root.mainloop()