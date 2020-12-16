from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 200)
    apellidos = models.CharField(max_length = 200)
    correo = models.CharField(max_length = 200)
    contraseña = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre
