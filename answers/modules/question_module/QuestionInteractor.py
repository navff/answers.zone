from answers.modules.question_module.QuestionsGateway import QuestionsGateway
from django.utils.timezone import timedelta, now


class QuestionInteractor:
    def __init__(self):
        self.questions = QuestionsGateway()

    def add(self, question):
        result = self.questions.add_new(question)
        return result

    def get_all(self):
        return self.questions.all()

    def get_by_id(self, question_id):
        return self.questions.by_id(question_id)

    def search(self, word=None, date_start=None, date_end=None, answered=None, page=1):
        if not date_start:
            date_start = now() + timedelta(days=-365)

        if not date_end:
            date_end = now() + timedelta(days=365)

        result = self.questions.search(word, date_start, date_end, answered, page)
        return result

    def delete(self, question_id):
        self.questions.delete(question_id)


