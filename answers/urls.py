from django.urls import path
from answers.modules.question_module.QuestionsPresenter import *

urlpatterns = [
    path('', QuestionsPresenter.NotAnswered.as_view(), name='list_questions_url'),
    path('/answered', QuestionsPresenter.Answered.as_view(), name='answered_questions_url'),
    path('/add', QuestionsPresenter.FormAdd.as_view(), name='question_add_url'),
    path('/<str:question_id>', QuestionsPresenter.OneItem.as_view(), name='question_detail_url'),
    path('/update/<str:question_id>', QuestionsPresenter.FormUpdate.as_view(), name='question_update_url'),
]
