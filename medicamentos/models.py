from django.db import models

class Medicamentos(models.Model):

    nomeMedicamento = models.CharField(max_length=100)
    posologiaMedicamento = models.IntegerField()

    def __str__(self):
        return self.nomeMedicamento

