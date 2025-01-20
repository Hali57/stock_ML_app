from rest_framework import serializers #Serializers convert complex data types (like Django models) into JSON and vice versa.
from .models import Stock, Cryptocurrency, Portfolio

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'  # Include all fields of the Stock model

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
        
    def create(self, validated_data):
        # Link the portfolio to the current user automatically
        # if you don't want the user to pass in 'user'
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
