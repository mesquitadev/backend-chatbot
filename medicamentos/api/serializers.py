from rest_framework.serializers import ModelSerializer
from core.models import Medicamentos

class MedicamentosSerializer(ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = ('id', 'nomeMedicamento', 'posologiaMedicamento')
