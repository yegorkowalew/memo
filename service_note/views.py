from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render, redirect
from service_note.models import ServiceNote, ReadyOrder, InDocument, Waybill

from append_sn import allRebuild, inDocumentRebuild, readyOrderRebuild, serviceNoteRebuild

import logging
logger = logging.getLogger(__name__)

def sn(request):
    try:
        p = ServiceNote.objects.all()
        logger.info("Page ServiceNote with %s user. Objects:%s" % (request.user, len(p)))
    except ServiceNote.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'sn.html', {'poll': p})

def ro(request):
    try:
        p = ReadyOrder.objects.all()
        logger.info("Page ReadyOrder with %s user. Objects:%s" % (request.user, len(p)))
    except ReadyOrder.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'ro.html', {'poll': p})

def ind(request):
    try:
        p = InDocument.objects.all()
        logger.info("Page InDocument with %s user. Objects:%s" % (request.user, len(p)))
    except InDocument.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'ind.html', {'poll': p})

def wb(request):
    try:
        p = Waybill.objects.all()
        logger.info("Page InDocument with %s user. Objects:%s" % (request.user, len(p)))
    except Waybill.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'wb.html', {'poll': p})

def filereadadmin(request):
    text = 'Файлы, которые можно обновить:'
    try:
        logger.info("Page File Read Admin with %s user." % (request.user))
        bases = [
            {'table':'sn', 'link':'/production/filereadadmin/sn/', 'name':'Служебные записки'},
            {'table':'ro', 'link':'/production/filereadadmin/ro/', 'name':'Готовые заказы'},
            {'table':'ind', 'link':'/production/filereadadmin/ind/', 'name':'График документации'},
            {'table':'all', 'link':'/production/filereadadmin/all/', 'name':'Все'},
        ]
    except:
        raise Http404("Page File Read Admin error")
    return render(request, 'filereadadmin.html', {'update_links': bases, 'text':text})

def filereadadminAll(request):
    if request.user.is_superuser:
        try:
            logger.info("Page File Read Admin with %s user." % (request.user))
            if allRebuild():
                text = 'Обновление файла прошло успешно.'
            else:
                text = 'Что-то пошло не так, подробности в логе.'
            bases = [
                # {'table':'sn', 'link':'/production/filereadadmin/sn/', 'name':'Служебные записки'},
                # {'table':'ro', 'link':'/production/filereadadmin/ro/', 'name':'Готовые заказы'},
                # {'table':'ind', 'link':'/production/filereadadmin/ind/', 'name':'График документации'},
                {'table':'all', 'link':'/production/filereadadmin/all/', 'name':'Все'},
            ]
        except:
            raise Http404("Page File Read Admin error")
        return render(request, 'filereadadmin.html', {'update_links': bases, 'text':text})
    else:
        return redirect('/production/filereadadmin/')