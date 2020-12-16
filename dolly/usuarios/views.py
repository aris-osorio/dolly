from rest_framework import viewsets
from django.shortcuts import render
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
