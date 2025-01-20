from django.urls import path
from .views import PortfolioListCreateView, PortfolioRetrieveUpdateDestroyView, StockListView, StockDetailView, StockRefreshView, CryptocurrencyListView, CryptocurrencyDetailView

urlpatterns = [
    # Stock APIs
    path('api/stocks/', StockListView.as_view(), name='stock-list'),
    path('api/stocks/<str:symbol>/', StockDetailView.as_view(), name='stock-detail'),

    # Refresh stocks
    path('api/stocks/refresh/', StockRefreshView.as_view(), name='stock-refresh'),

    # Cryptocurrency APIs
    path('api/cryptos/', CryptocurrencyListView.as_view(), name='crypto-list'),
    path('api/cryptos/<str:symbol>/', CryptocurrencyDetailView.as_view(), name='crypto-detail'),

    # Portfolio APIs
    path('api/portfolio/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('api/portfolio/<int:pk>/', PortfolioRetrieveUpdateDestroyView.as_view(), name='portfolio-rud'),
]

