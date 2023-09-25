#esta permite hacer el proceo de un CRUD


from rest_framework import viewsets

from .models import Publicacion
from .serializer import PublicacionSerializer

from .models import Proyectos
from .serializer import ProyectosSerializer

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer


class ProyectosViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer