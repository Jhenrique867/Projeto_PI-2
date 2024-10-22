from django.db import models

class Venda(models.Model):

    id_venda = models.AutoField(primary_key=True)
    produto_venda = models.TextField(max_length=255)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now=True)
    quantidade_venda = models.IntegerField(max_length=4)
    