from django.contrib import admin
from entidades import models    

# Register your models here.
@admin.register(models.Cursa)
class adminCursa(admin.ModelAdmin):
    pass

@admin.register(models.Tutor)
class adminTutor(admin.ModelAdmin):
    pass

@admin.register(models.Estudiante)
class adminEstudiante(admin.ModelAdmin):
    pass

@admin.register(models.Proyecto)
class adminProyecto(admin.ModelAdmin):
    pass