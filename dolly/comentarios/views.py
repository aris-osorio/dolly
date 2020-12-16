from rest_framework import viewsets
from django.shortcuts import render
from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer

# Create your views here.
class ComentariosViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()