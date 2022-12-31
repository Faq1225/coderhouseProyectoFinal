from django.contrib import admin
from .models import *

# Register your models here.
class perfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fotoDePerfil')
    search_fields = ('usuario', 'fotoDePerfil')

class CanalMensajeInline(admin.TabularInline):
    model = CanalMensaje
    extra = 1

class CanalUsuarioInline(admin.TabularInline):
    model = CanalUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalMensajeInline, CanalUsuarioInline]

    class Meta:
        model = Canal

admin.site.register(Perfil, perfilAdmin)
admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)