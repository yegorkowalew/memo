from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)

from django.conf import settings

from pathlib import Path

def get_disp_fullname(file_path):
    try:
        return file_path.partition('Диспетчер')[2].partition(' - ')[2].partition('\\')[0]
    except BaseException as ind:
        logger.error("Error with parse Dispatcher Full Name: %s" % ind)
        return None

def get_disp_smallname(file_path):
    try:
        full = file_path.partition('Диспетчер')[2].partition(' - ')[2].partition('\\')[0]
        return '%s %s.%s.' % (full.partition(' ')[0], full.partition(' ')[2][0], full.partition(' ')[2].partition(' ')[2][0])
    except BaseException as ind:
        logger.error("Error with parse Dispatcher Small Name: %s" % ind)
        return None
    
def get_disp_no(file_path):
    try:
        return file_path.partition('Диспетчер')[2].partition('-')[2].partition(' - ')[0]
    except BaseException as ind:
        logger.error("Error with parse Dispatcher No: %s" % ind)
        return None

def get_names_from_path(path):
    p = Path(path)
    dispatcher_dirs = [str(x) for x in p.iterdir() if x.is_dir()]
    dispatcher_list = [{
        'dispatcher_full_name': get_disp_fullname(x),
        'dispatcher_small_name': get_disp_smallname(x),
        'dispatcher_no': get_disp_no(x),
        } for x in dispatcher_dirs]
    return dispatcher_list

def renew(request):
    # dispatcher_folder = settings.SHEDULE_FOLDER
    for disp in get_names_from_path(settings.SHEDULE_FOLDER):
        print(disp['dispatcher_no'])
    return render(request, 'adm/test.html', {'records': settings.SHEDULE_FOLDER})

# TODO Переделать вьюшку под обновление пользователей из имен папок
# def renew(request):
#     Order.objects.all().delete()
    
#     no_error, records = order_read_file(file_path)
#     if no_error:
#         get_update(records)
#         logger.info("RENEW from file %s with %s user. rows:%s" % (file_path, request.user, len(records)))
#         return render(request, 'adm/on-adm-renew.html', {'lenrecords': len(records)})
#     else:
#         logger.error("Error in page renew from file with %s user" % (request.user))
#         return render(request, 'adm/on-adm-renew.html', {'lenrecords': 'Error'})
    