from .Question import Question
from answers.common.SettingsAdapter import SettingsAdapter
import math

class QuestionsGateway:

    def all(self):
        questions_all = Question.objects.all()
        return list(questions_all)


    def search(self, word, date_start, date_end, page):
        query = Question.objects.all()

        if word:
            query = query.filter(title__contains=word) \
                    | query.filter(author__contains=word) \
                    | query.filter(text__contains=word)

        query = query.filter(date__range=[date_start, date_end])

        start = page*SettingsAdapter.ITEMS_PER_PAGE()
        end = start + SettingsAdapter.ITEMS_PER_PAGE()
        total_objects_count = query.count()
        total_pages = math.ceil(total_objects_count /
                                SettingsAdapter.ITEMS_PER_PAGE())
        # TODO: сформировать нормальный запрос
        # https://habr.com/ru/post/175727/“““
        query = query[start:end]


    def by_id(self, question_id):
        question = Question.objects.get(id=question_id)
        return question

    def add_new(self, question):
        q = Question(title=question.title,
                     text=question.text,
                     date=question.date,
                     author=question.author)
        return q.save()
