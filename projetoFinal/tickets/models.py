from django.db import models

class Tickets(models.Model):
    #nome = models.CharField(max_length=150)
    descricao = models.TextField()
    dataCriacao = models.DateField
    dataFim = models.DateField
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.descricao
