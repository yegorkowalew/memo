from django.shortcuts import render

# Create your views here.
from .models import Order

def order_list(request):
    p = 'yo'
    # all_orders = Order.objects.all()[950:1000]
    all_orders = Order.objects.all()
    return render(request, 'order_list.html', {'all_orders': all_orders})