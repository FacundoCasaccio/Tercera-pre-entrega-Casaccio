from django import forms 

# Formulario para registrar instrumentos
class FormularioInstrumento(forms.Form):
    instrumentos = (
        (1, "Guitarra"),
        (2, "Bajo"),
        (3, "Teclado"),
    )
    
    marcas = (
        (1, "Ibanez"),
        (2, "Gibson"),
        (3, "Fender"),
        (4, "Casio"),
        (5, "Yamaha"),
    )
    
    tipo = forms.ChoiceField(label="Instrumento", choices=instrumentos, required=True)
    marca = forms.ChoiceField(label="Marca", choices=marcas, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    precio = forms.FloatField(label="Precio", required=True)

# Formulario para registrar discos
class FormularioDisco(forms.Form):
    artista = forms.CharField(label="Artista", max_length=50, required=True)
    album = forms.CharField(label="Album", max_length=50, required=True)
    precio = forms.FloatField(label="Precio", required=True)

# Formulario para registrar remeras
class FormularioRemera(forms.Form):
    color = (
        (1, "Negro"),
        (2, "Blanco"),
        (3, "Gris"),
    )

    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    color = forms.ChoiceField(label="Color", choices=color, required=True)
    precio = forms.FloatField(label="Precio", required=True)

class FormularioInstrumentosPorMarca(forms.Form):
    instrumentos = (
        (1, "Guitarra"),
        (2, "Bajo"),
        (3, "Teclado"),
    )
    
    marcas = (
        (1, "Ibanez"),
        (2, "Gibson"),
        (3, "Fender"),
        (4, "Casio"),
        (5, "Yamaha"),
    )
        
    tipo = forms.ChoiceField(label="Instrumento", choices=instrumentos, required=True)
    marca = forms.ChoiceField(label="Marca", choices=marcas, required=True)