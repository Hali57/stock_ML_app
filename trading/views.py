from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock, Cryptocurrency, Portfolio
from .serializers import StockSerializer, CryptocurrencySerializer, PortfolioSerializer
from .utils import fetch_and_save_stocks, fetch_and_save_cryptos

# Create your views here.
# List and retrieve stocks
    

class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class StockRefreshView(APIView):
    """
    Refreshes data for given stock symbols from the external API
    and updates the DB. Then returns a success response.
    """
    def post(self, request, *args, **kwargs):
        symbols = request.data.get('symbols', [])
        if not symbols:
            return Response({"error": "No symbols provided."}, status=400)

        # Fetch the data from yfinance (or whichever library you're using)
        fetch_and_save_stocks(symbols)

        return Response({"detail": "Stock data refreshed."}, status=200)
    


class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'symbol'  # Allows lookup by stock symbol

# List and retrieve cryptocurrencies
class CryptocurrencyListView(generics.ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer


class CryptoRefreshView(APIView):
    """
    Refreshes data for given crypto symbols from the external API
    and updates the DB. Then returns a success response.
    """
    def post(self, request, *args, **kwargs):
        symbols = request.data.get('symbols', [])
        if not symbols:
            return Response({"error": "No symbols provided."}, status=400)

        # Fetch the data from yfinance (or whichever library you're using)
        fetch_and_save_cryptos(symbols)

        return Response({"detail": "Crypto data refreshed."}, status=200)
    

class CryptocurrencyDetailView(generics.RetrieveAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    lookup_field = 'symbol'  # Allows lookup by crypto symbol

# Portfolio management

class PortfolioListCreateView(generics.ListCreateAPIView):
    """
    Lists all portfolio items for the current user,
    and allows creating new holdings.
    """
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only the portfolio entries for the logged-in user
        return Portfolio.objects.filter(user=self.request.user)

class PortfolioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific portfolio entry by ID.
    """
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only retrieve entries belonging to the current user
        return Portfolio.objects.filter(user=self.request.user)