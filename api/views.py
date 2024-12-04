from django.shortcuts import render
import requests

def cotacao_todas_moedas(request):
    url = "https://economia.awesomeapi.com.br/json/all"
    try:
        response = requests.get(url)
        response.raise_for_status()
        cotacoes = response.json()
        return render(request, 'cotacoes.html', {'cotacoes': cotacoes})
    except requests.RequestException as e:
        return render(request, 'error.html', {'error': str(e)})

{
  "USD": {
    "code": "USD",
    "codein": "BRL",
    "name": "Dólar Americano/Real Brasileiro",
    "high": "5.2300",
    "low": "5.1800",
    "varBid": "-0.0200",
    "pctChange": "-0.38",
    "bid": "5.2000",
    "ask": "5.2200",
    "timestamp": "1696941600",
    "create_date": "2024-10-10 10:00:00"
  },
  "EUR": {
    "code": "EUR",
    "codein": "BRL",
    "name": "Euro/Real Brasileiro",
    "high": "5.7500",
    "low": "5.7000",
    "varBid": "-0.0300",
    "pctChange": "-0.52",
    "bid": "5.7200",
    "ask": "5.7400",
    "timestamp": "1696941600",
    "create_date": "2024-10-10 10:00:00"
  }
}
