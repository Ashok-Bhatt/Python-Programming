from os import system
from time import sleep
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"],question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("")

sleep(1)
system("cls")

print(f"Quiz Over! \nYour final Score: {quiz.score}/12")