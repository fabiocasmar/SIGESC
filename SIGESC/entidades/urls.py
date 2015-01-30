'''
Aqui iran las vistas que manipulen cualquier
entidad indicada en el modelo de la
caparta local.
'''

from django.conf.urls import patterns, url
from entidades import views

urlpatterns = patterns('',
    url(r'^estudiantes/$', views.estudiantes, name='estudiante'),
    url(r'^estudiante/$', views.estudiantesDetalles, name='detalles_estudiante'),
    url(r'^tutores/$', views.tutores, name='tutor'),
    url(r'^tutores/(?P<ced>)\w+/$', views.tutorDetalles, name='detalles_tutor'),
    url(r'^proyectos/$', views.proyectos, name='proyecto'),
    url(r'^proyectos/(?P<cod>)\w+/$', views.proyectoDetalles, name='detalles_proyecto'),
    url(r'^proponentes/$', views.proponentes, name='proponente'),
    url(r'^proponentes/(?P<id>)\w+/$', views.proponenteDetalles, name='detalles_proponente'),
    url(r'^cursa/$', views.cursa, name='cursa'),
)
