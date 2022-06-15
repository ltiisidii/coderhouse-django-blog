from django import forms
from django.forms import ModelForm
from blogapp.models import Page
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class CreatePost(forms.ModelForm):
    
    body = RichTextField()

    class Meta:
        model = Page
        fields = ['title','subtitle','slug','body', 'page_image','author']
        #help_texts = {k:'' for k in fields }

class PostSearch(forms.Form):
    title = forms.CharField(max_length=60, label='Titulo del post')