import json
from django.core.management.base import BaseCommand
from myapp.models import StockData

class Command(BaseCommand):
    help = 'Load stock data from JSON file'

    def handle(self, *args, **options):
        with open('stock_market_data.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                StockData.objects.create(**entry)