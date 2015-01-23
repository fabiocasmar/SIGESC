from django.shortcuts import render
from entidades.forms import *
from entidades.models import *
from entidades.models import Estudiante
from django.core import serializers

def estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        context = {'msj': "Estudiante creado con exito.",
                    'est': form}
        if form.is_valid():
            est = form.save()
            return render(request, 'index.html', context )
            
        else:
            context = {'msj': 'error'}
            return render(request, 'estudiantes.html', context)
    else:
        est = Estudiante.objects.all()
        context = {'est': est,
               'form': EstudianteForm()}
    return render(request, 'estudiantes.html',context)

def estudiantesDetalles(request, ced):
     
    est = Estudiante.objects.get(pk = '08-1383')
    if request.method == 'POST':
        mensaje= "estudiante eliminado con exito"
        est.delete()
        context = {'msj': mensaje}
        return render(request, 'index.html', context)
    print(est)
    context = {'est': est}
    return render(request, 'estudiante.html', context )

def tutores(request):
    context = {'msj':"Aqui va la vista inicial de tutor."}
    return render(request, 'tutores.html',context)

def cursa(request):
    context = {'msj':"Aqui va la vista inicial de cursa."}
    return render(request, 'cursa.html',context)

def proyectos(request):
    context = {'msj':"Aqui va la vista inicial de proyecta."}
    return render(request, 'proyectos.html',context)