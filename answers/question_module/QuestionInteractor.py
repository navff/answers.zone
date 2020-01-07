from answers.question_module.QuestionsGateway import QuestionsGateway


class QuestionInteractor:
    def __init__(self):
        self.questions = QuestionsGateway()

   # @boundary_method
    def add_new_by_guest(question):
        return question

    def get_all(self):
        return self.questions.all()

