from rest_framework import viewsets
from django.shortcuts import render
from tarjetas.models import Tarjeta
from tarjetas.serializers import TarjetaSerializer

# Create your views here.
class TarjetasViewSet(viewsets.ModelViewSet):
    serializer_class = TarjetaSerializer
    queryset = Tarjeta.objects.all()