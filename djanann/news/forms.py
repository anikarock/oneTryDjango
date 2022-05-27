from django.forms import DateTimeInput, ModelForm, TextInput, Textarea 
from.models import Articels

class ArticelsForm(ModelForm):

    class Meta:
        model=Articels
        fields=['title','anons','full_text','date']

        widgets={
            'title': TextInput(attrs={
                'class':"form-control",'placeholder':'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class':"form-control",'placeholder':'Анонс'
            }),
            'full_text': Textarea(attrs={
                'class':"form-control",'placeholder':'Статья'
            }),
            'date':DateTimeInput(attrs={
                'class':"form-control",'placeholder':'Дата и время'
            })
        }