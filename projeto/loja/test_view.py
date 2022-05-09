from django.test import TestCase
from .models import Produto
import pytest
from django.test import RequestFactory
from loja.views import detail_produto

class MyTest(TestCase):
    fixtures = ["produtos.json","clientes.json","itenspedidos.json","pedidos.json"]

    def test_should_create_group(self):
        p = Produto.objects.get(pk=1)
        self.assertEqual(p.preco, 20)
    
    @pytest.mark.django_db
    def test_detail_product(self):
        texto_alerta = "A view que mostra detalhes do produto não está pronta. Você terminou de implementar?"
        try:
            rf = RequestFactory()
            request = rf.get('/loja')
            response = detail_produto(request, 1)
            assert response.status_code == 200, texto_alerta
        except NameError:
            raise AssertionError(texto_alerta)