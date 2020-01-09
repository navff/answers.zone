from .Question import Question


class QuestionsGateway:

    # @entity(Question)
    def all(self):
        questions_all = Question.objects.all()
        return list(questions_all)

    def by_id(self, question_id):
        question = Question.objects.get(id=question_id)
        return question

    def add_new(self, question):
        q = Question(title=question.title,
                     text=question.text,
                     date=question.date,
                     author=question.author)
        return q.save()
