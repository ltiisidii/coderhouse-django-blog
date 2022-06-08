from django.db import models
from django.contrib.auth.models import *
from django.utils import timezone

class Message(models.Model):
    user_origin = models.CharField(max_length=100)
    user_destination = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    text_message = models.CharField(max_length=250)