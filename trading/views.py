from django.shortcuts import render
from rest_framework import generics
from .models import Stock, Cryptocurrency, Portfolio
from .serializers import StockSerializer, CryptocurrencySerializer, PortfolioSerializer

# Create your views here.
# List and retrieve stocks
class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'symbol'  # Allows lookup by stock symbol

# List and retrieve cryptocurrencies
class CryptocurrencyListView(generics.ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

class CryptocurrencyDetailView(generics.RetrieveAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    lookup_field = 'symbol'  # Allows lookup by crypto symbol

# Portfolio management
class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetailView(generics.RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
