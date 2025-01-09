from django.urls import path
from .views import StockListView, StockDetailView, CryptocurrencyListView, CryptocurrencyDetailView, PortfolioListView, PortfolioDetailView

urlpatterns = [
    # Stock APIs
    path('api/stocks/', StockListView.as_view(), name='stock-list'),
    path('api/stocks/<str:symbol>/', StockDetailView.as_view(), name='stock-detail'),

    # Cryptocurrency APIs
    path('api/cryptos/', CryptocurrencyListView.as_view(), name='crypto-list'),
    path('api/cryptos/<str:symbol>/', CryptocurrencyDetailView.as_view(), name='crypto-detail'),

    # Portfolio APIs
    path('api/portfolio/', PortfolioListView.as_view(), name='portfolio-list'),
    path('api/portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]
