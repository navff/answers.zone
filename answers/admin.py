from django.contrib import admin
from .models import Question
from .models import Answer
from django.db import models


admin.site.register(Question)
#admin.site.register(Answer)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    raw_id_fields = ('question',)

