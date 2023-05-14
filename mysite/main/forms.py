from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {'name', 'text', 'email'}
        labels = {
            'name': 'Ваше имя',
            'text': 'Пишите здесь',
            'email': 'Ваша почта для связи'
        }
