import keyboard
import os

while keyboard.read_key() != "r":
    if keyboard.read_key() == "a":
        print("Yes! You Clicked 'a'.")