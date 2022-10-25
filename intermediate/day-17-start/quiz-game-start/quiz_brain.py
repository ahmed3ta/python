class QuestionBrain:
    def __init__(self, q_list):
        self.question_numer = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        # print(self.question_numer)
        # print(len(self.question_list))
        return self.question_numer < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_numer]
        answer = self.question_list[self.question_numer].answer
        self.question_numer += 1
        user_input = input(f"Q{self.question_numer}: {current_question.text} (True/False)")
        self.check_answer(user_input, answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are Right!!")
            self.score += 1
        else:
            print("That is wrong")

        print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_numer}")



