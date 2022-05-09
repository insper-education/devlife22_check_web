import pytest
from django.db import models
from .models import Produto
from django.urls import reverse

@pytest.mark.django_db
def test_view(client):
   url = reverse('loja:index')
   print(url)
   response = client.get(url)
   assert response.status_code == 200, "O servidor não está executando ou tem algo errado com a aplicação. Você definiu corretamente as rotas do projeto?"

@pytest.fixture
def Produto():
    try:
        from .models import Produto as model
        return model
    except ImportError:
        raise AssertionError('Você não implementou o modelo Produto ou ele não foi encontrado no arquivo models.py')

@pytest.fixture
def campos_por_nome(Produto):
    return {
        campo.name: campo
        for campo in Produto._meta.fields
    }

@pytest.mark.django_db
def test_campo_nome(campos_por_nome):
    campo_nome = campos_por_nome.get('nome')
    assert campo_nome is not None, 'O modelo Produto não possui um campo nome.'
    assert isinstance(campo_nome, models.CharField), 'O campo nome deveria ser do tipo CharField.'
    assert campo_nome.max_length == 100, 'O campo nome deveria ter um limite de 100 caracteres.'

@pytest.mark.django_db
def test_campo_preco(campos_por_nome):
    campo_preco = campos_por_nome.get('preco')
    assert campo_preco is not None, 'O modelo Produto não possui um campo preco.'
    assert isinstance(campo_preco, models.DecimalField), 'O campo preco deveria ser do tipo DecimalField.'
    assert campo_preco.default == pytest.approx(0), 'O campo preco deveria ter um valor padrão igual a zero.'

@pytest.mark.django_db
def test_campo_descricao(campos_por_nome):
    campo_descricao = campos_por_nome.get('descricao')
    assert campo_descricao is not None, 'O modelo Produto não possui um campo descricao.'
    assert isinstance(campo_descricao, models.TextField), 'O campo descricao deveria ser do tipo TextField.'




