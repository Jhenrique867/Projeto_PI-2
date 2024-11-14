from django import forms
from . import models

class SaidaForm(forms.ModelForm):
    class Meta:
        model = models.Saida
        fields = '__all__'