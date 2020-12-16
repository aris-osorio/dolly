from django.db import models
from tarjetas.models import Tarjeta
from usuarios.models import Usuario
# Create your models here.
class Comentario(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete = models.CASCADE)
    mensaje = models.CharField(max_length = 200)
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.mensaje
