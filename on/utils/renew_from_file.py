from on.models import OfficeNote, Couterparty, ProductType, Order
import pandas as pd
from django.conf import settings
from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render, redirect
from history.models import History
import logging
logger = logging.getLogger(__name__)

file_path = settings.ORDER_FILE


def order_read_file(sn_file):
    try:
        df = pd.read_excel(
            sn_file,
            sheet_name="СЗ",
            parse_dates=[
                'Отгрузка "от"',
                'Отгрузка "до"',
                'Дата СЗ',
                'Дата СЗ Факт',
                'Комплектовочные План Дата',
                'Отгрузочные План Дата',
                'Конструкторская документация План Дата',
                'Материалы План Дата',
                'Черный металл План Дата',
                'Оцинкованный металл План Дата',
                'Чугун План Дата',
            ],
            dtype={
                'ID': int,
                'Продукция': str,
                'Контрагент': str,
                '№ Заказа': str,
                '№ СЗ': str,
                '№ СЗ с изменениями': str,
                'П/н': str,
                'Тип продукции': str,
            }
        )

    except Exception as ind:
        logger.error("serviceNoteReadFile error with file: %s - %s" %
                     (sn_file, ind))
        return False, None
    else:
        df = df.rename(columns={
            'ID': 'in_id',
            'Отгрузка "от"': 'shipment_from',
            'Отгрузка "до"': 'shipment_before',
            'П/н': 'personal_no',
            'Согласно КП №': 'according_to',
            'Тип продукции': 'pruduct_type',
            'Продукция': 'product_name',
            'Контрагент': 'couterparty',
            '№ Заказа': 'order_no',
            'Кол-во': 'amount',
            '№ СЗ': 'sn_no',
            '№ СЗ с изменениями': 'sn_no_amended',
            'Дата СЗ': 'sn_date',
            'Дата СЗ Факт': 'sn_date_fact',
            'Комплектовочные План Дней': 'pickup_plan_days',
            'Комплектовочные План Дата': 'pickup_plan_date',
            'Отгрузочные План Дней': 'shipping_plan_days',
            'Отгрузочные План Дата': 'shipping_plan_date',
            'Конструкторская документация План Дней': 'design_plan_days',
            'Конструкторская документация План Дата': 'design_plan_date',
            'Материалы План Дней': 'material_plan_days',
            'Материалы План Дата': 'material_plan_date',
            'Черный металл План Дней': 'black_metal_plan_days',
            'Черный металл План Дата': 'black_metal_plan_date',
            'Оцинкованный металл План Дней': 'galvanized_metal_plan_days',
            'Оцинкованный металл План Дата': 'galvanized_metal_plan_date',
            'Чугун План Дней': 'cast_iron_plan_days',
            'Чугун План Дата': 'cast_iron_plan_date',
            'Описание': 'product_text',
        }
        )
        df = df.astype(object)
        df = df.where(df.notnull(), None)
        df_records = df.to_dict('records')
        return True, df_records


def get_sn_obj(count_str):
    obj_list = []
    if count_str:
        for count in count_str.split(', '):
            obj, _ = OfficeNote.objects.get_or_create(name=count)
            obj_list.append(obj)
        return obj_list
    else:
        return None


def get_update(records):
    for record in records:
        obj_counterparty, _ = Couterparty.objects.get_or_create(
            name=record['couterparty'],
        )
        if record['pruduct_type']:
            obj_type, _ = ProductType.objects.get_or_create(
                name=record['pruduct_type'],
            )
        else:
            obj_type = None
        obj_order, _ = Order.objects.get_or_create(
            in_id=record['in_id'],
        )
        obj_order.shipment_from = record['shipment_from']
        obj_order.shipment_before = record['shipment_before']
        obj_order.personal_no = record['personal_no']
        obj_order.according_to = record['according_to']
        obj_order.pruduct_type = obj_type
        obj_order.product_name = record['product_name']
        obj_order.product_text = record['product_text']
        obj_order.couterparty = obj_counterparty
        obj_order.order_no = record['order_no']
        obj_order.amount = record['amount']
        obj_order.sn_date = record['sn_date']
        obj_order.sn_date_fact = record['sn_date_fact']
        obj_order.pickup_plan_days = record['pickup_plan_days']
        obj_order.pickup_plan_date = record['pickup_plan_date']
        obj_order.shipping_plan_days = record['shipping_plan_days']
        obj_order.shipping_plan_date = record['shipping_plan_date']
        obj_order.design_plan_days = record['design_plan_days']
        obj_order.design_plan_date = record['design_plan_date']
        obj_order.material_plan_days = record['material_plan_days']
        obj_order.material_plan_date = record['material_plan_date']
        obj_order.black_metal_plan_days = record['black_metal_plan_days']
        obj_order.black_metal_plan_date = record['black_metal_plan_date']
        obj_order.galvanized_metal_plan_days = record['galvanized_metal_plan_days']
        obj_order.galvanized_metal_plan_date = record['galvanized_metal_plan_date']
        obj_order.cast_iron_plan_days = record['cast_iron_plan_days']
        obj_order.cast_iron_plan_date = record['cast_iron_plan_date']

        # sn_no
        sn_no = get_sn_obj(record['sn_no'])
        if sn_no:
            obj_order.sn_no = sn_no[0]
        # sn_no_amended
        list_sn_no = get_sn_obj(record['sn_no_amended'])
        if list_sn_no:
            obj_order.sn_no_amended.add(*list_sn_no)
        obj_order.save()


def renew_from_file(file_path):
    orders = order_read_file(file_path)
    get_update(orders)


def renew(request):
    Order.objects.all().delete()

    no_error, records = order_read_file(file_path)
    if no_error:
        get_update(records)
        info_text = "Обновлено: %s строк, пользователь: %s, файл: %s" % (
            len(records), request.user, file_path)
        logger.info(info_text)
        History.objects.create(
            icon='far fa-file-excel',
            color='text-success',
            name='Файл: "Служебные записки.xlsx" обновлен.',
            link='/on',
            short_text=info_text,
        )
        return render(request, 'adm/on-adm-renew.html', {'lenrecords': len(records)})
    else:
        info_text = "Ошибка обновления файла %s пользователем %s" % (
            file_path, request.user)
        logger.error(info_text)
        History.objects.create(
            icon='far fa-file-excel',
            color='text-danger',
            name='Файл: "Служебные записки.xlsx" НЕ обновлен.',
            link='/on',
            short_text=info_text,
        )
        return render(request, 'adm/on-adm-renew.html', {'lenrecords': 'Error'})
