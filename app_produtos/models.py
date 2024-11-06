from django.db import models

class Produto (models.Model):

    descricao = models.TextField(max_length=100, null=False)
    quantidade = models.IntegerField(null=False)
    fornecedor = models.TextField(max_length=100, null=False)
    fabricante = models.TextField(max_length=100, null=False)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    lucro = models.IntegerField(null=False)                       
    observação = models.TextField(max_length=255, null=False)

