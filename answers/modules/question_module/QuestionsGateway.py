from .Question import Question


class QuestionsGateway:

    # @entity(Question)
    def all(self):
        questions_all = Question.objects.all()
        return list(questions_all)

    def by_id(self, question_id):
        question = Question.objects.get(id=question_id)
        return question
