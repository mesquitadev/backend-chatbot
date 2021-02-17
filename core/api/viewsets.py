from rest_framework.viewsets import ModelViewSet
from core.models import Paciente
from .serializers import PacienteSerializer
class PacienteViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer