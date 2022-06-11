from django.contrib import admin
from userapp.models import Profile

class profileusers(admin.ModelAdmin):
    list_display = ('user', 'bio', 'url')

admin.site.register(Profile, profileusers)