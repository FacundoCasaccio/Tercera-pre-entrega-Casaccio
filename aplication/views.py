from django.shortcuts import render
from django.http import HttpRequest
from .models import *
from .forms import *

def index(request):
    return render(request, "aplication/index.html")

# Formulario para la carga de instrumentos
def instrumentoForm(request):
    if request.method == "POST":   
        formulario = FormularioInstrumento(request.POST)
        if formulario.is_valid():
            tipo_instrumento = formulario.cleaned_data.get('tipo')
            marca_instrumento = formulario.cleaned_data.get('marca')
            modelo_instrumento = formulario.cleaned_data.get('modelo')
            precio_instrumento = formulario.cleaned_data.get('precio')
            
            # Labels de los select
            tipo_instrumento_label = formulario.fields['tipo'].choices[int(tipo_instrumento) - 1][1]
            marca_instrumento_label = formulario.fields['marca'].choices[int(marca_instrumento) - 1][1]

            instrumento = Instrumento(tipo = tipo_instrumento_label, 
                                      marca = marca_instrumento_label,
                                      modelo = modelo_instrumento,
                                      precio = precio_instrumento)
            instrumento.save()
            return render(request, "aplication/index.html")
    else:
        formulario = FormularioInstrumento()

    return render(request, "aplication/formulario_instrumentos.html", {"form":formulario})

# Formulario para la carga de discos
def discoForm(request):
    if request.method == "POST":   
        formulario = FormularioDisco(request.POST)
        if formulario.is_valid():
            artista_disco = formulario.cleaned_data.get('artista')
            album_disco = formulario.cleaned_data.get('album')
            precio_disco = formulario.cleaned_data.get('precio')
            
            disco = Disco(artista = artista_disco, 
                          album = album_disco,
                          precio = precio_disco)
            disco.save()
            return render(request, "aplication/index.html")
    else:
        formulario = FormularioDisco()

    return render(request, "aplication/formulario_discos.html", {"form":formulario})

# Formulario para la carga de remeras
def remeraForm(request):
    if request.method == "POST":   
        formulario = FormularioRemera(request.POST)
        if formulario.is_valid():
            modelo_remera = formulario.cleaned_data.get('modelo')
            color_remera = formulario.cleaned_data.get('color')
            precio_remera = formulario.cleaned_data.get('precio')

            # Label del color
            color_remera_label = formulario.fields['color'].choices[int(color_remera) - 1][1]
            
            remera = Remera(modelo = modelo_remera, 
                          color = color_remera_label,
                          precio = precio_remera)
            remera.save()
            return render(request, "aplication/index.html")
    else:
        formulario = FormularioRemera()

    return render(request, "aplication/formulario_remeras.html", {"form":formulario})

def busquedaForm(request):
    if request.method == "GET":   
        formulario = FormularioInstrumentosPorMarca(request.GET)
        if formulario.is_valid():
            # Opciones de los select
            tipo_instrumento = formulario.cleaned_data.get('tipo')
            marca_instrumento = formulario.cleaned_data.get('marca')

            # Labels de los select
            tipo_instrumento_label = formulario.fields['tipo'].choices[int(tipo_instrumento) - 1][1]
            marca_instrumento_label = formulario.fields['marca'].choices[int(marca_instrumento) - 1][1]
            
            instrumentos = Instrumento.objects.filter(tipo__icontains=tipo_instrumento_label, 
                                                      marca__icontains=marca_instrumento_label)
            

            return render(request, 
                      "aplication/resultados_busqueda.html", 
                      {"tipo": tipo_instrumento_label, "marca":marca_instrumento_label, "instrumentos":instrumentos,
                      })
    else:
        formulario = FormularioInstrumentosPorMarca()

    return render(request, "aplication/buscar_instrumento.html", {"form":formulario})


def listarInstrumentos(request):
    context = {"instrumentos": Instrumento.objects.all() }
    return render(request, "aplication/instrumentos.html", context)

def listarDiscos(request):
    context = {"discos": Disco.objects.all() }
    return render(request, "aplication/discos.html", context)

def listarRemeras(request):
    context = {"remeras": Remera.objects.all() }
    return render(request, "aplication/remeras.html", context)