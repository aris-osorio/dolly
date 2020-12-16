from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Tablero(models.Model):
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    favorito = models.BooleanField(default = False)
    visibilidad = models.BooleanField(default = False)
    miembros = models.ManyToManyField(Usuario, related_name='tableros')

    def __str__(self):
        return self.nombre
