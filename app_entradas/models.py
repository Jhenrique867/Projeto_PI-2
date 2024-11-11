from django.db import models


class Entradas(models.Model):

    data_entrada= models.DateTimeField(auto_now_add=False)
    produto = models.IntegerField(null=False)
    custo_unitario = models.DecimalField(max_digits=10,decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    código_produto = models.IntegerField()
    qtd_embalagem = models.IntegerField(null=False)
    quantidade = models.IntegerField()
    tipo_embalagem = models.TextField(max_length=255, null=False)
    Observacoes = models.TextField(max_length=255)
    fabricante = models.IntegerField(null=False)






