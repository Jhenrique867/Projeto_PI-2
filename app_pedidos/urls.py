from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('cad_pedido/', views.novo_pedido, name='novo_pedido'),
]
