from django.shortcuts import render, redirect
from .models import Produto
from . import forms


def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def cad_produtos(request):
    if request.method == 'POST':
        form = forms.ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:lista_produtos')
    else:
        form = forms.ProdutoForm()
    return render(request, 'cadprodutos.html', {'form': form})
