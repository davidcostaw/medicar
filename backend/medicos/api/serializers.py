from rest_framework import serializers
from backend.medicos.models import Medico

from backend.especialidades.api.serializers import EspecialidadeSerializer


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(many=False)

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']
