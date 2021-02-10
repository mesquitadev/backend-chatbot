from django.db import models
from consulta.models import Consulta
from medicamentos.models import Medicamentos

# Create your models
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    morbidades = models.TextField(max_length=200)
    consultas = models.ManyToManyField(Consulta)
    medicamentos=models.ManyToManyField(Medicamentos)

    def __str__(self):
        return self.nome
