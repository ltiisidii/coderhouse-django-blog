from django import forms
from django.forms import ModelForm
from userapp.models import Avatar, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='username', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    description = forms.CharField(label='Bio', min_length=3)
    website_url = forms.CharField(label='Website', min_length=3)
    facebook_url = forms.CharField(label='Facebook Page', min_length=3)
    twitter_url = forms.CharField(label='Twitter Profile', min_length=3)
    instagram_url = forms.CharField(label='Instagram Profile', min_length=3)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'description', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'password1', 'password2',]
        help_texts = {k: "" for k in fields}


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )
      
class SearchUser(forms.Form):
    usuario = forms.CharField(max_length=60, label='Name of User')