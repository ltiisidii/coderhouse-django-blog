from django import forms
from django.forms import ModelForm
from blogapp.models import Page
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

#class PageForm(forms.Form):
#    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
#    code = forms.IntegerField(label='Camada')

class CrearPost(forms.ModelForm):
    
    body = RichTextFormField(required=True)

    class Meta:
        model = Page
        fields = ['title','subtitle','body', 'page_image']
        help_texts = {k:'' for k in fields }

class PostSearch(forms.Form):
    title = forms.CharField(max_length=60, label='Titulo del post')