from django.urls import path
from . import views

app_name='blogapp'
urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about, name="About"),
    path('pages/', views.pages, name="Pages"),
]    