from django.shortcuts import render, redirect
from messageapp.models import Message
from messageapp.forms import MessageForm
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def messages(request):
    sent_messages = Message.objects.filter(user_origin = request.user.username)
    received_messages = Message.objects.filter(user_destination = request.user.username)
    return render(request,'messageapp/list_messages.html',{"sent_messages":sent_messages,"received_messages":received_messages})

@login_required
def send_messages(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            user_origin = User.objects.filter(username=information['user_origin'])
            user_destination = User.objects.filter(username=information['user_destination'])
            if(user_origin.count() > 0 and user_destination.count() > 0):
                message = Message(user_origin=information["user_origin"],user_destination=information["user_destination"],text_message=information["text_message"])
                message.save()
            else:
                form = MessageForm()
                return render(request,'messageapp/send_message.html',{'form':form,"message":"No existe alguno de lo usuarios ingresados"})
            
        return redirect ('messageapp:list-messages')
      
    else:
        form = MessageForm()
        return render(request,'messageapp/send_message.html',{'form':form})