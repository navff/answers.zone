from .Question import Question
from answers.common import SettingsAdapter
import math
from answers.common.PageView import PageView


class QuestionsGateway:

    def all(self):
        questions_all = Question.objects.all()
        return list(questions_all)


    def search(self, word, date_start, date_end, answered, page):
        query = Question.objects.all()

        if answered:
            query = query.filter(answers__isnull=False)

        if answered==False:
            query = query.filter(answers__isnull=True)

        if word:
            query = query.filter(title__contains=word) \
                    | query.filter(author__contains=word) \
                    | query.filter(text__contains=word)

        query = query.filter(date__range=[date_start, date_end])

        start = (page-1)*SettingsAdapter.ITEMS_PER_PAGE
        end = start + SettingsAdapter.ITEMS_PER_PAGE
        total_objects_count = query.count()
        total_pages = math.ceil(total_objects_count /
                                SettingsAdapter.ITEMS_PER_PAGE)

        query = query.only('title', 'author', 'date')[start:end]
        return PageView(content=query, current_page=page,
                        total_pages=total_pages,
                        total_objects_count=total_objects_count)


    def by_id(self, question_id):
        question = Question.objects.get(id=question_id)
        return question


    def add_new(self, question):
        q = Question(title=question.title,
                     text=question.text,
                     date=question.date,
                     author=question.author)
        q.save()
        return q
