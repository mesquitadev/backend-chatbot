from rest_framework.serializers import ModelSerializer
from core.models import Paciente

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'morbidades','Consulta', 'Medicamento' ]
