from django.contrib import admin
from messageapp.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','user_origin', 'user_destination','pub_date', 'text_message')
    #list_filter = ("user_origin","user_destination")
    search_fields = ['user_origin', 'user_destination', 'text_message']
    #prepopulated_fields = {'user_origin': ('text_message',)}
admin.site.register(Message, MessageAdmin)
