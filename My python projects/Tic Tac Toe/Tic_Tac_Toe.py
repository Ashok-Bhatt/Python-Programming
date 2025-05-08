# username1 and username2 are two variable that takes the user name from two users and assigns them a symbol.
username1=input("Enter the name of user 1:")
print(f"{username1}, your symbol will be X.")
print("")
username2=input("Enter the name of user 2:")
print(f"{username2}, your symbol will be O.")
print("")

# position is the list containing all the position possibilities in tic tac toe game
position=[1,2,3,4,5,6,7,8,9]

# board list will contain all the crosses and circles at a given position
# Initially, it has empty strings which states that the board is empty
board=[" "," "," "," "," "," "," "," "," "]

# solution is the list containing the set of combinations for which a player can win a game
solution=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# reserved is a list in which the position elements that has been used during the game are stored
# It ensure that the users can't overwrite the cross or round 
reserved=[]

# game over is a variable defined whose value is taken zero which means that the game is still going on
# if any any of yhe user gets succedded in creating a winning pattern then the value of game_over variable becomes 1 which means that someone has won the game
game_over=0

def game_board():
    """
    game_board is a function which can be used to display the game-board during the active game
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def winner(Symbol,user1,user2):
    """
   winner is a function which is used to decide the winner of the tic tac toe game based on the matching of a symbol.
   It takes two additional parameters i.e., user1 which takes the winner name and user2 which takes the loser name
    """
    global board
    global solution
    for key in range(len(solution)):
        key1=solution[key][0]
        key2=solution[key][1]
        key3=solution[key][2]
        if board[key1-1]==board[key2-1]==board[key3-1]==Symbol:
            print(f"{user1} has won the game against {user2}.")
            global game_over
            game_over=1
            break   # we are breaking the loop when we find a match so that the loop won't waste the time to check the other combinations 

print("The positions in a game board are as follows:\n")
print(f" 1 | 2 | 3 ")
print("-----------")
print(f" 4 | 5 | 6 ")
print("-----------")
print(f" 7 | 8 | 9 ")
print("")

print("The initial stage of the game is given by:\n")
game_board()
print("")

i=0     # i is the number of turns played by the user 1
j=0     # j is the number of turns played by the user 2
while True:
    print(f"Turn:{i+j+1}")      # 1 is added to i+j in order to find the no. of turns because initially no one has played the game
    print("")
    # choice1 is the variable assigned to take the input from username1 for assigning the "X" symbol at specific position
    choice1=int(input(f"{username1}, Enter the position for the X symbol (1-9):"))
    if (choice1 not in position) or (choice1 in reserved):
        while (choice1 not in position) or (choice1 in reserved):
            print("You have either entered the position invalid for tic tac toe game or have entered the number that has been already used.\n")
            choice1=int(input(f"{username1}, Enter the position for the X symbol (1-9):"))
        else:
            reserved.append(choice1)
            board[choice1-1]="X"    # We are reducing the index by 1 as the indexing starts from zero
            print("")
            game_board()
            print("")
            winner("X",username1,username2)
            if game_over==1:
                break   # We are breaking the loop when the value of game_over variable becomes 1 which states that someone has won the game
            i+=1
    else:
        reserved.append(choice1)
        board[choice1-1]="X"
        print("")
        game_board()
        print("")
        winner("X",username1,username2)
        if game_over==1:
            break
        i+=1
    if i==5:
    # We are breaking the loop when the value of i becomes 5 because at that instance the no. of turns completed will be 4+5=9     [i=5 and j=4]
        break

    print(f"Turn:{i+j+1}")
    print("")
    # choice2 is the variable assigned to take the input from username2 for assigning the "O" symbol at specific position
    choice2=int(input(f"{username2}, Enter the position for the O symbol (1-9):"))
    if (choice2 not in position) or (choice2 in reserved):
        while (choice2 not in position) or (choice2 in reserved):
            print("You have either entered the position invalid for tic tac toe game or have entered the number that has been already used.\n")
            choice2=int(input(f"{username2}, Enter the position for the O symbol (1-9):"))
        else:
            reserved.append(choice2)
            board[choice2-1]="O"
            print("")
            game_board()
            print("")
            winner("O",username2,username1)
            if game_over==1:
                break
            j+=1
    else:
        reserved.append(choice2)
        board[choice2-1]="O"
        print("")
        game_board()
        print("")
        winner("O",username2,username1)
        if game_over==1:
            break
        j+=1
if game_over==0:    # We are checking whether the value of game_over at the end of game is zero or not to ensure if someone has won the game or not
    print("")
    print(f"{username1} and {username2}, None of you have won this game.")