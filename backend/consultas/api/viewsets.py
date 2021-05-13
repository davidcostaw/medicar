from rest_framework import status, viewsets
from rest_framework.response import Response

from backend.consultas.models import Consulta
from .serializers import ConsultaSerializer

from .filters import ConsultaFilter


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = [ConsultaFilter]

    def destroy(self, request, *args, **kwargs):
        consulta = ConsultaFilter().disponivel_para_deletar(request.user.pk, kwargs['pk'])
        if not consulta:
            return Response('Não é possível desmarcar a consulta solicitada!', status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(consulta)

        return Response(status=status.HTTP_200_OK)
