# Generated by Django 4.2.5 on 2023-09-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='framework',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='frameworks',
            field=models.ManyToManyField(to='myApp.lenguajesframeworks'),
        ),
    ]
