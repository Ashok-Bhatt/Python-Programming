import random
from hangmanKit import printHangman

possible_words = ["apple","banana","cherry","grapes","grave","backyard"]
word = random.choice(possible_words)
word_list = ["-"]*len(word)

lives = 7
while (lives>0 and "-" in word_list):

    guess = input("Guess the character: ").lower()

    found = False
    for index,element in enumerate(word):
        if element==guess and word_list[index]=="-":
            word_list[index] = guess
            found = True

    for i in word_list:
        print(i, end=" ")
    print()

    if found == False:
        lives = lives-1
    
    printHangman(lives)

if lives:
    print("\nYou Won")
else:
    print("You Lose")