from django.urls import path
from . import views

app_name='messageapp'
urlpatterns = [
    path('messages', views.messages, name='list-messages'),
    path('messages/send',views.send_messages, name="send_messages"),
    ]    