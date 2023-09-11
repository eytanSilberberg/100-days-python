class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_q_num = self.question_number
        curr_question = self.question_list[curr_q_num]
        self.question_number += 1
        user_answer = input(f' Q{self.question_number}. {curr_question.text} (True/False)').lower()
        self.check_answer(user_answer, curr_question.answer.lower())

    def check_answer(self, user_answer, q_answer):
        if user_answer == q_answer:
            self.score += 1
            print('You got it right ')
        else:
            print('You got it wrong')
        print(f'{self.score}/{self.question_number}')
