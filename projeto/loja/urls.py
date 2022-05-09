from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    # /loja/
    path('', views.index, name='index'),
    # /loja/1/
    path('<int:produto_id>/', views.detail_produto, name='detail_produto'),
    # /add_item
    path('add_item/', views.add_item, name='add_item'),
    # /add_pedido
    path('add_pedido/', views.add_pedido, name='add_pedido'),
    # /clientes
    path('clientes/', views.clientes, name='clientes'),
    
    # /loja/cliente/1
    # TODO
    
    # /add_produto
    path('add_produto/', views.add_produto, name='add_produto'),
]
