from datetime import date, datetime

from django.db import models
from django.db.models import Case, Exists, OuterRef, Prefetch, Q, Value, When


class AgendaQuerySet(models.QuerySet):

    def prefetch_horarios_disponiveis(self):
        from .models import HorarioAgenda

        hoje = date.today()
        hora = datetime.now().strftime('%H:%M')

        horarios_disponiveis = (
            HorarioAgenda
            .objects
            .filter(
                disponivel=True,
                hora__gte=Case(
                    When(
                        Q(agenda__dia=hoje), then=Value(hora)
                    ),
                    default=Value('00:00')
                )
            )
        )

        return self.prefetch_related(
            Prefetch('horarios', queryset=horarios_disponiveis)
        )


class AgendaDisponivelManager(models.Manager):

    def get_queryset(self):
        from backend.agendas.models import HorarioAgenda

        hoje = date.today()
        hora = datetime.now().strftime('%H:%M')
        horarios = (
            HorarioAgenda
            .objects
            .filter(
                agenda=OuterRef('pk'),
                disponivel=True,
                hora__gte=Case(
                    When(
                        Q(agenda__dia=hoje), then=Value(hora)
                    ),
                    default=Value('00:00')
                )
            )
        )

        return super().get_queryset().filter(dia__gte=date.today()).filter(Exists(horarios))
