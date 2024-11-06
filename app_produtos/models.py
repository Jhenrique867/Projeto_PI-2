from django.db import models

class Produto (models.Model):

<<<<<<< HEAD
    descricao = models.TextField(max_length=100, null=False)
    quantidade = models.IntegerField(null=False)
    fornecedor = models.TextField(max_length=100, null=False)
    fabricante = models.TextField(max_length=100, null=False)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    lucro = models.IntegerField(null=False)                       
    observação = models.TextField(max_length=255, null=False)

=======
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    descricao = models.TextField(max_length=100)
    quantidade = models.IntegerField(max_length=4)
    fornecedor = models.TextField(max_length=100)
    marca = models.TextField(max_length=255)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_produto = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.DecimalField(max_digits=5, decimal_places=2)                            
    observacao = models.TextField(max_length=255)

    def __str__(self):
        return self.nome
>>>>>>> 412b564798e7fa0dbdbda709840ec3c9daf10a1d
