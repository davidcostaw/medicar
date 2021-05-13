from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=150, unique=True, null=False)

    def __str__(self):
        return self.nome
