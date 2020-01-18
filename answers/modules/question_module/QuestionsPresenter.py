from answers.modules.question_module.QuestionInteractor import QuestionInteractor
from answers.modules.question_module.QuestionAddForm import QuestionAddForm
from answers.modules.question_module.QuestionsMixins import QuestionPresenterMixin
from django.shortcuts import render, redirect
from django.views.generic import View


class QuestionsPresenter:

    class OneItem(QuestionPresenterMixin, View):

        def get(self, request, question_id):
            question = self.questions_interactor.get_by_id(question_id)
            template_data = {
                "question": question,
            }
            return render(request, "modules/question_module/views/question_one_item.html", template_data)

    class NotAnswered(QuestionPresenterMixin, View):

        def get(self, request):
            questions_page_view = self.questions_interactor.search(answered=False)
            template_data = {
                "title": "Неотвеченные вопросы",
                "questions": questions_page_view.content,
            }
            return render(request, "modules/question_module/views/question_list.html", template_data)

    class Answered(QuestionPresenterMixin, View):

        def get(self, request):
            questions_interactor = QuestionInteractor()
            questions_page_view = questions_interactor.search(answered=True)
            template_data = {
                "title": "Отвеченные вопросы",
                "questions": questions_page_view.content,
            }
            return render(request, "modules/question_module/views/question_list.html", template_data)

    class FormAdd(QuestionPresenterMixin, View):
        def get(self, request):
            form = QuestionAddForm()
            template_data = {
                'title': 'Добавление нового вопроса',
                'form': form
            }
            return render(request,
                          "modules/question_module/views/question_add_item.html",
                          template_data)

        def post(self, request):
            form = QuestionAddForm(request.POST)
            if form.is_valid():
                result = form.save()
                return redirect('question_detail_url', result.id)
            else:
                template_data = {
                    'title': 'Добавление нового вопроса',
                    'form': form
                }
                return render(request,
                              "modules/question_module/views/question_add_item.html",
                              template_data)

    class FormUpdate(QuestionPresenterMixin, View):
        def get(self, request, question_id):
            question = self.questions_interactor.get_by_id(question_id)
            form = QuestionAddForm(instance=question)
            template_data = {
                'title': f'Обновление вопроса | {question.title}',
                'form': form,
                'question': question
            }
            return render(request,
                          "modules/question_module/views/question_update_item.html",
                          template_data)



