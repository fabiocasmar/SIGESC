from django.forms import ModelForm
from entidades.models import *

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        
class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields= '__all__'
        
class ProyectoForm(ModelForm):
        class Meta:
            model = Proyecto
            fields = '__all__'

class ProponenteForm(ModelForm):
        class Meta:
            model = Proponente
            fields = '__all__'