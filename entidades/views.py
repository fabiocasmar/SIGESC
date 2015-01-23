from django.shortcuts import render, HttpResponse

def estudiante(request):
    return HttpResponse('vista de estudiante')

def tutor(request):
    return HttpResponse("vista de tutor")

def cursa(request):
    return HttpResponse("vista de cursa")

def proyecto(request):
    return HttpResponse('vista de proyecto')