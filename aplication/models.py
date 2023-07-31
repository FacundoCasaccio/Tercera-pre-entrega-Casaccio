from django.db import models

class Instrumento(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"{self.tipo} {self.marca} - Modelo: {self.modelo} - ${self.precio}"
    
class Disco(models.Model):
    artista = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f"{self.album} - {self.artista} - ${self.precio}"

class Remera(models.Model):
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f"Remera {self.modelo}, color: {self.color} - ${self.precio}"
