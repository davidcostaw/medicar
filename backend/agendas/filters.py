import django_filters

from .models import Agenda
from backend.medicos.models import Medico
from backend.especialidades.models import Especialidade


class AgendaFilter(django_filters.FilterSet):
    medico = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Medico.objects.all()
    )

    medico__especialidade = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Especialidade.objects.all()
    )

    data_inicio = django_filters.DateFilter(field_name='dia', lookup_expr='gte')
    data_final = django_filters.DateFilter(field_name='dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = [
            'medico', 'medico__especialidade', 'data_inicio', 'data_final'
        ]
