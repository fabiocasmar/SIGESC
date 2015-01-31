from django.contrib import admin
from entidades import models

# Register your models here.
@admin.register(models.Cursa)
class adminCursa(admin.ModelAdmin):
    list_display = ('proyecto', 'estudiante', 'estado')
    search_fields = ('proyecto', 'estudiante', 'estado')
    list_filter = ('proyecto', 'estado')

@admin.register(models.Tutor)
class adminTutor(admin.ModelAdmin):
    list_display = ('USBID', 'nombre', 'cedula', 'sede',
                     'email', 'telefono')
    search_fields = ('USBID', 'nombre', 'cedula', 'sede',
                     'email', 'telefono')
    list_filter = ('sede',)

@admin.register(models.Estudiante)
class adminEstudiante(admin.ModelAdmin):
    list_display = ('USBID', 'nombre', 'carrera', 'sede', 'email', 'telefono')
    search_fields = ('USBID', 'nombre', 'cedula', 'carrera', 'sede',
                     'email', 'carrera', 'telefono')
    list_filter = ('sede', 'carrera',)

@admin.register(models.Proyecto)
class adminProyecto(admin.ModelAdmin):
    list_display = ('tutor','area', 'nombre', 'cod_proyecto', 'estado')
    search_fields = ('tutor', 'area', 'nombre', 'cod_proyecto', 'estado')
    list_filter = ('area', 'estado')
    
@admin.register(models.Proponente)  
class adminProponente(admin.ModelAdmin):
    list_display = ('tipo_prop','id','nombre','apellido','email','sexo','telefono')
    search_fields = ('tipo','id','nombre','apellido','email','sexo','telefono')
    list_filter = ('tipo_prop',)
    
@admin.register(models.Sede)  
class adminSede(admin.ModelAdmin):
    list_display = ('nombre_sede',)
    search_fields = ('nombre_sede',)
    list_filter = ('nombre_sede',)
    
@admin.register(models.Area)  
class adminArea(admin.ModelAdmin):
    list_display = ('nombre_area',)
    search_fields = ('nombre_area',)
    list_filter = ('nombre_area',)
    
