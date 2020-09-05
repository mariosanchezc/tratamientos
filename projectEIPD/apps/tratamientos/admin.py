from apps.tratamientos.models import (
    Tratamiento, Pregunta, Respuesta,
    UsuarioRespuesta, UsuarioTratamiento,
)
from django.contrib import admin

# Register your models here.
admin.site.register(Tratamiento)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(UsuarioRespuesta)
admin.site.register(UsuarioTratamiento)