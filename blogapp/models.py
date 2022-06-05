from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Page(models.Model):
    # Titulo, subtitulo, cuerpo, autor, fecha y una imagen (minimo,obligatorio)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='page_image/%Y/%m/%d/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title