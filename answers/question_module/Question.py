from django.db import models
import uuid


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, default='')
    text = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author + ' — ' + self.text[:30]

