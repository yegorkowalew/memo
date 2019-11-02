from django.shortcuts import render

# Create your views here.
from .models import Order
from incoming_documents.models import DocumentDate

from django.db.models import Q


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
