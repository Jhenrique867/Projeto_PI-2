from django.shortcuts import redirect, render
from .models import Venda
from . import forms 


def venda(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas.html', {'vendas': vendas})
  
def cad_vendas(request):
    if request.method == 'POST': 
        form = forms.VendaForm(request.POST)
        if  form.is_valid():
            form.save()
            return render(request, 'cadvenda.html')
    else: 
        form = forms.VendaForm()
    return render(request, 'cadvenda.html', {'form':form})