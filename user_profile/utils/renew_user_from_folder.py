from pathlib import Path
from django.conf import settings
from django.contrib.auth.models import User
from user_profile.models import Profile
from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)


def get_disp_fullname(file_path):
    """По пути возвращаем ФИО пользователя"""
    try:
        return file_path.partition('Диспетчер')[2].partition(' - ')[2].partition('\\')[0]
    except BaseException as ind:
        logger.error("Error with parse Dispatcher Full Name: %s" % ind)
        return None


def get_disp_smallname(file_path):
    """По пути возвращаем Фамилию, инициалы пользователя"""
    try:
        full = file_path.partition('Диспетчер')[2].partition(
            ' - ')[2].partition('\\')[0]
        return '%s %s.%s.' % (full.partition(' ')[0], full.partition(' ')[2][0], full.partition(' ')[2].partition(' ')[2][0])
    except BaseException as ind:
        logger.error("Error with parse Dispatcher Small Name: %s" % ind)
        return None


def get_disp_no(file_path):
    """По пути возвращаем Номер диспетчера"""
    try:
        return file_path.partition('Диспетчер')[2].partition('-')[2].partition(' - ')[0]
    except BaseException as ind:
        logger.error("Error with parse Dispatcher No: %s" % ind)
        return None


def get_dispatcher_from_path(path):
    """По пути возвращаем кортеж такого вида:
    - Ф.И.О диспетчера
    - Фамилию, инициалы диспетчера
    - Номер диспетчера"""
    dispatcher = {
        'full_name': get_disp_fullname(path),
        'small_name': get_disp_smallname(path),
        'no': get_disp_no(path),
    }
    return dispatcher


def get_dispatchers_from_path(path):
    """По пути возвращаем список кортежей диспетчеров
    - Ф.И.О диспетчера
    - Фамилию, инициалы диспетчера
    - Номер диспетчера"""
    p = Path(path)
    dispatcher_dirs = [str(x) for x in p.iterdir() if x.is_dir()]
    dispatcher_list = [get_dispatcher_from_path(x) for x in dispatcher_dirs]
    return dispatcher_list


def renew_profile(dispatcher):
    """Получаем кортеж диспетчера,
    если такого диспетчера нет, создаем пользователя и профиль.
    Возвращаем пользователя.
    """
    try:
        profile = Profile.objects.get(
            fullname=dispatcher['full_name'])
        logger.info("Пользователь: %s существует." % profile.fullname)
        return profile
    except BaseException as ind:
        logger.info("Пользователь: %s не существует. Создаем." %
                    dispatcher['full_name'])
        # Создал пользователя и сохранил его в базе данных
        user = User.objects.create_user(dispatcher['small_name'], '', '')

        # Обновил поля и сохранил их снова
        user.first_name = dispatcher['full_name'].split(' ')[1]
        user.last_name = dispatcher['full_name'].split(' ')[0]
        user.profile.fullname = dispatcher['full_name']
        user.profile.fullname_small = dispatcher['small_name']
        user.profile.user_no = dispatcher['no']
        user.save()
        return user.profile


def renew_profiles(path):
    """Получаем путь к папке, обновляем профили пользователей
    или создаем новые.
    """
    for dispatcher in get_dispatchers_from_path(path):
        renew_profile(dispatcher)


def renew(request):
    renew_profiles(settings.SHEDULE_FOLDER)
    return render(request, 'adm/test.html', {'records': settings.SHEDULE_FOLDER})
