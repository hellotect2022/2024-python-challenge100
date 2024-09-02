class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def get_next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        your_answer = input(f"Q.{self.question_number}: {current_question.show_question()} (True/False)?: ")
        self.check_answer(your_answer,current_question.show_answer())
        print(f"Current score: {self.show_score()}")

    def check_answer(self,your_answer,real_answer):
        if your_answer.lower() == real_answer.lower():
            print("You got it right!")
            self.score += 1
        else :
            print("That's wrong")
        print(f"The correct answer was: {real_answer}")
    
    def show_score(self):
        return f"{self.score}/{self.question_number}"