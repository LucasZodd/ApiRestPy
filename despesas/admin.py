from django.contrib import admin

from .models import Despesa, Categoria

# Registrando o modelo despesa e categoria para facilitar inserir dados
admin.site.register(Despesa)
admin.site.register(Categoria)
