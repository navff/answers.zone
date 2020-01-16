from answers.modules.question_module.QuestionInteractor import QuestionInteractor
from answers.modules.question_module.QuestionAddForm import QuestionAddForm
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
        questions_page_view = questions_interactor.search(answered=False)
        template_data = {
            "title": "Неотвеченные вопросы",
            "questions": questions_page_view.content,
        }
        return TemplateResponse(request, "modules/question_module/views/question_list.html", context=template_data)

    def answered(request):
        questions_interactor = QuestionInteractor()
        questions_page_view = questions_interactor.search(answered=True)
        template_data = {
            "title": "Отвеченные вопросы",
            "questions": questions_page_view.content,
        }
        return TemplateResponse(request, "modules/question_module/views/question_list.html", context=template_data)

    def add(request):
        form = QuestionAddForm()
        template_data = {
            'title': 'Добавление нового вопроса',
            'form': form
        }
        return TemplateResponse(request,
                                "modules/question_module/views/question_add_item.html",
                                context=template_data)

