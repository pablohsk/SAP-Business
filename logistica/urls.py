from django.urls import path
from .views import TransportadoraListView, PedidoListView

urlpatterns = [
    path('transportadoras/', TransportadoraListView.as_view(), name='transportadora_list'),
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
]