from django.http import HttpResponse
from answers.question_module.QuestionInteractor import QuestionInteractor

class QuestionsPresenter:
    def index(request, name="жопулечка"):
        output = "<h2>User</h2><h3>name: {0}</h3>".format(name)
        return HttpResponse(output)

    def one_item(request, name):
        questions_interactor = QuestionInteractor()
        questions = questions_interactor.get_all()
        output = f"<h2>Подробка</h2><h3>name: {questions[0].author}</h3>"
        return HttpResponse(output)
