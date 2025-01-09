from django.contrib import admin

# Register your models here.
from .models import Stock, Cryptocurrency, Portfolio

admin.site.register(Stock)
admin.site.register(Cryptocurrency)
admin.site.register(Portfolio)