from django import forms

class MessageForm(forms.Form):
    user_origin = forms.CharField(max_length=50)
    user_destination = forms.CharField(max_length=50)
    text_message = forms.CharField(max_length=250)