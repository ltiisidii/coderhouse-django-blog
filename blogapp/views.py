from django.shortcuts import render

###################### Home ###################### 

def index(request):
    return render(request, "blogapp/index.html")

def pages(request):
    return render(request, "blogApp/pages-index.html")

def about(request):
    return render(request, "blogApp/about.html")