from rest_framework.viewsets import ModelViewSet
from medicamentos.models import Medicamentos
from .serializers import MedicamentosSerializer

class MedicamentosViewSet(ModelViewSet):

    queryset = Medicamentos.objects.all()
    serializer_class = MedicamentosSerializer