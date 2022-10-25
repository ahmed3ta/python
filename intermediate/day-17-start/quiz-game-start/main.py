from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain
question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))
# print(question_bank)

question_process = QuestionBrain(question_bank)
while question_process.still_has_question():
    question_process.next_question()
    # print("over")
print("-------------------------------------------------")
print("You have completed the Quiz")
print(f"Your final score is {question_process.score}/{len(question_bank)}")
