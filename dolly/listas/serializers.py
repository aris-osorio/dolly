from rest_framework import serializers
from listas.models import Lista

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'