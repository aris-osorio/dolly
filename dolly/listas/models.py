from django.db import models
from tableros.models import Tablero

# Create your models here.
class Lista(models.Model):
    nombre = models.CharField(max_length = 200)
    tablero = models.ForeignKey(Tablero, on_delete = models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    posicion = models.IntegerField()

    def __str__(self):
        return self.nombre
