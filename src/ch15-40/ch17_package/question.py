class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
    def show_question(self):
        return self.question
    def show_answer(self):
        return self.answer