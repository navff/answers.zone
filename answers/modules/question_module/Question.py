from django.db import models
from django.shortcuts import reverse
import uuid


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, default='')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('question_detail_url', kwargs={'question_id': self.id})

    def get_update_url(self):
        return reverse('question_update_url', kwargs={'question_id': self.id})

    def get_delete_url(self):
        return reverse('question_delete_url', kwargs={'question_id': self.id})

    def __str__(self):
        return self.author + ' — ' + self.title[:30]

