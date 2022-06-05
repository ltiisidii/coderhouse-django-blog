from django import forms
from django.forms import ModelForm
from blogapp.models import Page

class PageForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    code = forms.IntegerField(label='Camada')