from answers.modules.question_module.QuestionInteractor import QuestionInteractor
from django.template.response import TemplateResponse


class QuestionsPresenter:
    def one_item(request, question_id):
        questions_interactor = QuestionInteractor()
        question = questions_interactor.get_by_id(question_id)
        template_data = {
            "question": question,
        }

        return TemplateResponse(request, "modules/question_module/views/question_one_item.html", context=template_data)

    def all(request):
        questions_interactor = QuestionInteractor()
        questions = questions_interactor.get_all()
        template_data = {
            "title": "Список вопросов",
            "questions": questions,
        }

        return TemplateResponse(request, "modules/question_module/views/question_list.html", context=template_data)

