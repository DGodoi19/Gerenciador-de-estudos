from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Trilha(models.Model):
    nomeDaTrilha = models.CharField("Nome da trilha", max_length=100)
    descricao = models.TextField("Descrição")
    semestre = models.IntegerField(
        "Semestre",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=3
    )
    criado_em = models.DateTimeField("Criado em",auto_now_add=True)
    concluido = models.BooleanField("Concluído", default=False)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.nomeDaTrilha} ({self.semestre}º sem)"

class Topico(models.Model):
    trilha = models.ForeignKey(Trilha, on_delete=models.CASCADE, related_name='topicos')
    nomeDoTopico = models.CharField("Nome do tópico", max_length=100)
    descricao = models.TextField("Descrição")
    concluido = models.BooleanField("Concluído", default=False)

    def __str__(self):
        return f"{self.nomeDoTopico} - {self.trilha.nomeDaTrilha}"
