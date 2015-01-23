from django.forms import ModelForm
from entidades.models import *

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        
    def clean(self):
        super(EstudianteForm, self).clean()

        data = {}

        for key, value in self.cleaned_data.items():
            data[key] = value

        return self.cleaned_data