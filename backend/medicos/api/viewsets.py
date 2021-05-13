from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from backend.especialidades.filters import MedicoFilter
from backend.medicos.models import Medico
from .serializers import MedicoSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [SearchFilter, MedicoFilter]
    search_fields = ['nome']
