print("Welcome back to KBC: 'Kaun Banega Crorepati'".center(150))
print("\nFollowing are some instructions regarding the game:")
print("\nThis game consists of 15 questions and on every right answer, you will be assigned some amount.")
print("On entering the wrong answer,the game will be over and your prize money will be dispalyed.")
print("\nWe have created this game in a very precise manner so that you can answer the given question in any case i.e. lower,upper or capitalize.")
print("Be sure that you are entering the correct spelling of the answer as we can't do anything for it.")
print("\nYou can skip the question three times. Afterwards skipping the question will be restricted. To skip the question, enter 'S' or 'skip'. Entering another word will lead to command that you don't want to skip the question. Again this command is not case-sensitive.")
print("\nIn case of our answer being an number, don't write it's spelling. It will be considered wrong. Simply enter the figure in digits.")
print("\nThe amount you will be winning after the each question is as follows:")
print("\n15| 7 Crore \n14| 1 Crore \n13| 50 lac \n12| 25 lac \n11| 12.5 lac \n10| 6.4 lac \n9 | 3.2 lac \n8 | 1.6 lac \n7 | 80 thousand \n6 | 40 thousand \n5 | 20 thousand \n4 | 10 thousand \n3 | 5 thousand \n2 | 3 thousand \n1 | 1 thousand \n")

# list1 is a 2 dimensional list
# list1 contains 30 elements and every element contains two sub-elements: question and it's correct answer
list1=[["Which is the largest planet in our solar system:","jupiter"],
["Which country is the leading producer of sugarcane:","brazil"],
["How many states are there in south India:","5"],
["Is ice less dense than water? Kindly enter 'Y' for yes and 'N' for no:","y"],
["What is capital of Rajasthan?","jaipur"],
["How many meters are there in one gigameter:","1000000000"],
["Which is the largest land animal:","elephant"],
["Which vegetable is also known as Egg plant:","brinjal"],
["Does mass of body matters in case of calculating it's escape speed from earth? Kindly enter 'Y' for yes and 'N' for no:","n"],
["How many complex cuberoots does the one have:","2"],
["Which is the highest grossing movie of all time in the entire world:","avatar"],
["For what value of radius, the numerical value of circumference is same to that of it's area:","2"],
["How many foot are there in one yard:","3"],
["Which is the only even prime number:","2"],
["Which is the highest grossing anime series of all time in the entire world:","pokemon"],
["What is the extension used to save the python program:",".py"],
["which is the largest country in the world in terms of area:","russia"],
["Which planet in solar system is also a name of an element:","mercury"],
["Which is the longest river in the world:","nile"],
["Which marvel character turns into a giant green monster like being whenever he gets angry because of the gamma radiation inside it:","hulk"],
["Which is the fastest running bird:","ostrich"],
["How many bones does the average adult human have:","206"],
["Which state of India has the highest literacy rate:","kerala"],
["Which is the longest epic in the world:","mahabharat"],
["What is the height of the Mount Everest (in meters)? Please enter only number and dont't include the unit:","8848"],
["In which country both lions and tigers are found:","india"],
["How many planets in solar system don't have moons:","2"],
["Which is the smartest aquatic animal:","dolphin"],
["Which trigonometric function denotes the x-coordinate of a unit circle? Please kindly enter sin, cos, tan, sec, cosec, or cot:","cos"],
["Which is the most abundant element in the Earth's atmosphere:","nitrogen"]]

# life has been taken 1, which states that you are still in game. 
# On giving wrong answer, the value of life becomes zero which tells that you are eliminated from the game.
life=1
# score denotes the number of questions you have answered correct.
# In beginning, it is taken 0 and after each correct answer, it gets increased by one.
score=0
# skip denotes the number of times you can skip the questions.
# In beginning, the value of skip is taken 3 and after 3 trials, it's value becomes 0 which means that you can't skip the questions anymore.
skip=3
# amount is the total amount won by the user after you won the or lose the game.
# The elements of amount can be accessed by taking the score variable as the indices for elements of amount list.
amount=[0, 1000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

user=input("Enter your name:")      # user ia a variable defined to take the user name as an input to execute it in any statement whenever required
print("\nWelcome",user)
print("Let's start the game.")
print("")

def answer():
    """
    answer function is used to check whether our answer is correct or not
    It cotains our two global variables: life score
    """
    # variable score and life has been called using the global keyword as they are defined at global scope not at local scope
    global score
    global life
    if ans.lower()==quiz[1]:            # We are comparing our answer in lower case with actual answers that are stored in lower case to avoid spelling errors that can cause mismatch of the answers
        print("")
        print("Absolutely correct answer.")
        if score<14:
            # The below statement will be executed if your score is less than 14
            # It is not specified for 15 because before that instance you have answered only 14 question, not 15 and the value of score variable will become 15 afterwards
            print("Now lets move to our next question.")
        print("")
        life=1
        score+=1    # The increment in score by one states that you have won some prize amount, more than previous one
    else:
        print("")
        print("Unfortunately! This answer is not correct.")
        print("The correct answer of this question is",quiz[1].title())
        print("Now your game is over.")
        print("")
        life=0      # The value of life=0 ensure that you have terminated the loop and the game is over

import random
while (life==1)&(score!=15):        # stopping the loop when the value of score become zero ensures that you won't win more than 7 crore.
    quiz=random.choice(list1)
    print(quiz[0])      # Here, we are accessing only first element of quiz to ensure that the answer is not going to be printed
    # skip_choice variable asks if you want to skip the question if you aren't sure about the correct answer.
    skip_choice=input("Do you want to skip the this question? Use 'skip' or 's' to do so. Enter anything if you don't want to skip:")
    if (skip_choice.lower()=="skip")|(skip_choice.lower()=="s"):
        if skip==0:     # In case, of skip variable has zero value , you aren't no more able to skip the question
            print("You cant't skip now.")
            ans=input("Enter the answer:")      # ans variable asks you to enter the answer
            answer()
        else:
            life=1
            skip-=1         # Reducing value of skip by one tells us that you have lost your one skip lifeline
            print("")
            print("So",user,"has decided to skip the question.")
            if skip!=0:
            # Below statement will be executed if the value of skip variable is not zero.
            # The statement is not specified for value one unlike the method used in score variable as value of skip has alraedy reduced by one at this instance
                print("Now you can skip the questions only",skip,"times.")
            else:
                print("Now, You can't skip the question.")
            print("Now let's move to the next question.")
            print("")
    else:
        ans=input("Enter the answer:")
        answer()
    list1.remove(quiz)      # Removing the asked question from the list ensures that the question will not be displayed again.

if score==0:
     print("Unfortunately!",user,",you didn't won any amount today. But, still claps for you. And best wishes for your upcoming future.")
elif score<14:
    print("Congratulations!",user,",you have won",amount[score],". A very very congratulations to you and your upcoming future.")
elif score==14:
    print("Congratulations!",user,",you have won",amount[score],". You have become the new crorepati of this season.")
    print("This is your check of 1 crore and best wishes for your upcoming future.")
else:
    print("A very very very big Congratulations!!!!!!!!!!!! to you",user,". You have won",amount[score],". And now you are the new maha crorepati of this season.")
    print("This is your check of 7 crores. This seems to be a very proud moment for you and especially for your parents.")
    print("A very very best wishes for your upcoming future.")
    print("Audience, a very big aplause of round for",user)