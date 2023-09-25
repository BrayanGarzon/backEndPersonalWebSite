
#nos permite serializar el modelo enviar info por http

from rest_framework import serializers

from .models import Publicacion
from .models import Proyectos


class PublicacionSerializer(serializers.ModelSerializer):
    # Define campos para mostrar los nombres de la categoría y el framework
    categoria_nombre = serializers.CharField(source='categoria.nombre')
    frameworks_nombre = serializers.StringRelatedField(many=True, source='frameworks')  # Usamos frameworks en lugar de framework

    class Meta:
        model = Publicacion
        fields = ('id', 'titulo', 'descripcion', 'imagen', 'fechaPublicacn','url', 'categoria_nombre', 'frameworks_nombre')


class ProyectosSerializer(serializers.ModelSerializer):
    frameworks_nombre = serializers.StringRelatedField(many=True, source='frameworks')  # Usamos frameworks
    

    class Meta:
        model = Proyectos
        fields = ('id', 'titulo', 'descripcion', 'imagen', 'fechaPublicacn', 'url', 'frameworks_nombre')