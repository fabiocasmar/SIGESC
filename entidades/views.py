from django.shortcuts import render
from entidades.forms import *
from entidades.models import *
from entidades.models import Estudiante, Proyecto
from entidades.models import Proponente, Tutor
from django.core import serializers

def estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        context = {'msj': "Estudiante creado con exito.",
                    'est': form}
        if form.is_valid():
            est = form.save()
            context = {'form' : form}
            return render(request, 'estudiantes.html', context )
        else:
            context = {'msj': 'error',
                       'form' : form}
            return render(request, 'estudiantes.html', context)
    else:
        est = Estudiante.objects.all()
        context = {'est': est,
               'form': EstudianteForm()}
    return render(request, 'estudiantes.html',context)

def estudiantesDetalles(request, ced):
    est = Estudiante.objects.get(cedula = ced)
    if request.method == 'POST':
        mensaje= "Estudiante eliminado con exito"
        est.delete()
        context = {'msj': mensaje}
        return render(request, 'estudiantes.html', context)
    context = {'est': est}
    return render(request, 'estudiante.html', context )

def tutores(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        context = {'msj': "Tutor creado con exito."}
        if form.is_valid():
            form.save()
            context = {'form' : form}
            return render(request, 'tutores.html', context)
        else:
            context = {'msj'  : 'error', 
                       'form' : form}
            return render(request, 'tutores.html', context)
    else:
        tutores = Tutor.objects.all()
        context = {'tutores': tutores,
               'form': TutorForm()}
        return render(request, 'tutores.html', context)

def tutorDetalles(request, ced):  
    tutor = Tutor.objects.get(cedula = ced)
    if request.method == 'POST':
        mensaje= "Tutor eliminado con exito"
        tutor.delete()
        context = {'msj': mensaje, 'form': TutorForm()}
        return render(request, 'tutores.html', context)
    context = {'tutor': tutor}
    return render(request, 'tutor.html', context )

def cursa(request):
    context = {'msj':"Aqui va la vista inicial de cursa."}
    return render(request, 'cursa.html',context)

def proyectos(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        context = {'msj': "Proyecto creado con exito.",}
        if form.is_valid():
            form.save()
            return render(request, 'proyecto.html', context )
            
        else:
            context = {'msj': 'error', 
                     'form' : form}
            return render(request, 'proyectos.html', context)
    else:
        proy = Proyecto.objects.all()
        context = {'proy': proy,
               'form': ProyectoForm()}
    return render(request, 'proyectos.html', context)

def proyectoDetalles(request, cod):
    proyecto = Proyecto.objects.get(cod_proyecto=cod)
    if request.method == 'POST':
        mensaje= "Proyecto eliminado con exito"
        proyecto.delete()
        context = {'msj': mensaje}
        return render(request, 'proyectos.html', context)
    context = {'proyecto': proyecto}
    return render(request, 'proyecto.html', context )


def proponentes(request):
    if request.method == 'POST':
        form = ProponenteForm(request.POST)
        context = {'msj': "Proponente creado con exito."}
        if form.is_valid():
            form.save()
            return render(request, 'proponentes.html', context )

        else:
            context = {'msj': 'error'}
            return render(request, 'proponentes.html', context)
    else:
        proponentes = Proponente.objects.all()
        context = {'proponentes': proponentes,
               'form': ProponenteForm()}
    return render(request, 'proponentes.html', context)

def proponenteDetalles(request, cod):
    proponente = Proponente.objects.get(pk = cod)
    if request.method == 'POST':
        mensaje= "Proponente  eliminado con exito"
        proponente.delete()
        context = {'msj': mensaje}
        return render(request, 'proponentes.html', context)
    context = {'proponente': proponente}
    return render(request, 'proponente.html', context )
