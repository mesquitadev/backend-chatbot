from rest_framework.viewsets import ModelViewSet
from consulta.models import Consulta
from .serializers import ConsultaSerializer
class ConsultasViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer