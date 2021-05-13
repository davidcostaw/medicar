from rest_framework import viewsets

from backend.agendas.models import Agenda
from .serializers import AgendaSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.disponivel.prefetch_horarios_disponiveis()
    serializer_class = AgendaSerializer
