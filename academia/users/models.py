from django.db import models

class usuarios(models.Model):
    email = models.EmailField(max_length=100)
    #usarmos hexadecimales para incriptar el password para evitar robos
    password = models.CharField(max_length=254)
    #con ese token se autentifica a la api para que el frontend pueda dar accesos a los apartados de la pagina
    token=models.CharField(max_length=100)
    
