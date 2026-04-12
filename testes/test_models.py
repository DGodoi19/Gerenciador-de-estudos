import pytest
from estudos.models import Trilha, Topico
from django.utils import timezone

@pytest.mark.django_db
def test_trilha_creation():
    trilha = Trilha.objects.create(
        nomeDaTrilha="Teste trilha",
        descricao="Esse é um estudo de teste.",
        semestre=3
    )
    assert trilha.nomeDaTrilha == "Teste trilha"
    assert trilha.descricao == "Esse é um estudo de teste."

@pytest.mark.django_db
def test_topico_str():
    trilha = Trilha.objects.create(
        nomeDaTrilha="Teste trilha",
        descricao="Esse é um estudo de teste."
    )
    topico = Topico.objects.create(
        trilha=trilha,
        nomeDoTopico="Teste tópico",
        descricao="Esse é um tópico de teste."
    )
    assert str(topico) == "Teste tópico - Teste trilha"