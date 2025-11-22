from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for line in question_data:
    question = Question(line["question"], line["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}.")