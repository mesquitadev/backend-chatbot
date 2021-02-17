from rest_framework.serializers import ModelSerializer
from consulta.models import Consulta

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('id', 'especialidade', 'nomeMedico', 'DiaHorario')
