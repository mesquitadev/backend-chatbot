from django.db import models

class Consulta(models.Model):
    especialidade =models.CharField(max_length=100)
    nomeMedico = models.CharField(max_length=100)
    DiaHorario = models.DateTimeField()

    def __str__(self):
        return self.especialidade

# Create your models here.
