from django.shortcuts import render
from django.db.models import Q

from blogapp.models import Page


def index(request):
    return render(request, "home/main.html", )


def search(request):
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        pages = Page.objects.filter(query)
        context_dict.update({
            'pages': pages,
            'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )