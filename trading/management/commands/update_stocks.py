# trading/management/commands/update_stocks.py
from django.core.management.base import BaseCommand # type: ignore
from trading.utils import fetch_and_save_stocks

class Command(BaseCommand):
    help = "Fetches stock data from Yahoo Finance and updates the DB"

    def handle(self, *args, **options):
        # Define the symbols you want to update periodically
        symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']  
        fetch_and_save_stocks(symbols)
        self.stdout.write(self.style.SUCCESS("Stock data updated successfully!"))
