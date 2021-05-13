from django.db import models

from backend.especialidades.models import Especialidade


class Medico(models.Model):
    nome = models.CharField(max_length=150, null=False)
    crm = models.IntegerField(unique=True, null=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=80, unique=True, null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
