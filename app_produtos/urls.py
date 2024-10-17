from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_usuarios, name='lista_produtos'),
    path('cad_produto/', views.novo_usuario, name='novo_produto'),
]
