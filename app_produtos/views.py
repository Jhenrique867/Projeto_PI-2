from django.shortcuts import render, redirect
from .models import Produto
from . import forms

def cad_produtos(request):
    if request.method == 'POST':
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:lista_produtos')
    else:
        form = forms.ProdutoForm()
    return render(request, 'Arquivos_HTML/cadprodutos.html', {'form': form})

def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'Arquivos_HTML/produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        novo_produto = Produto(
            descricao=request.POST.get('descricao'),
            quantidade=request.POST.get('quantidade'),
            fornecedor=request.POST.get('fornecedor'),
            valor_produto=request.POST.get('valor_produto'),
            lucro=request.POST.get('lucro'),
            observacao=request.POST.get('observacao'),
            custo=request.POST.get('custo')
        )
        novo_produto.save()
        return redirect('produtos:lista_produtos')
    return render(request, 'Arquivos_HTML/cadprodutos.html')  