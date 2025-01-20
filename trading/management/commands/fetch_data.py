from django.core.management.base import BaseCommand # type: ignore
from trading.utils import fetch_and_save_stocks, fetch_and_save_cryptos

class Command(BaseCommand):
    help = "Fetch stock and cryptocurrency data"

    def handle(self, *args, **kwargs):
        tickers = ['AAPL', 'GOOGL', 'MSFT']  # Add more stock symbols as needed
        fetch_and_save_stocks(tickers)
        fetch_and_save_cryptos()
        self.stdout.write("Data fetching completed!")
