from django.db import models

# Create your models here.
#creas las tablas
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    telefono = models.IntegerField()

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.IntegerField()
    entregado=models.BooleanField()



