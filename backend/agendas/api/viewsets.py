from rest_framework import viewsets

from backend.agendas.models import Agenda
from .serializers import AgendaSerializer

from backend.agendas.filters import AgendaFilter


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.disponivel.prefetch_horarios_disponiveis()
    serializer_class = AgendaSerializer
    filter_class = AgendaFilter
    filterset_fields = ['medico']
    ordering_fields = ['dia']
