from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
quiz_is_on = True

question_Bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text= question_text, q_answer=question_answer)
    question_Bank.append(new_question)

quiz = QuizBrain(question_Bank)
while quiz.still_has_question():
   quiz.next_question()






