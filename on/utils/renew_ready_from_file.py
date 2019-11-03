from on.models import Order
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

import pandas as pd
from django.http import Http404
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)


"""
Готовые заказы
ReadyOrder
"""
RO_FILE = 'C:\\work\\memo\\TESTWORK\\Готовые заказы.xlsx'


def readyOrderReadFile(ro_file):
    try:
        df = pd.read_excel(
            ro_file,
            sheet_name="Готовые заказы",
            usecols=[
                'ID',
                'Готово',
                'Готово Дата'
            ],
            parse_dates=[
                'Готово Дата',
            ],
            dtype={
                'ID': int,
            },
            converters={
                'Готово': bool,
            }
        )

    except Exception as ind:
        logger.error("readyOrderReadFile error with file: %s - %s" %
                     (ro_file, ind))
    else:
        df = df.rename(columns={
            'ID': 'in_id',
            'Готово': 'ready',
            'Готово Дата': 'ready_date',
        }
        )
        df.fillna({'': False})
        df["ready_date"] = pd.to_datetime(df["ready_date"])
        df = df.astype({
            'in_id': 'int64',
            'ready': 'bool',
            'ready_date': 'object',
        })
        df = df.where(df.notnull(), None)
        df_records = df.to_dict('records')
        return df_records


def readyOrderRebuild(sn_file):
    df = readyOrderReadFile(sn_file)
    for r_order in df:
        try:
            order = Order.objects.get(in_id=r_order['in_id'])
        except ObjectDoesNotExist as ind:
            logger.info("Renew ready: {}".format(ind))
        else:
            order.ready = r_order['ready']
            if r_order['ready_date']:
                order.ready_date = r_order['ready_date']
            order.save()


def renew(request):
    readyOrderRebuild(RO_FILE)
    return render(request, 'adm/on-adm-renew-ready.html', {'lenrecords': 'Error'})
