from django.shortcuts import render
from django.views.generic import ListView
from .models import Transacao, Conta, Fatura


def lista_transacoes(request):
    transacoes = Transacao.objects.all()
    return render(request, 'financeiro/lista_transacoes.html', {'transacoes': transacoes})


def lista_contas(request):
    contas = Conta.objects.all()
    return render(request, 'financeiro/lista_contas.html', {'contas': contas})


class FaturaListView(ListView):
    model = Fatura
    template_name = 'financeiro/lista_faturas.html'
    context_object_name = 'faturas'
