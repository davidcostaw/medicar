from rest_framework.filters import BaseFilterBackend

from django.db.models import Case, Q, Value, When
from datetime import date, datetime

from backend.consultas.models import Consulta
from backend.consultas.validators import Validators


class ConsultaFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        hoje = date.today()
        hora = datetime.now().strftime('%H:%M')

        return queryset.filter(
            usuario=request.user,
            dia__gte=date.today(),
            horario__gte=Case(
                When(
                    Q(agenda__dia=hoje), then=Value(hora)
                ),
                default=Value('00:00')
            )
        )

    def disponivel_para_deletar(self, user, consulta):
        consulta = Consulta.objects.filter(
            pk=consulta,
            usuario=user
        )

        if not consulta.exists():
            return False

        data = consulta.first()

        if Validators().data_expirada(data.dia, data.horario):

            return False

        return consulta
