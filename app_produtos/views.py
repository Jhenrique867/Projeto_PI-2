from django.shortcuts import render, redirect
from .models import Produto

def cad_produtos(request):
    return render (request, 'templastes/produtos/cadprodutos.html')

def produto(request):
    novo_produto = Produto()
    novo_produto.descricao = request.POST.get('descricao')
    novo_produto.fornecedor = request.POST.get('ornecedor')
    novo_produto.custo = request.POST.get('custo')
    novo_produto.lucro = request.POST.get("lucro")
    novo_produto.valor_de_venda =request.POST.get("valor venda")
    novo_produto.marca = request.POST.get("marca")