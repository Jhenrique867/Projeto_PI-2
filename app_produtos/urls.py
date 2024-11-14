from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produto, name='lista_produtos'),  # URL para listar produtos
    path('cadprodutos/', views.cad_produtos, name='cadastra_produtos'), #URL para cadastrar produtos
]