from django import forms
from . import models

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = ['nome', 'descricao', 'quantidade', 'fornecedor', 'marca', 'custo', 'valor_produto', 'lucro', 'observacao']
