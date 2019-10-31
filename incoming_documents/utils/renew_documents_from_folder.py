from pathlib import Path
# from django.conf import settings
# from django.contrib.auth.models import User
# from user_profile.models import Profile
from django.shortcuts import render
import pandas as pd
import os
import time
from user_profile.utils.renew_user_from_folder import get_dispatcher_from_path

from incoming_documents.models import DocumentDate
from on.models import Order

import logging
logger = logging.getLogger(__name__)

file_path = 'C:\\work\\memo\\TESTWORK\\График документации\\Диспетчер-4 - Пирлик Інна Іванівна\\График документации.xlsx'
file = 'График документации.xlsx'
path = 'C:\\work\\memo\\TESTWORK\\График документации\\Диспетчер-4 - Пирлик Інна Іванівна'


def inDocumentReadFile(path, file_name):
    try:
        df = pd.read_excel(
            os.path.join(path, file_name),
            sheet_name="Документация",
            usecols=[
                'ID',
                'Комплектовочные Выдача',
                'Комплектовочные Дата 1',
                'Комплектовочные Дата 2',
                'Комплектовочные Дата 3',
                'Отгрузочные Выдача',
                'Отгрузочные Дата 1',
                'Отгрузочные Дата 2',
                'Отгрузочные Дата 3',
                'Конструкторские Выдача',
                'Конструкторские Дата 1',
                'Конструкторские Дата 2',
                'Конструкторские Дата 3',
                'Изменения чертежей Выдача',
                'Изменения чертежей Дата 1',
                'Изменения чертежей Дата 2',
                'Изменения чертежей Дата 3'
            ],

            parse_dates=[
                'Комплектовочные Дата 1',
                'Комплектовочные Дата 2',
                'Комплектовочные Дата 3',
                'Отгрузочные Дата 1',
                'Отгрузочные Дата 2',
                'Отгрузочные Дата 3',
                'Конструкторские Дата 1',
                'Конструкторские Дата 2',
                'Конструкторские Дата 3',
                'Изменения чертежей Дата 1',
                'Изменения чертежей Дата 2',
                'Изменения чертежей Дата 3'
            ],

            dtype={
                'ID': int,
            },
            converters={
                'Готово': bool,
                'Комплектовочные Выдача': bool,
                'Отгрузочные Выдача': bool,
                'Конструкторские Выдача': bool,
                'Изменения чертежей Выдача': bool,
            }
        )

    except Exception as ind:
        logger.error("inDocumentReadFile error with file: %s - %s" %
                     (file_name, ind))
    else:
        df = df.rename(columns={
            'ID': 'in_id',
            'Диспетчер': 'dispatcher',
            'Комплектовочные Выдача': 'pickup_issue',
            'Комплектовочные Дата 1': 'pickup_date_1',
            'Комплектовочные Дата 2': 'pickup_date_2',
            'Комплектовочные Дата 3': 'pickup_date_3',
            'Отгрузочные Выдача': 'shipping_issue',
            'Отгрузочные Дата 1': 'shipping_date_1',
            'Отгрузочные Дата 2': 'shipping_date_2',
            'Отгрузочные Дата 3': 'shipping_date_3',
            'Конструкторские Выдача': 'design_issue',
            'Конструкторские Дата 1': 'design_date_1',
            'Конструкторские Дата 2': 'design_date_2',
            'Конструкторские Дата 3': 'design_date_3',
            'Изменения чертежей Выдача': 'drawings_issue',
            'Изменения чертежей Дата 1': 'drawings_date_1',
            'Изменения чертежей Дата 2': 'drawings_date_2',
            'Изменения чертежей Дата 3': 'drawings_date_3'
        }
        )
        df['dispatcher'] = os.path.split(path)[-1]
        df['pickup_date_1'] = pd.to_datetime(df['pickup_date_1'])
        df['pickup_date_2'] = pd.to_datetime(df['pickup_date_2'])
        df['pickup_date_3'] = pd.to_datetime(df['pickup_date_3'])
        df['shipping_date_1'] = pd.to_datetime(df['shipping_date_1'])
        df['shipping_date_2'] = pd.to_datetime(df['shipping_date_2'])
        df['shipping_date_3'] = pd.to_datetime(df['shipping_date_3'])
        df['design_date_1'] = pd.to_datetime(df['design_date_1'])
        df['design_date_2'] = pd.to_datetime(df['design_date_2'])
        df['design_date_3'] = pd.to_datetime(df['design_date_3'])
        df['drawings_date_1'] = pd.to_datetime(df['drawings_date_1'])
        df['drawings_date_2'] = pd.to_datetime(df['drawings_date_2'])
        df['drawings_date_3'] = pd.to_datetime(df['drawings_date_3'])

        df = df.astype({
            'pickup_date_1': 'object',
            'pickup_date_2': 'object',
            'pickup_date_3': 'object',
            'shipping_date_1': 'object',
            'shipping_date_2': 'object',
            'shipping_date_3': 'object',
            'design_date_1': 'object',
            'design_date_2': 'object',
            'design_date_3': 'object',
            'drawings_date_1': 'object',
            'drawings_date_2': 'object',
            'drawings_date_3': 'object',
        })
        df = df.where(df.notnull(), None)
        df = df.to_dict('records')
        return df


def inDocumentFindFile(in_folder, need_file):
    tree = os.walk(in_folder)
    folder_list = []
    for i in tree:
        for address, dirs, files in [i]:
            for fl in files:
                if fl == need_file:
                    folder_list.append(address)
    return folder_list


def inDocumentRebuild(in_folder, need_file, m_obj):
    t = time.time()
    m_obj.objects.all().delete()
    logger.info(
        "Clear DBTable: {} - {:.3}".format(m_obj.__name__, (time.time()-t)))

    for folder in inDocumentFindFile(in_folder, need_file):
        t = time.time()
        df = inDocumentReadFile(folder, need_file)
        logger.info(
            "Convert to Table: {} - {:.3}".format(m_obj.__name__, (time.time()-t)))
        t = time.time()
        insertToDB(df, m_obj)
        logger.info(
            "Insert to DBTable: {} - {:.3}".format(m_obj.__name__, (time.time()-t)))


"""
{
    'in_id': 1216, 
    'pickup_issue': False, 
    'pickup_date_1': None, 
    'pickup_date_2': None, 
    'pickup_date_3': None, 
    'shipping_issue': False, 
    'shipping_date_1': None, 
    'shipping_date_2': None, 
    'shipping_date_3': None, 
    'design_issue': False, 
    'design_date_1': None, 
    'design_date_2': None, 
    'design_date_3': None, 
    'drawings_issue': False, 
    'drawings_date_1': None, 
    'drawings_date_2': None, 
    'drawings_date_3': None, 
    'dispatcher': 'Диспетчер-4 - Пирлик Інна Іванівна'

    DOCUMENT_TYPE_CHOICES = [
        ('pickup_fact_date', 'Комплектовочные Факт Дата'),
        ('shipping_fact_date', 'Отгрузочные Факт Дата'),
        ('design_fact_date', 'Конструкторская документация Факт Дата'),
        ('material_fact_date', 'Материалы Факт Дата'),
        ('black_metal_fact_date', 'Черный метал Факт Дата'),
        ('galvanized_fact_date', 'Оцинкованный метал Факт Дата'),
        ('cast_iron_fact_date', 'Чугун Факт Дата'),
    ]
 
}
"""
# dispatcher
# order
# document_type DOCUMENT_TYPE_CHOICES
# date


def renew(request):
    dates = inDocumentReadFile(path, file)

    dispatcher = get_dispatcher_from_path(file_path)
    for date_d in dates:
        try:
            order = Order.objects.get(in_id=int(date_d['in_id']))
            order.pickup_must = date_d['pickup_issue']
            order.shipping_must = date_d['shipping_issue']
            order.design_must = date_d['design_issue']
            order.save()

        except BaseException as ind:
            logger.error("Ошибка добавления документа. ID: %s - %s" %
                         (date_d['in_id'], ind))
    return render(request,
                  'adm/renew-documents.html', {
                      'dispatcher': dispatcher,
                      'dd': dates
                  }
                  )
