class QuizController:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def has_more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return question

    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number - 1]
        is_correct = user_answer.lower() == current_question.answer.lower()
        return is_correct, current_question.explanation
