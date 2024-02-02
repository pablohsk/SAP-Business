from django.db import models

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()