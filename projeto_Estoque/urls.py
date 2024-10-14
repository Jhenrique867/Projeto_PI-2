
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')), 
    path('fornecedores/', include('app_fornecedores.urls')),
    path('produtos/', include('app_produtos.urls')), 
    path('pedidos/', include('app_pedidos.urls')), 
    path('vendas/', include('app_vendas')), 
    path('usuarios/', include('app_usuarios'))

]
