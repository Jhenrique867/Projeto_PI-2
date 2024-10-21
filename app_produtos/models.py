from django.db import models


class Produto (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
<<<<<<< HEAD
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    Fabricante = models.TextField(max_length=255)
    
    
=======
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

class SaidaVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField()

class EntradaVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField()

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
>>>>>>> dcb0ac2ba6f4c98f85fd338e9b89e5cf00527eb3
