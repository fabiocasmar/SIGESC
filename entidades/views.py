from django.shortcuts import render
def estudiantes(request):
    context = {'msj':"Aqui va la vista inicial estudiante."}
    return render(request, 'estudiantes.html',context)

def tutores(request):
    context = {'msj':"Aqui va la vista inicial de tutor."}
    return render(request, 'tutores.html',context)

def cursa(request):
    context = {'msj':"Aqui va la vista inicial de cursa."}
    return render(request, 'cursa.html',context)

def proyectos(request):
    context = {'msj':"Aqui va la vista inicial de proyecta."}
    return render(request, 'proyectos.html',context)