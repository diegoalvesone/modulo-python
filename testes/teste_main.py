from main import Produto
import pytest

@pytest.fixture
def produto():
    return Produto(1, 'python', 1.0, 10)


def test_constructor(produto):
    assert produto.id      == 1
    assert produto.nome    == 'python'
    assert produto.preco   == 1.0
    assert produto.estoque == 10


def test_adicionar_estoque(produto):
    produto.adicionar_estoque(10)
    assert produto.estoque == 20


def test_remover_estoque(produto):
    produto.remover_estoque(10)
    assert produto.estoque == 0


def test_verificar_numero_positivo(produto):
    with pytest.raises(Exception) as assert_error:
        produto.verificar_numero_positivo(-1)
    assert assert_error.value.args[0] == "O número precisa ser positivo"

def test_verificar_estoque_negativo(produto):
    with pytest.raises(Exception) as assert_error:
        produto.remover_estoque(11)
    assert assert_error.value.args[0] == "O estoque precisa ser maior ou igual a 0"