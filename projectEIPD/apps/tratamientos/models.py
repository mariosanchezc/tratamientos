from django.contrib.auth.models import User
from django.db import models

class Tratamiento(models.Model):

    PERFILADO = 'perfilado'
    DECISIONES_AUTOMATIZADAS = 'decisiones_automatizadas'

    TIPO_TRATAMIENTO = (
        (PERFILADO, 'perfilado'),
        (DECISIONES_AUTOMATIZADAS, 'decisiones_automatizadas')
    )
    usuario_tratamiento = models.ManyToManyField(
        User, through='UsuarioTratamiento'
    )
    name = models.CharField(max_length=200)
    tipo = models.CharField(
        max_length=60,
        choices=TIPO_TRATAMIENTO,
        default=PERFILADO
    )

    def __str__(self):
        return self.name

class UsuarioTratamiento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tratamiento.name} - {self.user.username}'

class Pregunta(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.description[:50]} - {self.tratamiento.name}'

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class UsuarioRespuesta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.respuesta.pk} - {self.user.username}'






