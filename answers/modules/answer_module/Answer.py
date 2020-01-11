from django.db import models
import uuid
from answers.modules.question_module.Question import Question


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question,
                      on_delete=models.CASCADE,
                      null=False,)
    text = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=50)

