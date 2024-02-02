from django.shortcuts import render
from django.views import View
from .models import Pagamento

class PagamentoListView(View):
    def get(self, request):
        pagamentos = Pagamento.objects.all()
        return render(request, 'pagamentos/lista_pagamentos.html', {'pagamentos': pagamentos})