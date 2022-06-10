from django.contrib import admin
from userapp.models import Avatar, Profile

class profileusers(admin.ModelAdmin):
    list_display = ('user', 'description', 'website_url','facebook_url','twitter_url','instagram_url')

admin.site.register(Avatar)
admin.site.register(Profile, profileusers)