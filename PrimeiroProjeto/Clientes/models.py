from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()
    ativo = models.BooleanField(default=True)


