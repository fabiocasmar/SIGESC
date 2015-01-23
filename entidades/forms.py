from django.forms import ModelForm
from entidades.models import *

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['USBID', 'cedula', 'nombre', 'apellido',
                  'sede', 'email', 'sexo', 'telefono', 'direccion']
