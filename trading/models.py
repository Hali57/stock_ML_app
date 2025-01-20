from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=10)  # Stock ticker symbol
    name = models.CharField(max_length=50)    # Company name
    last_price = models.FloatField()          # Most recent price
    volume = models.BigIntegerField()         # Trading volume
    date = models.DateField()                 # Data collection date

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10)  # Crypto symbol (e.g., BTC)
    name = models.CharField(max_length=50)    # Cryptocurrency name
    last_price = models.FloatField()          # Most recent price
    market_cap = models.BigIntegerField()     # Market capitalization
    date = models.DateField()                 # Data collection date

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)         # User ID (to be linked later)
    stock_symbol = models.CharField(max_length=10)  # Tracked stock symbol
    crypto_symbol = models.CharField(max_length=10, null=True, blank=True)  # Tracked crypto (optional)
    quantity = models.FloatField()           # Quantity held
    purchase_price = models.FloatField()     # Price at the time of purchase
    purchase_date = models.DateField()       # Date of purchase

    def __str__(self):
        return f"User {self.user_id}'s holdings: {self.quantity} of {self.stock_symbol or self.crypto_symbol}"
