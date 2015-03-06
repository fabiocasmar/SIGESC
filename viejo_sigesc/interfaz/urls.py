'''
Aqui iran las vistas que no manipulan ningun
modelo pero son necesarias para la correcta
y facil utilizacion de la pagina.
'''

from django.conf.urls import patterns, url
from interfaz import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='home'),
)