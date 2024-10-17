from django.db import models


class Produto (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    Fabricante = models.TextField(max_length=255)
    
    
