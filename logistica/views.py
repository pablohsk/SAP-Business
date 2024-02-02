# logistica/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Transportadora, Pedido

class TransportadoraListView(ListView):
    model = Transportadora
    template_name = 'logistica/transportadora_list.html'
    context_object_name = 'transportadoras'

class PedidoListView(ListView):
    model = Pedido
    template_name = 'logistica/pedido_list.html'
    context_object_name = 'pedidos'
