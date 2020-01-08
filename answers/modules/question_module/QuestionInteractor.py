from answers.modules.question_module.QuestionsGateway import QuestionsGateway


class QuestionInteractor:
    def __init__(self):
        self.questions = QuestionsGateway()

    def add_new_by_guest(question):
        return question

    def get_all(self):
        return self.questions.all()

    def get_by_id(self, question_id):
        return self.questions.by_id(question_id)


