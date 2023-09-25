from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import Categoria, Publicacion, LenguajesFrameworks, Proyectos
from django.contrib.auth.models import User

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)



admin.site.unregister(User)  # Desregistrando el modelo User predeterminado
admin.site.register(User, CustomUserAdmin)  # Registrando el modelo User personalizado

admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(LenguajesFrameworks)
admin.site.register(Proyectos)
