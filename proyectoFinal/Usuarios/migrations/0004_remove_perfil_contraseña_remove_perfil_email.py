# Generated by Django 4.1.3 on 2022-12-23 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_rename_usuario_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='email',
        ),
    ]
