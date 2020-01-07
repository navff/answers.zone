from django.http import HttpResponse
from answers.question_module.QuestionInteractor import QuestionInteractor
from django.template.response import TemplateResponse


class QuestionsPresenter:
    def index(request, name="жопулечка"):
        output = "<h2>User</h2><h3>name: {0}</h3>".format(name)
        return HttpResponse(output)

    def one_item(request, name):
        questions_interactor = QuestionInteractor()
        questions = questions_interactor.get_all()
        template_data = {
            "title": "Список вопросов",
            "questions": questions,
        }

        return TemplateResponse(request, "question_module/views/question_list.html", context=template_data)

