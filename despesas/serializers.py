from rest_framework import serializers

from .models import Despesa, Categoria

# Classe para converter os dados de despesa para um modelo de consulta como JSON
class DespesaSerializer(serializers.ModelSerializer):
    
    despesa_categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(),
        slug_field='categoria_nome',
    )

    class Meta:
        model = Despesa
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'