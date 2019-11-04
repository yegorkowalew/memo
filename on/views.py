from django.shortcuts import render

# Create your views here.
from .models import Order
from incoming_documents.models import DocumentDate

from django.db.models import Q


def dashboard(request):
    orders = Order.objects.all().count()

    ready_orders = Order.objects.filter(ready=True).count()
    ready_orders_percent = int(ready_orders*100/orders)

    process_orders = Order.objects.filter(ready=False).count()
    process_orders_percent = int(process_orders*100/orders)
    graf = {
        'ready_orders': ready_orders,
        'ready_orders_percent': ready_orders_percent,
        'process_orders': process_orders,
        'process_orders_percent': process_orders_percent
    }
    return render(request, 'dashboard.html', {
        'alerts': 'alerts',
        'messages': 11,
        'title': 'Главная страница',
        'graf': graf
    })

def adm_index(request):
    orders = Order.objects.all().count()

    ready_orders = Order.objects.filter(ready=True).count()
    ready_orders_percent = int(ready_orders*100/orders)

    process_orders = Order.objects.filter(ready=False).count()
    process_orders_percent = int(process_orders*100/orders)
    graf = {
        'ready_orders': ready_orders,
        'ready_orders_percent': ready_orders_percent,
        'process_orders': process_orders,
        'process_orders_percent': process_orders_percent
    }
    return render(request, 'adm/adm_index.html', {
        'alerts': 'alerts',
        'messages': 11,
        'title': 'Главная страница',
        'graf': graf
    })

def order_list(request):
    # p = 'yo'
    # order = Order.objects.get(in_id=8)
    # print(order)
    # all_dates = DocumentDate.objects.filter(order=order, document_type='pickup_fact_date')
    # last_date = DocumentDate.objects.filter(order=order, document_type='pickup_fact_date').order_by('date')[0].date
    # print(all_dates[0].date)
    # for al in all_dates:
    #     print(al.date)
    # print(last_date)
    all_orders = Order.objects.all()
    return render(request, 'order_list.html', {'all_orders': all_orders})
