from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Service, Order
from django.db.models import Q
import yfinance as yf


# Create your views here.

def index(request):
    return render(request, 'index.html')


def show_services(request):
    items_per_page = 2
    services = Service.objects.all()
    paginator = Paginator(services, items_per_page)
    page = request.GET.get('page')
    page_content = paginator.get_page(page)
    return render(request, 'show_services.html', context={'services': page_content})


def show_orders(request):
    # without Q operator:
    # , <> AND
    # with Q operator:
    # & <> AND
    # | <> OR
    orders = Order.objects.filter(
        Q(vehicle__model__brand__startswith='Brand2') | Q(vehicle__model__model__startswith='Model1')
    ).all()
    return render(request, 'show_orders.html', context={'orders': orders})


def show_stock_data(request):
    data = []
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        ticker_object = yf.Ticker(ticker)
        hist = ticker_object.history(period="max")
        data = hist.reset_index().to_dict('records')
        return render(request, 'show_stock_data.html', context={'data': data})
    return render(request, 'show_stock_data.html')
