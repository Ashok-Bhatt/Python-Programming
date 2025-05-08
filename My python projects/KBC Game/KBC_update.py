
import random
import csv
import os
import time


def is_correct_answer(correct_answer, user_answer):

    """
    a function to check whether the answer given by user is correct or not
    """

    if user_answer.lower() == correct_answer:
        return True
    return False
    

def fetch_questions():

    """
    a function that will fetch the list of question-answer pair from csv file
    """

    question_list = []
    with open("questions.csv") as file:
        csvfile = csv.reader(file)
        for question in csvfile:
            question_list.append(question)
    
    return question_list


print("Welcome back to KBC: 'Kaun Banega Crorepati'".center(150))
print("""\nFollowing are some instructions regarding the game:
This game consists of 15 questions and on every right answer, you will be assigned some amount.
On entering the wrong answer,the game will be over and your prize money will be dispalyed.
We have created this game in a very precise manner so that you can answer the given question in any case i.e. lower,upper or capitalize.
Be sure that you are entering the correct spelling of the answer as we can't do anything for it.
You can skip the question three times. Afterwards skipping the question will be restricted. To skip the question, enter 'S' or 'skip'. Entering another word will lead to command that you don't want to skip the question. Again this command is not case-sensitive.
In case of our answer being an number, don't write it's spelling. It will be considered wrong. Simply enter the figure in digits.
      
The amount you will be winning after the each question is as follows:
15| 7 Crore
14| 1 Crore
13| 50 lac
12| 25 lac
11| 12.5 lac
10| 6.4 lac
9 | 3.2 lac
8 | 1.6 lac
7 | 80 thousand
6 | 40 thousand
5 | 20 thousand
4 | 10 thousand
3 | 5 thousand
2 | 3 thousand
1 | 1 thousand""")

# list1 is a 2 dimensional list
# list1 contains 30 elements and every element contains two sub-elements: question and it's correct answer
question_list = fetch_questions()

# life has initialized 1, which states that you are still in game, becomes 0 whenever you gave wrong answer
life = 1

# score denotes the number of questions you have answered correct.
score = 0

# skip denotes the number of times you can skip the questions. It is initialized eith 3 which will reduce until it reaches 0 which means you cannot skip after that
skip = 3

# amounts is array which will contain different money amounts that you can win after each correct answer to the question
amounts = [0, 1000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

user = input("\nEnter your name:")
os.system("cls")

print(f"\nWelcome {user}, Let's start the game.")

# game will stop once wrong answer is given or score reaches 15
while (life==1 and score!=15):

    time.sleep(1)
    os.system("cls")
    question = random.choice(question_list)
    print("\n", question[0], sep="\b ")      # Accessing only index 0, i.e. question
    
    answer = ""       # initializing the answer with \n to enter into the loop
    prev_skip = skip

    # trying to get answer from user until he/she enters any answer in case he/she has no skips else reducing one skip
    while (answer==""):
        answer = input("\nEnter the answer:")
        if (answer == ""):
            if (skip == 0):
                print("No more skips left")
            else:
                print(f"1 skip reduced. {skip-1} skip left")
                skip = skip - 1
                question_list.remove(question)
                break
    
    # checking id value of skip is reduced or not
    if (prev_skip != skip):
        continue

    # checking the answer provided by user in comparison to real answer
    if (is_correct_answer(question[1].strip(), answer.strip())):
        print("\nAbsolutely correct answer.")
        if score<14:
            print("Now lets move to our next question.")
        score = score + 1
        question_list.remove(question)      # Ensuring the question won't repeat by removing it
    else : 
        print(f"Unfortunately! The answer is wrong. \nThe correct answer of this question is {question[1].title()}. \nSo, your game is over.")
        life = 0


if score==0:
     print(f"Unfortunately! {user}, you didn't won any amount today. But, still claps for you. And best wishes for your upcoming future.")
elif score<14:
    print(f"Congratulations! {user}, you have won {amounts[score]}. A very very congratulations to you and your upcoming future.")
elif score==14:
    print(f"Congratulations! {user}, you have won {amounts[score]}. You have become the new crorepati of this season. \nThis is your check of 1 crore and best wishes for your upcoming future.")
else:
    print(f"""A very very very big Congratulations!!!!!!!!!!!! to you {user}. You have won {amounts[score]}. And now you are the new maha crorepati of this season
    This is your check of 7 crores. This seems to be a very proud moment for you and especially for your parents.
    A very very best wishes for your upcoming future.
    Audience, a very big aplause of round for {user} """)