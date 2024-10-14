from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),
]
