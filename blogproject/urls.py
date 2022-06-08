from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('blogapp.urls')),
    path('', include('userapp.urls')),
    path('', include('messageapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "blogproject.views.page_not_found_view"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)