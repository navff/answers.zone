from .Question import Question


class QuestionsGateway:

    # @entity(Question)
    def all(self):
        questions_all = Question.objects.filter(text__contains='a')\
            .filter(text__contains='b')
        return list(questions_all)
