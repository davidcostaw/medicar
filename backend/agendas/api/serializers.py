from rest_framework import serializers

from backend.agendas.models import Agenda
from backend.medicos.api.serializers import MedicoSerializer


class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    horarios = serializers.StringRelatedField(many=True, source='horarios_disponiveis')

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']
