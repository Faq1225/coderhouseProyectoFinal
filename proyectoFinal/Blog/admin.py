from django.contrib import admin
from .models import *

# Register your models here.
class articuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug','fechaDelPosteo')
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}

class comentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'articulo', 'usuario', 'fechaDelComentario')
    search_fields = ('usuario', 'contenido')

admin.site.register(Articulo, articuloAdmin)
admin.site.register(Comentario, comentarioAdmin)


