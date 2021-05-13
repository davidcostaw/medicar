from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from backend.especialidades.models import Especialidade
from .serializers import EspecialidadeSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']
