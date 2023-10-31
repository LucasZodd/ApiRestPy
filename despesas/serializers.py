from rest_framework import serializers

from .models import Despesa, Categoria

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        filds = '__all__'

# class CategoriaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Categoria
#         filds = '__all__'