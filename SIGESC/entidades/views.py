from django.shortcuts import render
from entidades.forms import *
from entidades.models import *
from entidades.models import Estudiante
from entidades.models import Proponente
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

def estudiantesDetalles(request):     
    context = {
               'form': EstudianteForm()}
    return render(request, 'estudiante.html', context )

def tutores(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        context = {'msj': "Tutor creado con exito.",
                    'tutores': form}
        if form.is_valid():
            form.save()
            return render(request, 'index.html', context )
            
        else:
            context = {'msj': 'error'}
            return render(request, 'tutores.html', context)
    else:
        tutores = Tutor.objects.all()
        context = {'tutores': tutores,
               'form': TutorForm()}
        return render(request, 'tutores.html', context)

def tutorDetalles(request, ced):
     
    tutor = Tutor.objects.get(pk = '11-111')
    if request.method == 'POST':
        mensaje= "Tutor eliminado con exito"
        tutor.delete()
        context = {'msj': mensaje}
        return render(request, 'index.html', context)
    context = {'tutor': tutor}
    return render(request, 'tutor.html', context )

def cursa(request):
    context = {'msj':"Aqui va la vista inicial de cursa."}
    return render(request, 'cursa.html',context)

def proyectos(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        context = {'msj': "Proyecto creado con exito.",
                    'proy': form}
        if form.is_valid():
            form.save()
            return render(request, 'index.html', context )
            
        else:
            context = {'msj': 'error'}
            return render(request, 'proyectos.html', context)
    else:
        proy = Proyecto.objects.all()
        context = {'proy': proy,
               'form': ProyectoForm()}
    return render(request, 'proyectos.html', context)

def proyectoDetalles(request, cod):
     
    proy = Estudiante.objects.get(pk = cod)
    if request.method == 'POST':
        mensaje= "Proyecto eliminado con exito"
        proy.delete()
        context = {'msj': mensaje}
        return render(request, 'index.html', context)
    context = {'proy': proy}
    return render(request, 'estudiante.html', context )



def proponentes(request):
    if request.method == 'POST':
        form = ProponenteForm(request.POST)
        context = {'msj': "Proponente creado con exito.",
                    'proponentes': form}
        if form.is_valid():
            form.save()
            return render(request, 'index.html', context )

        else:
            context = {'msj': 'error'}
            return render(request, 'proponentes.html', context)
    else:
        proy = Proponente.objects.all()
        context = {'proponentes': proponentes,
               'form': ProponenteForm()}
    return render(request, 'proponentes.html', context)

def proponenteDetalles(request, cod):
    proponente = Proponente.objects.get(pk = cod)
    if request.method == 'POST':
        mensaje= "Propronente  eliminado con exito"
        proponente.delete()
        context = {'msj': mensaje}
        return render(request, 'index.html', context)
    context = {'proy': proy}
    return render(request, 'proponente.html', context )
