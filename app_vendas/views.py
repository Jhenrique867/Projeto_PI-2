from django.shortcuts import redirect, render
from .models import Venda


def venda(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/vendas.html', {'vendas': vendas})

def cad_vendas(request):
    return render(request, 'vendas/cad_vendas.html')