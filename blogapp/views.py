from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.models import Page
from blogapp.forms import *
from userapp.models import *

###################### Home ###################### 

def index(request):
    return render(request, "blogapp/index.html")

def pages(request):
    return render(request, "blogapp/pages-index.html")

def about(request):
    return render(request, "blogapp/about.html")

###################### Blog pages ###################### 

class PagesListView(ListView):
    model = Page
    queryset = Page.objects.filter(status=1).order_by('-created_on')
    template_name = "blogapp/pages_list.html"


class PageDetailView(DetailView):
    model = Page
    template_name = "blogapp/page_detail.html"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    success_url = reverse_lazy('blogapp:pages-list')
    fields = ['title', 'subtitle', 'slug', 'body', 'status', 'page_image','author']


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    success_url = reverse_lazy('blogapp:pages-list')
    fields = ['title', 'subtitle', 'body', 'status', 'page_image']


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('blogapp:pages-list')


