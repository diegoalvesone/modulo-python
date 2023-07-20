from jogo_adivinhacao_poo import JogoAdivinhacao
import pytest

@pytest.fixture
def jogo():
  return JogoAdivinhacao(1,100,3);


def test_constructor(jogo):
  assert jogo.limite_inferior == 1;
  assert jogo.limite_superior == 100;
  assert jogo.max_tentativas  == 3;