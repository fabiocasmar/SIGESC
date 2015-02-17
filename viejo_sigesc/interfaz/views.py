from django.shortcuts import render, HttpResponse

def index(request):
    context = {'msj':"Aqui va la vista inicial de la pagina, con links."}
    return render(request, 'index.html',context)