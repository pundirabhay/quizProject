class QuizBrain:

    def __init__(self, q_lsit):
        self.question_number = 0
        self.score = 1
        self.question_list = q_lsit


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (Ture/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("hurry! You Got the right answer😍")

        else:
            print("sorry! you got the wrong answer")
        print(f"The Correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



