from django import forms
from . import models

class EntradaForm(forms.ModelForm):
    class Meta:
        model = models.Entradas
        fields = '__all__'
