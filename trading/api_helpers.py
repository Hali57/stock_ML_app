# A Helper Script for Fetching Data

import yfinance as yf
from .models import Stock

def fetch_stock_data(symbols):
    """
    Fetches data for a list of stock symbols and updates the database.
    """
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            data = stock.info
            Stock.objects.update_or_create(
                symbol=symbol,
                defaults={
                    'name': data.get('shortName', symbol),
                    'price': data.get('regularMarketPrice', 0),
                    'change': data.get('regularMarketChange', 0),
                    'percentage_change': data.get('regularMarketChangePercent', 0),
                },
            )
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
