from django.db import models

from backend.medicos.models import Medico
from backend.agendas.managers import AgendaQuerySet, AgendaDisponivelManager


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField()

    objects = models.Manager()
    disponivel = AgendaDisponivelManager.from_queryset(AgendaQuerySet)()

    class Meta:
        unique_together = ['dia', 'medico']
        ordering = ['dia']

    def __str__(self):
        return str(self.dia)


class HorarioAgenda(models.Model):
    hora = models.TimeField()
    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.PROTECT)
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = ['agenda', 'hora']
        ordering = ['hora']

    def __str__(self):
        return str(self.hora)
