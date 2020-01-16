from django import forms


class QuestionAddForm(forms.Form):
    title = forms.TextInput()
    text = forms.Textarea()
    author = forms.TextInput()

