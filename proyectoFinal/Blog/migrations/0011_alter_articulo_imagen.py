# Generated by Django 4.1.3 on 2022-12-27 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='apolo.jpeg', upload_to='Blog/media/articuloImagenes/'),
        ),
    ]
