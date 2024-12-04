from django.urls import path
from .views import cotacao_todas_moedas

urlpatterns = [
    path('cotacoes/', cotacao_todas_moedas, name='cotacao_todas_moedas'),
]
