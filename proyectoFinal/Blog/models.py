from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.urls import *
from PIL import Image

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=80, unique = True)
    slug = models.SlugField(max_length=80, unique= True)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_articulos')
    fechaDelPosteo = models.DateTimeField(auto_now_add=True)
    fechaDelEdit = models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ['-fechaDelPosteo']
    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('articuloDetalle', kwargs={'slug': self.slug})

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE,related_name='comentarios')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comentador')
    contenido = models.TextField(max_length = 256)
    fechaDelComentario = models.DateTimeField(default=datetime.now)
    class Meta:
        ordering = ['-fechaDelComentario']
    def __str__(self):
        return 'Comentario {} de {}'.format(self.contenido, self.usuario)