from answers.modules.question_module.Question import Question
from answers.modules.answer_module.Answer import Answer
from django.test import TestCase
from django.utils import timezone
from answers.modules.question_module.QuestionInteractor import  QuestionInteractor
from answers.modules.question_module.QuestionAddForm import QuestionAddForm


class QuestionsTest(TestCase):

    def __init__(self, *args, **kwargs):
        super(QuestionsTest, self).__init__(*args, **kwargs)
        self.interactor = QuestionInteractor()
        self._question = None
        self._answer = None

    def setUp(self):
        self._question = Question.objects.create(text="This is text of question",
                                                 author="unit_test",
                                                 date=timezone.now(),
                                                 title="This is title")

        self._answer = Answer.objects.create(author='author_value',
                                             text='text_value',
                                             date=timezone.now(),
                                             question=self._question)

        Question.objects.create(text="Текст второго вопроса",
                                author="автор 2",
                                date=timezone.now(),
                                title="Заголовок 2")

        Question.objects.create(text="Текст третьего вопроса",
                                author="автор 3",
                                date=timezone.now(),
                                title="Заголовок 3")

        Question.objects.create(text="Текст четвёртого вопроса",
                                author="автор 4",
                                date=timezone.now(),
                                title="Заголовок 4")

    # model test
    # -------------------------------------------------
    def test_to_string(self):
        question = Question(title="Title", text="This is text", author="author")
        self.assertEquals(question.author + ' — ' + question.title, str(question))

    # -------------------------------------------------
    # interactor test
    def test_get_all(self):
        result = self.interactor.get_all()
        self.assertTrue(len(result)>0)

    def test_get_by_id(self):
        question_from_db = Question.objects.first()
        result = self.interactor.get_by_id(question_from_db.id)
        self.assertTrue(result.id == question_from_db.id)

    def test_add(self):
        result = self.interactor.add(
            question=Question(
                author='Vova',
                text='This is text',
                title='This is title'
            )
        )
        self.assertTrue(result.author == 'Vova')

    def test_search_by_name(self):
        result = self.interactor.search(word=self._question.title)
        self.assertEquals(first="This is title", second=result.content[0].title)

    def test_search_by_title_page2(self):
        result = self.interactor.search(word='Заголовок', page=2)
        self.assertTrue(result.total_objects_count == 3)

    def test_search_answered(self):
        result = self.interactor.search(answered=True)
        self.assertTrue(result.total_objects_count == 1)

    # -------------------------------------------------------
    # View tests
    def test_list_page(self):
        resp = self.client.get('/q')
        self.assertEqual(resp.status_code, 200)

    def test_one_question_page(self):
        resp = self.client.get(f'/q/{self._question.id}')
        self.assertEqual(resp.status_code, 200)

    def test_answered_list_page(self):
        resp = self.client.get(f'/q/answered')
        self.assertEqual(resp.status_code, 200)

    def test_add_question_page(self):
        resp = self.client.get(f'/q/add')
        self.assertEqual(resp.status_code, 200)

    # -------------------------------------------------------
    # Forms tests
    def test_add_question_form(self):
        d = {'title': 'this is title',
             'text': 'this is text',
             'author': 'this is author'}
        form = QuestionAddForm(d)
        result = form.save()

        self.assertTrue(form.is_bound)
        self.assertTrue(result.id)


