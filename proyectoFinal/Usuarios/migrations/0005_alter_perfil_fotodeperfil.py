# Generated by Django 4.1.3 on 2022-12-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_remove_perfil_contraseña_remove_perfil_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fotoDePerfil',
            field=models.ImageField(default='Usuarios/media/fotosDePerfil/apolo.jpeg', upload_to='Usuarios/media/fotosDePerfil'),
        ),
    ]
