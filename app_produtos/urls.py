from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produto, name='lista_produtos'),  # URL para listar produtos
    path('cadprodutos/', views.cad_produtos, name='cadastra_produtos'),
    path('criar_produto/', views.criar_produto, name='criar_produto'),
]