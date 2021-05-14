from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import UsuarioSerializer


class CriarUsuarioViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

