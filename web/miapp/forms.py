from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomCreationForm(UserCreationForm):
    pass

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        #fields = ['title', 'categories','image','public']
        fields = '__all__'
