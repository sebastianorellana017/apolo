from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomCreationForm(UserCreationForm):
    pass

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['user','title', 'categories','image','public']
        #fields = '__all__'

        def save(self, **kwargs):
            user = kwargs.pop('user')
            instance = super(ArticlesForm, self).save(**kwargs)
            instance.user = user
            instance.save()
            return instance
