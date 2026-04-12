import pytest
from estudos.models import Trilha, Topico

@pytest.mark.django_db
def test_criacao_trilha_sucesso():
    """1. Cenário de uso correto (Caminho Feliz)"""
    trilha = Trilha.objects.create(
        nomeDaTrilha="Engenharia de Software",
        descricao="Estudo de CI/CD e testes"
    )
    assert trilha.nomeDaTrilha == "Engenharia de Software"
    assert Trilha.objects.count() == 1

@pytest.mark.django_db
def test_topico_str_formatacao():
    """2. Caso de variação importante (Regra de negócio da String)"""
    trilha = Trilha.objects.create(nomeDaTrilha="Django", descricao="Web")
    topico = Topico.objects.create(
        trilha=trilha,
        nomeDoTopico="Modelos",
        descricao="Testando models"
    )
    assert str(topico) == "Modelos - Django"

@pytest.mark.django_db
def test_vinculo_trilha_topico():
    """3. Caso limite: Verificar se tópico exige uma trilha (Integridade)"""
    with pytest.raises(Exception):

        Topico.objects.create(nomeDoTopico="Tópico Órfão")
