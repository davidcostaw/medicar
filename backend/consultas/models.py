from django.db import models

from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

from backend.agendas.models import Agenda
from backend.agendas.models import HorarioAgenda

from django.contrib.auth.models import User


class Consulta(models.Model):

    id = models.AutoField(primary_key=True)
    dia = models.DateField()
    agenda = models.ForeignKey(
        Agenda, related_name="Agendas", on_delete=models.CASCADE
    )
    horario = models.TimeField()

    data_agendamento = models.DateTimeField(
        default=timezone.now, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['dia', 'horario']

    def __str__(self):
        return str(self.data_agendamento)


@receiver(post_save, sender=Consulta)
def marcar_horario_como_indisponivel(sender, instance, created, **kwargs):
    if created:
        (
            HorarioAgenda
            .objects
            .filter(agenda__dia=instance.dia, hora=instance.horario)
            .update(disponivel=False)
        )


@receiver(post_delete, sender=Consulta)
def marcar_horario_como_disponivel(sender, instance, **kwargs):
    (
        HorarioAgenda
        .objects
        .filter(agenda__dia=instance.dia, hora=instance.horario)
        .update(disponivel=True)
    )
