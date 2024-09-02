from ch17_package.question import Question
from ch17_package.data import question_data
from ch17_package.quiz_brain import QuizBrain

question_list = []
def main():
    for item in question_data:
        question = Question(item['text'], item['answer'])
        question_list.append(question)
    
    quiz = QuizBrain(question_list)
    
    while quiz.still_has_questions():
        quiz.get_next_question()
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.show_score()}")

            



if __name__ == '__main__':
    main()