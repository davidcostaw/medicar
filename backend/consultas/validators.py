from datetime import datetime

from backend.consultas.models import Consulta


class Validators:

    def data_expirada(self, dia, hora):
        data_verificada = datetime.strptime(
            f"{dia} {hora}", "%Y-%m-%d %H:%M:%S"
        )
      
        return data_verificada < datetime.today()

    def mesmo_dia_para_usuario(self, dia, hora, user):
        Consulta.objects.filter(
            dia=dia,
            horario=hora,
            usuario=user,
        ).exists()

    def agenda_em_uso(self, agenda, hora):
        Consulta.objects.filter(
            agenda__id=agenda,
            horario=hora,
        ).exists()
