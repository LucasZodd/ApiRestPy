from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Despesa, Categoria
from .serializers import DespesaSerializer, CategoriaSerializer

import json

# Get de todas as despesas
@api_view(['GET'])  
def get_despesas(request):

    if request.method == 'GET':

        despesas = Despesa.objects.all() 
        
        serializer = DespesaSerializer(despesas, many=True) 
        
        return Response(serializer.data) 

    return Response(status=status.HTTP_404_NOT_FOUND)

# Get da despesas filtrada por categoria
@api_view(['GET'])
def get_categoria_filter(request, nick):
    
    try:
        despesas = Despesa.objects.filter(despesa_categoria = nick)
        
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        

        serializer = DespesaSerializer(despesas, many=True)
        
        return Response(serializer.data) 
    
# Get da despesas filtrada por data
@api_view(['GET'])
def get_data_filter(request, data_inicial, data_final):
    
    try:
        despesas = Despesa.objects.filter(despesa_data__range=[data_inicial, data_final])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = DespesaSerializer(despesas, many=True)
        
        return Response(serializer.data)
    
# Get da categoria por nome
@api_view(['GET']) 
def get_categoria_by_name(request, nick):
    
    try:
        categoria = Categoria.objects.get(categoria_nome = nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = CategoriaSerializer(categoria)  
        return Response(serializer.data)
        
# Get de todas as categorias
@api_view(['GET'])
def get_categorias(request):

    if request.method == 'GET':

        categorias = Categoria.objects.all() 

        serializer = CategoriaSerializer(categorias, many=True)
        
        return Response(serializer.data) 

    return Response(status=status.HTTP_404_NOT_FOUND)

# Cadastro de despesa
@api_view(['POST'])
def cadastro_despesa(request):
    
    if request.method == 'POST':

        new_despesa = request.data
        
        serializar = DespesaSerializer(data=new_despesa)
        
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_201_CREATED)
    
    return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)

# Cadastro de categoria
@api_view(['POST'])
def cadastro_categoria(request):
    
    if request.method == 'POST':

        new_categoria = request.data
        
        serializar = CategoriaSerializer(data=new_categoria)
        
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_201_CREATED)
    
    return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)