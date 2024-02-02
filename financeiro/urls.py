from django.urls import path
from .views import FaturaListView

urlpatterns = [
    path('faturas/', FaturaListView.as_view(), name='fatura-list'),
]