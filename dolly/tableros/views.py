from rest_framework import viewsets
from django.shortcuts import render
from tableros.models import Tablero
from tableros.serializers import TableroSerializer

# Create your views here.
class TablerosViewSet(viewsets.ModelViewSet):
    serializer_class = TableroSerializer
    queryset = Tablero.objects.all()

