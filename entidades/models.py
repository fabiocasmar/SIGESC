'''
Created on 22/1/2015

@author: Emmanuel De Aguiar

@author: Daniel Pelayo

@author: Daniel Zeait

'''

from django.db import models

class Estudiante(models.Model):
    tipo_sexo=(
              ("M","Masculino"),
              ("F","Femenino"),
              )
        
    USBID = models.CharField(max_length = 8,primary_key = True)
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    cedula = models.CharField(max_length = 8)
    carrera = models.CharField(max_length = 30)
    sede = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    sexo = models.CharField(max_length = 1, choices = tipo_sexo)
    telefono = models.CharField(max_length = 12)
    direccion = models.CharField(max_length = 50)
    
        
class Tutor(models.Model):
    tipo_sexo=(
              ("M","Masculino"),
              ("F","Femenino"),
              )
    
    USBID = models.CharField(max_length = 20,primary_key = True)
    cedula = models.CharField(max_length = 8)    
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    sede = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    sexo = models.CharField(max_length = 1, choices = tipo_sexo)
    telefono = models.CharField(max_length = 12)
    direccion = models.CharField(max_length = 50)
    
class Proyecto(models.Model):
    cod_proyecto = models.CharField(max_length = 7,primary_key = True)
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100)
    area = models.CharField(max_length = 40)
    estado = models.CharField(max_length = 10)
    tutor = models.ForeignKey(Tutor)

class Cursa(models.Model):
    tipo_estado=(
              ("R","Retirado"),
              ("C","En curso"),
              ("F","Finalizado"),
              )
    
    estudiante= models.ForeignKey(Estudiante)    
    proyecto= models.ForeignKey(Proyecto)
    estado=models.CharField(max_length = 10, choices = tipo_estado)