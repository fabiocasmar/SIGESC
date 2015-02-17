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
        
class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        fields= '__all__'
        
class ComunidadForm(ModelForm):
    class Meta:
        model = Comunidad
        fields= '__all__'        
        
class CaracteristicasProyectoForm(ModelForm):
    class Meta:
        model = CaracteristicasProyecto
        fields = '__all__'
        
class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ProponenteForm(ModelForm):
    class Meta:
        model = Proponente
        fields = '__all__'
            
class SedeForm(ModelForm):
    class Meta:
        model = Sede
        fields = '__all__'

class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
            
