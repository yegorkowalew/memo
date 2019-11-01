from pathlib import Path
from django.shortcuts import render
import pandas as pd
import os
import time
from user_profile.utils.renew_user_from_folder import get_dispatcher_from_path, renew_profile

from incoming_documents.models import DocumentDate
from on.models import Order

import logging
logger = logging.getLogger(__name__)

file_path = 'C:\\work\\memo\\TESTWORK\\График документации\\Диспетчер-4 - Пирлик Інна Іванівна\\График документации.xlsx'
file = 'График документации.xlsx'
path = 'C:\\work\\memo\\TESTWORK\\График документации\\Диспетчер-4 - Пирлик Інна Іванівна\\'


def inDocumentReadFile(file_path):
    try:
        df = pd.read_excel(
            file_path,
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
                     (file_path, ind))
    else:
        df = df.rename(columns={
            'ID': 'in_id',
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
# must
# document_type DOCUMENT_TYPE_CHOICES
# date


def renew_all_documents_from_dispatcher(file_path):
    def create_date(dispatcher, order, must, document_type, date):
        document_date = DocumentDate(
            dispatcher=dispatcher,
            order = order,
            must = must,
            document_type = document_type,
            date = date
        )
        document_date.save()        

    dates = inDocumentReadFile(file_path)
    dispatcher_dict = get_dispatcher_from_path(file_path)
    dispatcher = renew_profile(dispatcher_dict)
    DocumentDate.objects.filter(dispatcher=dispatcher).delete()
    for date_d in dates:
        try:
            # TODO разобраться с документами, что такое изменение чертежей, что такое конструкторская документация
            order = Order.objects.get(in_id=int(date_d['in_id']))
            if date_d['pickup_date_1']:
                create_date(dispatcher, order, date_d['pickup_issue'], 'pickup_fact_date', date_d['pickup_date_1'])

            if date_d['pickup_date_2']:
                create_date(dispatcher, order, date_d['pickup_issue'], 'pickup_fact_date', date_d['pickup_date_2'])

            if date_d['pickup_date_3']:
                create_date(dispatcher, order, date_d['pickup_issue'], 'pickup_fact_date', date_d['pickup_date_3'])

            if date_d['shipping_date_1']:
                create_date(dispatcher, order, date_d['shipping_issue'], 'shipping_fact_date', date_d['shipping_date_1'])

            if date_d['shipping_date_2']:
                create_date(dispatcher, order, date_d['shipping_issue'], 'shipping_fact_date', date_d['shipping_date_2'])

            if date_d['shipping_date_3']:
                create_date(dispatcher, order, date_d['shipping_issue'], 'shipping_fact_date', date_d['shipping_date_3'])

            if date_d['design_date_1']:
                create_date(dispatcher, order, date_d['design_issue'], 'design_fact_date', date_d['design_date_1'])

            if date_d['design_date_2']:
                create_date(dispatcher, order, date_d['design_issue'], 'design_fact_date', date_d['design_date_2'])

            if date_d['design_date_3']:
                create_date(dispatcher, order, date_d['design_issue'], 'design_fact_date', date_d['design_date_3'])
            
        except BaseException as ind:
            logger.error("Ошибка добавления документа. ID: %s - %s" %
                         (date_d['in_id'], ind))
    return True

def renew(request):
    # renew_all_documents_from_dispatcher(file_path)

    return render(request,
                  'adm/renew-documents.html', {

                  }
                  )
