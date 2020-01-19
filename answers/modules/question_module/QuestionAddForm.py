from django import forms
from .Question import Question
from .QuestionInteractor import QuestionInteractor


class QuestionAddForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = {'title', 'text', 'author'}

    field_order = ['title', 'text', 'author']

    title = forms.CharField(
        max_length=100,
        label='Заголовок вопроса',
        error_messages={'required': 'Заголовок не должен быть пустым'},
        widget=forms.TextInput(attrs={'placeholder': 'Суть вопроса одним предложением',
                                      'class': 'form-control mb-4'})
    )

    text = forms.CharField(
        label='Полный текст вопроса',
        widget=forms.Textarea(attrs={'class': 'form-control mb-4',
                                     'placeholder': 'Всё, о чём вы мечтали спросить'})

    )

    author = forms.CharField(max_length=50,
                             label='Ваше имя',
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control mb-4',
                                 'placeholder': 'Напишите, как вас зовут'
                             }))

