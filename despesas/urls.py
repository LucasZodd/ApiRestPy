from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('despesas', views.get_despesas, name='get_all_despesa'),
    path('categorias', views.get_categorias, name='get_all_despesa'),
    path('categoria/<str:nick>', views.get_categoria_by_name),
    path('despesa/<str:nick>', views.get_categoria_filter),
    path('despesa/data/<str:data_inicial>/<str:data_final>', views.get_data_filter),
    path('cadastro/despesa', views.cadastro_despesa),
    path('cadastro/categoria', views.cadastro_categoria),
]
