from django.db import models


class PainelInformacoes(models.Model):
    descricao = models.TextField()
    dataCriacao = models.CharField(max_length=12)

    def __str__(self):
        return self.descricao
