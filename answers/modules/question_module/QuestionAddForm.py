from django import forms
from .Question import Question
from .QuestionInteractor import QuestionInteractor


class QuestionAddForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['author', 'title', 'text']

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control mb-4',
                       'placeholder': 'Ваше имя'}),
            'title': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-4'})
        }
        labels = {
            'author': 'Автор',
            'title': 'Заголовок одним предложением',
            'text': 'Полный текст вопроса'
        }

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


