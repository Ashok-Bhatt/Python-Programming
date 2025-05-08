print("\nThis game has been created for you. We are randomly generating a number between 1 to 100 which you have to guess.")
print("This game includes Guess Points and Time Points.")
print("\nOn guessing the correct number at the first trial you will score 20 Guess Points.")
print("On guessing the wrong number, your 1 Guess Point will be deducted and on guessing the number out of range 1-100, you will lose 3 points.")
print("On giving 20 wrong guesses, your game will be over.")
print("\nOn guessing the correct number before or on 20 seconds, you will score 20 Time Points.")
print("On taking, every extra seconds, your 1 time point will be reduced.")
print("\nThe final score will depend on 60% Guess Points and 40% Time Points.")
print("\nSo, let's start the game.")

# username is the variable that stores the name of a user which could be helpful in the later game events
username=input("\nEnter your name:")

import os
os.system("cls")

# chance is the variable which denotes the number of turns the user currently has, which will reduce by 1 after each trial
chance=20

# time_points is the variable which denotes the points scored by the user for finishing the game at the particular time
# In the beginning, the time_points of the user is 20, which will reduce by 1 after each seconds if the time has exceeded 20 seconds
time_points=20


def time_taken():
    """
time_taken is the function that calculates the Time Points according to the the time taken by the user to complete the game
    """

    global time_points      # We are using global keyword for time_points so that it's value can change at a global level

    if total_time.total_seconds()<=20:      # The time_points will not reduced if the user guessed the number in 20 or less seconds
        time_points=20

    # On taking more than 20 seconds then for each second, time_points will get reduced by one.
    # We are using math.ceil to convert the decimal number to the next integer.     E.g.: If time_taken = 12.4, then it will be considered 13
    else:
        time_points -= math.ceil(total_time.total_seconds()-20)

    if time_points>0:
        return time_points
    else:
        # If time_points is less than 0, then it will be considered as 0
        return 0

import random

# num is the variable which stores the random number between 1 to 100
num=random.randint(1,100)

import time
from datetime import datetime

# We are starting the the game with the user input so that the game will count the time accordingly
start=input("\nEnter any key to start the game:")

start_time = datetime.now()    # start_time will denote the starting time of the game. 
end_time = datetime.now()      # end_time will denote the time taken by the user after a guess or after the game over

import math

while chance!=0:
    end_time = datetime.now()
    total_time = (end_time-start_time).total_seconds        # total_time will denote the no. of seconds taken by the user to finish the game

    # guess is the variable that stores the value guessed by the user
    guess=int(input(f"\n{username}, please guess the number:"))

    if guess==num:
        if chance==20:
            print("\nBravo! You guessed the correct answer in your first trial. A person with a great luck.")
        elif chance>15:
            print("\nBravo! You guessed the correct answer in very few trials. You must be a very intelligent person.")
        else:
            print("\nCorrect answer. You did it.")

        end_time = datetime.now()
        total_time = end_time-start_time

        # We will clear the screen in 5 seconds after guessing the correct answer and the score will be displayed
        time.sleep(5)
        os.system("cls")

        print(f"Time Taken: {total_time.total_seconds()} seconds \n")
        print("Guess Points:",chance) if (chance>=0) else print("Guess points:",0)      # If guess is less than 0, then it will be considered 0
        print("Time Points:",time_taken())
        print(f"Total Score: {chance*3 + time_taken()*2}/100")
        break

    else:
        if (guess>100) or (guess<0):
            print(f"What are you doing {username}, you guessed {guess} which is out of range 0-100. So you have losed your 3 points.")
            chance=chance-3     # On guessing the number out of range 0-100, the Guess points will be reduced by 3

        else:
            if math.fabs(guess-num)==1:
                print("OMG! You are almost about to win. Just move one number around and the victory is yours.")
            elif math.fabs(guess-num)<=3:
                print("Come on! You are almost done! The difference between this answer and the real number is less than or equal to 3.")
            elif math.fabs(guess-num)<=10:
                print("Come on! You are so close. The difference between this answer and the real number is less than or equal to 10.")
            elif math.fabs(guess-num)<=20:
                print("You are still not close enough. The difference between this answer and the real number is less than or equal to 20.")
            else:
                print("You are too far from the correct answer.")
            chance=chance-1

else:
    print("\nGame Over!")
    print(f"The actual number was {num}.")