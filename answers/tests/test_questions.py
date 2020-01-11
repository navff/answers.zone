from answers.modules.question_module.Question import Question
from django.test import TestCase
from django.utils import timezone
from answers.modules.question_module.QuestionInteractor import  QuestionInteractor


class QuestionsTest(TestCase):

    def __init__(self, *args, **kwargs):
        super(QuestionsTest, self).__init__(*args, **kwargs)
        self.interactor = QuestionInteractor()

    def setUp(self):
        Question.objects.create(text="This is text of question",
                                author="unit_test",
                                date=timezone.now(),
                                title="This is title")

    def test_get_all(self):
        result = self.interactor.get_all()
        self.assertTrue(len(result)>0)

    def test_get_by_id(self):
        question_from_db = Question.objects.first()
        result = self.interactor.get_by_id(question_from_db.id)
        self.assertTrue(result.id == question_from_db.id)


    def test_add_new_by_guest(self):
        result = self.interactor.add_new_by_guest(
            question=Question(
                author='Vova',
                text='This is text',
                title='This is title'
            )
        )
        self.assertTrue(result.author=='Vova')

    def test_search_by_name(self):
        result = self.interactor.search(word='This is title')
        self.assertEquals(first="This is title", second=result.objects[0].title)


