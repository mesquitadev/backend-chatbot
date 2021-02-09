from django.db import models

# Create your models
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    morbidades = models.TextField(max_length=200)

    def __str__(self):
        return self.nome