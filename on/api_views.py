from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order

import datetime
from datetime import timedelta


@api_view()
def ongraph(request):
    orders_dict = []
    orders = Order.objects.all().count()

    ready_orders = Order.objects.filter(ready=True).count()
    ready_orders_percent = int(ready_orders*100/orders)
    orders_dict.append({
        'name':'Готовые заказы',
        'url':'/on/orders/ready_orders',
        'bgcolor':'bg-info',
        'orders':ready_orders,
        'orders_percent':ready_orders_percent
    })
    
    in_production_orders = Order.objects.filter(ready=False).count()
    in_production_orders_percent = int(in_production_orders*100/orders)
    orders_dict.append({
        'name':'В производстве',
        'url':'/on/orders/in_production_orders',
        'bgcolor':'bg-info',
        'orders':in_production_orders,
        'orders_percent':in_production_orders_percent
    })

    startdate = datetime.datetime.now()
    enddate = startdate + timedelta(days=10)
    less_ten_days_orders = Order.objects.filter(
        shipment_before__range=[startdate, enddate]).count()
    less_ten_days_orders_percent = int(less_ten_days_orders*100/orders)
    orders_dict.append({
        'name':'Меньше 10 дней до отгрузки',
        'url':'/on/orders/less_ten_days_orders',
        'bgcolor':'bg-info',
        'orders':less_ten_days_orders,
        'orders_percent':less_ten_days_orders_percent
    })

    late_orders = Order.objects.filter(
        shipment_before__gte=startdate, ready=False).count()
    late_orders_percent = int(late_orders*100/orders)
    orders_dict.append({
        'name':'Просроченные заказы',
        'url':'/on/orders/late_orders',
        'bgcolor':'bg-info',
        'orders':late_orders,
        'orders_percent':late_orders_percent
    })
    
    return Response({"orders": orders_dict})