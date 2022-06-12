from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Page(models.Model):
    # Titulo, subtitulo, cuerpo, autor, fecha y una imagen (minimo,obligatorio)
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    updated_on = models.DateTimeField(auto_now= True)
    body = RichTextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    page_image = models.ImageField(upload_to='page_image/%Y/%m/%d/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} - {self.author} - {self.created_on} '