from django.db import models

# Criando classe de categora e despesa para salvar no banco de dados
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nome = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Nome: {self.categoria_nome}'

class Despesa(models.Model):

    despesa_id = models.AutoField(primary_key=True)
    despesa_descricao = models.TextField(default='')
    despesa_data = models.DateField(default='')
    despesa_valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    despesa_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Descrição: {self.despesa_descricao} | Data: {self.despesa_data} | Valor: {self.despesa_valor} | Categoria: {self.despesa_categoria.categoria_nome}'