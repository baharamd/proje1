from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_q=Question(question_text,question_answer)
    question_bank.append(new_q)
print(question_bank)
quiz=QuizBrain(question_bank)
print( quiz.score)
print(quiz.question_number)
# quiz.next_question()
# quiz.still_has_questions()

while quiz.still_has_questions():
    quiz.next_question()



# print(new_q.question_number) #not true cause new_q comes from Question class which
# has no attribute question.number!!!!!!!!!!!!!!!!!!!

