from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # Otros campos personalizados que desees agregar

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categoría"
    
class LenguajesFrameworks(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Lenguajes / Frameworks"


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=250)
    imagen = models.ImageField(upload_to='imagenes/')
    fechaPublicacn = models.DateField(default=timezone.now)
    url = models.URLField(max_length=200, blank=True, null=True)


    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    frameworks = models.ManyToManyField(LenguajesFrameworks)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicación"



class Proyectos(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=250)
    imagen = models.ImageField(upload_to='imagenes/', default='/media/imagenes/imagen-no-disponible01601774755.jpg')
    fechaPublicacn = models.DateField(default=timezone.now)
    
   

    url = models.URLField(max_length=200, blank=True, null=True)

    frameworks = models.ManyToManyField(LenguajesFrameworks)


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Proyectos"