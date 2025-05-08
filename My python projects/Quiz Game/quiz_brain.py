class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number].question
        answer = self.question_list[self.question_number].answer
        user_Answer = input(f"Q.{self.question_number+1}. {question} (True/False): ")
        self.check_answer(user_Answer, answer)
        print(f"Current Score: {self.score}/12")
        self.question_number = self.question_number + 1

    def still_has_questions(self):
        return not(self.question_number == len(self.question_list))
    
    def check_answer(self, user_Answer, correct_Answer):
        if (user_Answer.title()==correct_Answer):
            print("Sahi jawab! I think you can do this the whole day.")
            self.score = self.score+1
        else:
            print("Ooh, Wrong Answer! Koi baat nahi agala ho jayega")
            print(f"Correct Answer: {correct_Answer}")