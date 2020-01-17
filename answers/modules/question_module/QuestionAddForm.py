from django import forms
from .Question import Question
from .QuestionInteractor import QuestionInteractor


class QuestionAddForm(forms.Form):
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


    def save(self):
        if not self.is_valid():
            pass

        interactor = QuestionInteractor()
        new_question = interactor.add(Question(
            author=self.cleaned_data['author'],
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
        ))
        return new_question
