from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    NdaConta = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    cpf = models.TextField(max_length=14)
    saldo = models.FloatField(default = 0, null = True)

class Pagamentos(models.Model):
    dia = models.TextField(default = 0)
    hora = models.TextField(default = 0)
    origem = models.TextField(max_length=30)
    destinovalor = models.FloatField(max_length=30)