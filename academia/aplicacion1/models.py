from django.db import models


# Create your models here.
# creas las tablas
class Clientes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
