from django.urls import path
from app_vendas import views

app_name = 'vendas'

urlpatterns = [
    path('', views.lista_vendas, name='lista_vendas'),
    path('cad_venda/', views.nova_venda, name='nova_venda'),
]
