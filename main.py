from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    new_question = Question(question.get("question"), question.get("correct_answer"))
    question_bank.append(new_question)
Quiz_Game = QuizBrain(question_bank)
while Quiz_Game.still_has_questions():
    Quiz_Game.next_question()
print("You completed the Quiz Game!")
print(f"Your final score is: {Quiz_Game.score}.")
Quiz_Game.score_check(Quiz_Game.score)

