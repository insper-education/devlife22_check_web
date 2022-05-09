from django.test import TestCase
from .models import Produto, Cliente, Pedido, ItemPedido
import pytest

class MyTest(TestCase):
    fixtures = ["produtos.json","clientes.json","itenspedidos.json","pedidos.json"]

    def test_existe_produto(self):
        p = Produto.objects.get(pk=1)
        self.assertEqual(p.preco, 20)

    def criando_item_pedido(self):
        pedido = Pedido.objects.create(cliente=5, valor_total=0, pago=False)
        pedido.save()
        item = ItemPedido.objects.create(produto = 1, pedido = pedido.id, quantidade = 10)
        item.save()
        self.assertEqual(item.quantidade, 10)

    def get_dados_pedido(self):
        p = Pedido.objects.get(pk=3)
        print(p.cliente)
        for item in p.ItemPedido.objects.all():
            print(item.produto+"   "+item.quantidade)

    