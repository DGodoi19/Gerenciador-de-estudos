import pytest
from estudos.models import Trilha

@pytest.fixture
def trilha_exemplo(db):
    """Cria uma trilha para os testes."""
    return Trilha.objects.create(
        nomeDaTrilha="Engenharia de Software",
        descricao="Estudo de padrões",
        semestre=3
    )
    