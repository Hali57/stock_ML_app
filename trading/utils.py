import requests
import yfinance as yf
from .models import Stock ,Cryptocurrency
from datetime import datetime

def fetch_and_save_stocks(tickers):
    """
    Fetch stock data for given ticker symbols and save to the database.
    """
    for ticker in tickers:
        try:
            stock_data = yf.Ticker(ticker)
            info = stock_data.history(period="1d")  # Fetch the latest day of data
            if not info.empty:
                latest_data = info.iloc[-1]
                Stock.objects.update_or_create(
                    symbol=ticker,
                    defaults={
                        'name': stock_data.info.get('shortName', 'N/A'),
                        'last_price': latest_data['Close'],
                        'volume': latest_data['Volume'],
                        'date': datetime.now().date(),
                    }
                )
                print(f"Updated data for {ticker}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")



def fetch_and_save_cryptos():
    """
    Fetch cryptocurrency data from CoinGecko and save to the database.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,  # Top 10 cryptocurrencies
        'page': 1,
        'sparkline': False,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        for crypto in data:
            Cryptocurrency.objects.update_or_create(
                symbol=crypto['symbol'].upper(),
                defaults={
                    'name': crypto['name'],
                    'last_price': crypto['current_price'],
                    'market_cap': crypto['market_cap'],
                    'date': datetime.now().date(),
                }
            )
            print(f"Updated data for {crypto['name']}")
    except Exception as e:
        print(f"Error fetching cryptocurrency data: {e}")