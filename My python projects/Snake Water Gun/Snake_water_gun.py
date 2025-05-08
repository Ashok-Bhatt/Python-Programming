print("Welocome to our Snake Water Gun game.".center(150))
print("\nThe simple rule followed for this game is you need to choose one out of Snake, Water and Gun.\nSnake is superior to Water, Water is superior to Gun and Gun is superior to Snake.")
print("Choose:\n\t0 for Snake\n\t1 for Water\n\t2 for Gun")

# username is the variable that stores the name of the user
# Using the username, we can track the progress of the user in the entire history of the game
username= input("\nEnter your name:")

# round is the variable that stores the number of round played by the user during the game time, which is initially zero as no game has been played
round=0
# user_points and computer_points will denote the score of user and computer respectively during game time
user_points=0
computer_points=0

# choice_list is the list that will store the Snake, Water and Gun according to the indices.
# Because of this we can know what decisions did the computer and the user has made
choice_list=["Snake","Water","Gun"]

def win(i,j):
    """
win function will decide the winner of the round on the basis of the win-loss matrix
    """
    # winner_list is the multidimensional list whose first index is the choice of the computer and second index is the choice of the user
    # 1 shows that the user has won the game, 0 shows that the game has been tied and -1 shows that the user has loss the game
    winner_list=[[0,-1,1],[1,0,-1],[-1,1,0]]
    if winner_list[i][j]==1:
        global user_points
        user_points=user_points+1
        return f"The point of this round goes to {username}."
    elif winner_list[i][j]==-1:
        global computer_points
        computer_points=computer_points+1
        return "The point of this round goes to computer."
    else:
        return f"This round is a draw between {username} and computer."

number_rounds=int(input("Enter the number of rounds you want to play in this round:"))
if number_rounds<=0:
    print("The number of rounds cannot be zero or negative number.")
else:
    # We are importing the random module to make the computer decide the integer bretween 0 and 2
    import random
    while round<number_rounds:
        # computer_choice will randomly decide the number between 0 to 2 and any of Snake, Water and Gun will be decided accordingly
        computer_choice=random.randint(0,2)
        # We are taking the value of user_choice to be 3 at the beginning so that the variable is defined before the loop starts
        # user_choice will be user's choice of integer between 0 and 2 which will decide any of Snake, Water and Gun accordingly
        user_choice=3
        while user_choice<0 or user_choice>2:
            print(f"\nRound no.:{round+1}")
            user_choice=int(input("Enter the number: 0 for Snake, 1 for Water and 2 for Gun:"))
            if 0<=user_choice<=2:
                print(f"\n{username} choosed {choice_list[user_choice]}.")
                print(f"Computer choosed {choice_list[computer_choice]}.")
                print(win(computer_choice,user_choice))
                round=round+1
            else:
                print("\nPlease choose an integer between 0 and 2.")

print(f"\nfinal score of {username} is {user_points}.")
print(f"final score of Computer is {computer_points}.")

if user_points>computer_points:
    print(f"\n{username} has won this game against Computer by {user_points-computer_points} points.")
elif user_points<computer_points:
    print(f"\n{username} has loosed this game against Computer by {computer_points-user_points} points.")
else:
    print(f"There is a draw between {username} and computer.")
    print("\nGet ready for the game draw round.")
    # We are taking the value of user_choice to be 4 at the beginning so that the variable is defined before the loop starts
    user_choice=4
    while (user_choice<0 or user_choice>2) or (computer_choice==user_choice):
        computer_choice=random.randint(0,2)
        user_choice=int(input("Enter the number: 0 for Snake, 1 for Water and 2 for Gun:"))
        if 0<=user_choice<=2:
            print(f"\n{username} choosed {choice_list[user_choice]}.")
            print(f"Computer choosed {choice_list[computer_choice]}.")
            print(win(computer_choice,user_choice))
            if user_points>computer_points:
                print(f"\n{username} has won this draw round and game against computer.")
            elif user_points<computer_points:
                print(f"\n{username} has loosed this draw round and game against computer.")
            else:
                print(f"\nStill a draw between {username} and computer. Let's try again.")
        else:
            print("Please choose an integer between 0 and 2.")