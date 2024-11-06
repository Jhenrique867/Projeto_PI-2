from django.db import models

class Venda(models.Model):

    código_venda = models.AutoField(primary_key=True)
    código_produto = models.IntegerField()
    produto = models.TextField(max_length=255)
    data_venda = models.DateTimeField(auto_now=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_venda = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_geral = models.IntegerField()
    forma_pagamento = models.TextField(max_length=255)
    observacoes = models.TextField(max_length=255)    
