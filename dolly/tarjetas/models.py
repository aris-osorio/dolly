from django.db import models
from listas.models import Lista
from usuarios.models import Usuario

# Create your models here.
class Tarjeta(models.Model):
    nombre = models.CharField(max_length = 200)
    lista = models.ForeignKey(Lista, on_delete = models.CASCADE)
    descripcion = models.CharField(max_length = 200)
    miembros = models.ManyToManyField(Usuario, related_name='tarjetas')
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null = True)
    posicion = models.IntegerField()

    def __str__(self):
        return self.nombre