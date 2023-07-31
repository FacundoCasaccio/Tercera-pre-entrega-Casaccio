from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('instrumentos/', listarInstrumentos, name="instrumentos"),
    path('cargar_instrumentos/', instrumentoForm, name="instrumento_form"),
    path('discos/', listarDiscos, name="discos"),
    path('cargar_discos/', discoForm, name="disco_form"),
    path('remeras/', listarRemeras, name="remeras"),
    path('cargar_remeras/', remeraForm, name="remera_form"),
    path('buscar_instrumentos/', busquedaForm, name="buscar_instrumentos"),
]
