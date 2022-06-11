from django.contrib import admin
from .models import Page

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')

admin.site.register(Page, PostAdmin)