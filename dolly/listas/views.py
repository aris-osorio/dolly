from rest_framework import viewsets
from django.shortcuts import render
from listas.models import Lista
from listas.serializers import ListaSerializer

# Create your views here.
class ListasViewSet(viewsets.ModelViewSet):
    serializer_class = ListaSerializer
    queryset = Lista.objects.all()

