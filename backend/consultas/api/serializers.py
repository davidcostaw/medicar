from rest_framework import serializers

from .validators import Validators

from backend.agendas.models import Agenda
from backend.consultas.models import Consulta
from backend.medicos.api.serializers import MedicoSerializer

from datetime import date


class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class ConsultaSerializer(serializers.ModelSerializer):
    agenda_id = serializers.PrimaryKeyRelatedField(
        queryset=Agenda.objects.filter(dia__gte=date.today()),
        write_only=True,
        label='agenda'
    )

    dia = serializers.DateField(read_only=True)

    medico = MedicoSerializer(source='agenda.medico', read_only=True)

    usuario = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento',
                  'medico', 'usuario', 'agenda_id']

    def validate(self, data):

        agenda = data['agenda_id']
        horario = data['horario']

        if Validators().data_expirada(agenda.dia, horario):
            raise serializers.ValidationError(
                "A data e hora informados são menores do que a data e o horário atual!"
            )

        if Validators().mesmo_dia_para_usuario(agenda.dia, horario, data['usuario']):
            raise serializers.ValidationError(
                'O paciente já possui uma consulta marcada para esse dia e horário!'
            )

        if Validators().agenda_em_uso(agenda.pk, horario):
            raise serializers.ValidationError('Essa agenda já está em uso!')

        if not agenda.horarios.filter(disponivel=True, hora=horario).exists():
            raise serializers.ValidationError('O horário solicitado não está disponível!')

        return data

    def create(self, data):

        agenda = data.pop('agenda_id')

        return Consulta.objects.create(
            dia=agenda.dia,
            agenda=agenda,
            usuario=data['usuario'],
            horario=data['horario']
        )

