from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Aqui va la vista inicial de la pagina, con links.")