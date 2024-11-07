from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produto, name='lista_produtos'),
    path('cadproduto/', views.cad_produtos, name='novo_produto'),
]
