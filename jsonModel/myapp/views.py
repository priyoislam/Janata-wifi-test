from django.shortcuts import render
from .models import StockMarketData


def stock_data(request):
    data = StockMarketData.objects.all()
    # form = StockMarketDataForm()

    # if request.method == 'POST':
    #     form = StockMarketDataForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    return render(request, 'stock_data.html', {'data': data})