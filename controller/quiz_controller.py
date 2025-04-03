class QuizController:
    def __init__(self, questions):
        self.questions = questions
        self.question_index = 0
        self.score = 0

    def has_more_questions(self):
        return self.question_index < len(self.questions)

    def next_question(self):
        question = self.questions[self.question_index]
        self.question_index += 1
        return question

    def check_answer(self, answer):
        current_question = self.questions[self.question_index - 1]
        return answer.lower() == current_question.answer.lower(), current_question.explanation