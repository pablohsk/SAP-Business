from django.db import models

class Transacao(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

class Conta(models.Model):
    nome = models.CharField(max_length=255)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    transacoes = models.ManyToManyField(Transacao)

class Fatura(models.Model):
    numero = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()