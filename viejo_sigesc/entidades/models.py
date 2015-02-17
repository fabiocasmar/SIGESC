'''
Created on 22/1/2015

@author: Emmanuel De Aguiar

@author: Daniel Pelayo

@author: Daniel Zeait

'''

from django.db import models
import re
from django.core.exceptions import ValidationError

def validarCarnet(carnet):
    
    if not re.match(r'[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]',carnet):
        raise ValidationError('%s Carnet no valido. Debe ser de la forma: XX-XXXXX' % carnet)
    else:
        pass        
    
class Sede(models.Model):
    nombre_sede = models.CharField(max_length = 15, primary_key = True)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre_sede
    
class Area(models.Model):
    nombre_area = models.CharField(max_length = 30, primary_key = True)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre_area


class Estudiante(models.Model):
    tipo_sexo=(("M","Masculino"), ("F","Femenino"),)
    tipo_carrera = (('0800','Ing. Computacion'),('0100','Ing. Mecanica'),('0200','Ing. Electrica'),('0300','Ing. Electronica'),
                    ('0400','Ing. Produccion'),('0500','Ing. Materiales'),('0600','Ing. Quimica'),('0700','Ing. Geofisica'))
    
        
    USBID = models.CharField(max_length = 8, primary_key = True, validators = [validarCarnet])
    nombre = models.CharField(max_length = 30, blank = False)
    apellido = models.CharField(max_length = 30, blank = False)
    cedula = models.CharField(max_length = 8, blank = False)
    carrera = models.CharField(max_length = 4, choices = tipo_carrera, blank = False)
    sede = models.ForeignKey(Sede, blank = False)
    email = models.EmailField(max_length = 75, blank = False)
    sexo = models.CharField(max_length = 1, choices = tipo_sexo, blank = False)
    telefono = models.CharField(max_length = 12, blank = False)
    direccion = models.CharField(max_length = 50, blank = False)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre + " " + self.apellido + " carnet: " + self.USBID
    
        
class Tutor(models.Model):
    tipo_sexo=(("M","Masculino"),("F","Femenino"))
    
    USBID = models.EmailField(max_length = 75, primary_key = True)
    cedula = models.CharField(max_length = 8, blank = False)    
    nombre = models.CharField(max_length = 30, blank = False)
    apellido = models.CharField(max_length = 30, blank = False)
    sede = models.ForeignKey(Sede, blank = False)
    email = models.EmailField(max_length = 30, blank = False)
    sexo = models.CharField(max_length = 1, choices = tipo_sexo, blank = False)
    telefono = models.CharField(max_length = 12, blank = False)
    direccion = models.CharField(max_length = 50, blank = False)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre + " " + self.apellido

class Proponente(models.Model):
    tipo_sexo=(("M","Masculino"),("F","Femenino"))
    tipo = (("E","Estudiante"),("P","Profesor"),("C","Comunidad"))
    tipo_prop = models.CharField(max_length = 15, choices = tipo, blank = False)
    id = models.CharField(max_length = 8, blank = False,primary_key = True)    
    nombre = models.CharField(max_length = 30, blank = False)
    apellido = models.CharField(max_length = 30, blank = False)
    email = models.EmailField(max_length = 30, blank = False)
    sexo = models.CharField(max_length = 1, choices = tipo_sexo, blank = False)
    telefono = models.CharField(max_length = 12, blank = False)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.id + " " +self.nombre

class Proyecto(models.Model):
    cod_proyecto = models.CharField(max_length = 7,blank = False,primary_key = True)
    def __str__(self):              # __unicode__ on Python 2
        return self.cod_proyecto
    
class Estado(models.Model):
    nombre = models.CharField(primary_key = True,blank = False,max_length = 20)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre
    
class Comunidad(models.Model):
    nombre = models.CharField(max_length = 25, blank = False,)
    estado = models.ForeignKey(Estado,default = None, blank = False)
    descripcion = models.TextField(max_length = 400, blank = False)
    cantidadBeneficiados = models.IntegerField(blank = False)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre

class CaracteristicasProyecto(models.Model):
    tipo_estado_proyecto=(("A","Abierto"),("C","Cerrado"),('P','En Proceso'))
    
    proyecto = models.ForeignKey(Proyecto, blank = False,default = None)
    nombre = models.CharField(max_length = 30, blank = False)
    descripcion = models.CharField(max_length = 100, blank = False)
    area = models.ForeignKey(Area, blank = False)
    estado = models.CharField(max_length = 10, blank = False, choices = tipo_estado_proyecto)
    tutor =      models.ForeignKey(Tutor,blank = False)
    fecha_inicio = models.DateTimeField(blank = False)
    fecha_fin = models.DateTimeField(blank = False)
    version= models.CharField(max_length = 10, blank = False,primary_key = True)
    comunidad = models.ForeignKey(Comunidad,default = None)
    proponente = models.ForeignKey(Proponente,default = None)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombre + " " +self.version
    


class Cursa(models.Model):
    tipo_estado=(("R","Retirado"),("C","En curso"),("F","Finalizado"))
    
    estudiante= models.ForeignKey(Estudiante)    
    proyecto= models.ForeignKey(Proyecto)
    estado=models.CharField(max_length = 10, choices = tipo_estado)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.estado
    

    
