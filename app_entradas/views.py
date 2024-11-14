from django.shortcuts import render
from django.shortcuts import redirect
from .models import Entradas
from . import forms

# Create your views here.
def cad_entradas(request):
    form = forms.EntradaForm()
    if request.method == 'POST':
        form = forms.EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:lista_produtos')
    template_name = 'produtos/cadprodutos.html'
    context = {'form': form}
    return render(request, template_name, context)
    

def entradas(request):
    obj = Entradas.objects.all()
    template_name = 'produtos/entradas.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def deletar_produto(request, id_produto):
    obj = Entradas.objects.get(id_produto=id_produto)
    obj.delete()
    return redirect('produtos:lista_produtos')