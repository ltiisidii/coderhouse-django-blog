from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.text import slugify
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
    fields = ['title', 'subtitle', 'body', 'status', 'page_image']
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blogapp:pages-list")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'body', 'status', 'page_image']
    #success_url = reverse_lazy('blogapp:pages-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blogapp:pages-list")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)    


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    #success_url = reverse_lazy('blogapp:pages-list')
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("blogapp:pages-list")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

