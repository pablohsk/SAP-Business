# logistica/models.py
from django.db import models

class Transportadora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    # Adicione outros campos conforme necessário

class Pedido(models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    data_entrega = models.DateField()
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE)
    # Adicione outros campos conforme necessário
