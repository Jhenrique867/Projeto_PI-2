from django.shortcuts import render, redirect
from .models import Produto

def cad_produtos(request):
    return render (request, 'produtos/cadprodutos.html')


# Não sei se é desse jeito mais vou deixar assim por enquanto
def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})

# essa função tá fazendo dar erro ao selecionar o botão de produtos

# def produto(request):
#     novo_produto = Produto()
#     novo_produto.descricao = request.POST.get('descricao')
#     novo_produto.fornecedor = request.POST.get('ornecedor')
#     novo_produto.custo = request.POST.get('custo')
#     novo_produto.lucro = request.POST.get("lucro")
#     novo_produto.valor_de_venda =request.POST.get("valor venda")
#     novo_produto.marca = request.POST.get("marca")