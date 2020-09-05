from django.shortcuts import render
from apps.tratamientos.models import Tratamiento


def tratamientos_lista(request, *args, **kwargs):
    tratamientos = Tratamiento.objects.all()
    context = {
        'tratamientos': tratamientos,
        'descripcion': 'Descripcion'
    }
    return render(request, template_name='index.html', context=context)