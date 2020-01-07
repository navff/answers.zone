from answers.modules.question_module.Question import Question
from django.test import TestCase
from django.utils import timezone


class QuestionsTest(TestCase):

    def setUp(self):
        Question.objects.create(text="This is text of question",
                                author="unit_test",
                                date=timezone.now())

    def test_animals_can_speak(self):
        self.assertEqual(1, 1)



