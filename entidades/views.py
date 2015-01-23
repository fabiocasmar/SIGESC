from django.shortcuts import render
def estudiante(request):
    context = {'msj':"Aqui va la vista inicial estudiante."}
    return render(request, 'estudiante.html',context)

def tutor(request):
    context = {'msj':"Aqui va la vista inicial de tutor."}
    return render(request, 'tutor.html',context)

def cursa(request):
    context = {'msj':"Aqui va la vista inicial de cursa."}
    return render(request, 'cursa.html',context)

def proyecto(request):
    context = {'msj':"Aqui va la vista inicial de proyecta."}
    return render(request, 'proyecto.html',context)