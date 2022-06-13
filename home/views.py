from django.shortcuts import render
from django.db.models import Q
from blogapp.models import Page
from django.views.generic import ListView


class index(ListView): 
    model = Page
    queryset = Page.objects.filter(status=1).order_by('-created_on')
    template_name = ('home/main.html')

def search(request):
    query=request.GET['query']
    print('query: ', query)
    allPosts= Page.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, 'home/search_result.html', params)