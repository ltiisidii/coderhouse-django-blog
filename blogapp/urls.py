from django.urls import path
from . import views

app_name='blogapp'
urlpatterns = [
    path('about/', views.about, name="About"),
    path('pages/', views.PagesListView.as_view(), name='pages-list'),
    path('page/add', views.PageCreateView.as_view(), name='page-add'),
    path('page/<int:pk>/detail', views.PageDetailView.as_view(), name='page-detail'),
    path('page/<int:pk>/update', views.PageUpdateView.as_view(), name='page-update'),
    path('page/<int:pk>/delete', views.PageDeleteView.as_view(), name='page-delete'),
    ]    