'''
Aqui iran las vistas que manipulen cualquier
entidad indicada en el modelo de la
caparta local.
'''

from django.conf.urls import patterns, url
from entidades import views

urlpatterns = patterns('',
    url(r'^estudiante/$', views.estudiante, name='estudiante'),
    url(r'^tutor/$', views.tutor, name='tutor'),
    url(r'^proyecto/$', views.proyecto, name='proyecto'),
    url(r'^cursa/$', views.cursa, name='cursa'),
)