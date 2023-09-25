from rest_framework import routers

from .viewsets import PublicacionViewSet, ProyectosViewSet

router = routers.SimpleRouter()
router.register('Publicacion', PublicacionViewSet)
router.register('Proyectos', ProyectosViewSet)



urlpatterns = router.urls


