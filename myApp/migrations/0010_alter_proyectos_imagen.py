# Generated by Django 4.2.5 on 2023-09-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_remove_proyectos_imagenes_proyectos_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(default='/media/imagenes/imagen-no-disponible01601774755.jpg', upload_to='imagenes/'),
        ),
    ]
