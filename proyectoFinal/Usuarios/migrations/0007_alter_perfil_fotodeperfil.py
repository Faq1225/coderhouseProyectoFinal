# Generated by Django 4.1.3 on 2022-12-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_alter_perfil_fotodeperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fotoDePerfil',
            field=models.ImageField(default='default.jpg', upload_to='Usuarios/media/fotosDePerfil'),
        ),
    ]
