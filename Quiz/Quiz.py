from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if quiz.score < quiz.question_number:
    print("Unfortunately, you have not completed the quiz, please try again")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")
else:
    print("You completed the quiz, congratulations!!!")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


