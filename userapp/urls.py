from django.urls import path
from . import views

app_name='userapp'
urlpatterns = [
    path('accounts/signup', views.register, name='user-register'),
    #path('accounts/profile', views.user_update, name='user-update'),
    path('accounts/Profile', views.profile,name='user-update'),
    path('accounts/login', views.login_request, name='user-login'),
    path('accounts/logout', views.logout_request, name='user-logout'),
    #path('accounts/avatar/load', views.avatar_load, name='avatar-load'),
    ]    