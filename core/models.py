from django.db import models
from consulta.models import Consulta
from medicamentos.models import Medicamentos
# Create your models
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    morbidades = models.TextField(max_length=200)
    Consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    Medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
