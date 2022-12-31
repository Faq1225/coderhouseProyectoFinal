from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

#######

@receiver(post_save, sender=User)
def crearPerfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardarPerfil(sender, instance, **kwargs):
    instance.perfil.save()