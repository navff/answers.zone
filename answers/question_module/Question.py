from django.db import models


class Question(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author + ' — ' + self.text[:30]

