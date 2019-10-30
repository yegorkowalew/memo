# -*- coding: utf-8 -*-
""" Модели Заказов """
from django.db import models

from datetime import timedelta  

# TODO считать рабочие дни. То-есть дни кроме сб, вс
"""
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
rr = rrule(DAILY, byweekday=(MO, TU, WE, TH, FR), count = 4)
rr[-1]
datetime.datetime(2019, 11, 4, 13, 50, 46)
"""

def get_plan_date(days, plan_date, sn_date, must):
    """
    Просчет даты по плану
    days - количество дней от даты служебной записки (int)
    plan_date - дата по плану (date)
    sn_date - дата служебной записки (date)
    must - нужно ли выдавать документацию на этот заказ (bool)
    """
    if must:
        try:
            if plan_date:
                # Если дата установлена
                return plan_date, 'Дата установлена в служебной записке.'
            elif days == 0 and sn_date:
                # Если установлено количество дней НОЛЬ! и дата служебной записки
                return sn_date, 'Установлено количество дней НОЛЬ и дата служебной записки (Дата СЗ).'
            elif days and sn_date:
                # Если установлено количество дней и дата служебной записки
                plan_date = sn_date + timedelta(days=days)
                return plan_date, 'Установлено количество дней и дата служебной записки (Дата СЗ + Дни).'
            elif plan_date == None and days == None and sn_date:
                # Не установлены дни и дата выдачи документации по плану. Но установлена дата служебной записки
                return sn_date, 'Не установлены дни и дата по плану. Установлена дата СЗ.'
            elif plan_date == None and days == None and sn_date == None:
                return None, 'Не установлены: дни, дата по плану, дата СЗ.'
        except BaseException as ind:
            return None, "Ошибка: %s" % ind
    else:
        return None, 'Документ не выдается.'

class Order(models.Model):
    """
    Модель Заказа.
    # Поля:
        in_id = 'ID',
        shipment_from = 'Отгрузка "от"',
        shipment_before = 'Отгрузка "до"',
        product_name = 'Продукция',
        couterparty = 'Контрагент',
        number = '№ Заказа',
        amount = 'Кол-во',
        sn_no = "служебные записки",
        sn_no_amended = '№ СЗ',
        sn_date = 'Дата СЗ',
        sn_date_fact = 'Дата СЗ Факт',

        # Комплектовочные
        pickup_must = 'Комплектовочные Выдаются',
        pickup_plan_days = 'Комплектовочные План Дней',
        pickup_plan_date = 'Комплектовочные План Дата',

        # Отгрузочные
        shipping_must = 'Отгрузочные Выдаются',
        shipping_plan_days = 'Отгрузочные План Дней',
        shipping_plan_date = 'Отгрузочные План Дата',

        # Конструкторская документация
        design_must = 'Конструкторская документация Выдается',
        design_plan_days = 'Конструкторская документация План Дней',
        design_plan_date = 'Конструкторская документация План Дата',

        # Материалы
        material_must = 'Материалы Выдаются',
        material_plan_days = 'Материалы План Дней',
        material_plan_date = 'Материалы План Дата',

        # Черный метал
        black_metal_must = 'Черный метал Выдается',
        black_metal_plan_days = 'Черный метал План Дней',
        black_metal_plan_date = 'Черный метал План Дата',

        # Оцинкованный метал
        galvanized_metal_must = 'Оцинкованный метал Выдается',
        galvanized_metal_plan_days = 'Оцинкованный метал План Дней',
        galvanized_metal_plan_date = 'Оцинкованный метал План Дата',

        # Чугун
        galvanized_metal_must = 'Чугун Выдается',
        cast_iron_plan_days = 'Чугун План Дней',
        cast_iron_plan_date = 'Чугун План Дата',

        created = 
        last_updated = 
    """
# * Основное
    in_id = models.IntegerField(
        verbose_name='ID',
        unique=True,
    )
    shipment_from = models.DateField(
        verbose_name='Отгрузка "от"',
        blank=True,
        null=True,
    )
    shipment_before = models.DateField(
        verbose_name='Отгрузка "до"',
        blank=True,
        null=True,
    )
    personal_no = models.CharField(
        verbose_name='П/н',
        max_length=255,
        blank=True,
        null=True,
    )
    according_to = models.CharField(
        verbose_name='Согласно КП №',
        max_length=255,
        blank=True,
        null=True,
    )
    pruduct_type = models.ForeignKey(
        'ProductType',
        verbose_name='Тип продукции',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product_name = models.CharField(
        verbose_name='Продукция',
        max_length=255,
        blank=True,
        null=True,
    )
    product_text = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )
    couterparty = models.ForeignKey(
        'Couterparty',
        verbose_name='Контрагент',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    order_no = models.CharField(
        verbose_name='№ Заказа',
        max_length=255,
        blank=True,
        null=True,
    )
    amount = models.FloatField(
        verbose_name='Кол-во',
        blank=True,
        null=True,
    )
    sn_no = models.ForeignKey(
        'OfficeNote',
        verbose_name='№ СЗ',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='on'
    )
    sn_no_amended = models.ManyToManyField(
        'OfficeNote',
        verbose_name='№ СЗ с изменениями',
        blank=True,
        # null=True,
        related_name='ons'
    )
    sn_date = models.DateField(
        verbose_name='Дата СЗ',
        blank=True,
        null=True,
    )
    sn_date_fact = models.DateField(
        verbose_name='Дата СЗ Факт',
        blank=True,
        null=True,
    )

# * Комплектовочные
    pickup_must = models.BooleanField(
        verbose_name='Комплектовочные Выдаются',
        default=True,
    )
    pickup_plan_days = models.SmallIntegerField(
        verbose_name='Комплектовочные План Дней',
        blank=True,
        null=True,
    )
    pickup_plan_date = models.DateField(
        verbose_name='Комплектовочные План Дата',
        blank=True,
        null=True,
    )
    pickup_fact_date = models.DateField(
        verbose_name='Комплектовочные Факт Дата',
        blank=True,
        null=True,
    )

# * Отгрузочные
    shipping_must = models.BooleanField(
        verbose_name='Отгрузочные Выдаются',
        default=True,
    )
    shipping_plan_days = models.SmallIntegerField(
        verbose_name='Отгрузочные План Дней',
        blank=True,
        null=True,
    )
    shipping_plan_date = models.DateField(
        verbose_name='Отгрузочные План Дата',
        blank=True,
        null=True,
    )
    shipping_fact_date = models.DateField(
        verbose_name='Отгрузочные Факт Дата',
        blank=True,
        null=True,
    )

# * Конструкторская документация
    design_must = models.BooleanField(
        verbose_name='Конструкторская документация Выдается',
        default=True,
    )
    design_plan_days = models.SmallIntegerField(
        verbose_name='Конструкторская документация План Дней',
        blank=True,
        null=True,
    )
    design_plan_date = models.DateField(
        verbose_name='Конструкторская документация План Дата',
        blank=True,
        null=True,
    )
    design_fact_date = models.DateField(
        verbose_name='Конструкторская документация Факт Дата',
        blank=True,
        null=True,
    )

# * Материалы
    material_must = models.BooleanField(
        verbose_name='Материалы Выдаются',
        default=True,
    )
    material_plan_days = models.PositiveSmallIntegerField(
        verbose_name='Материалы План Дней',
        blank=True,
        null=True,
    )
    material_plan_date = models.DateField(
        verbose_name='Материалы План Дата',
        blank=True,
        null=True,
    )
    material_fact_date = models.DateField(
        verbose_name='Материалы Факт Дата',
        blank=True,
        null=True,
    )

# * Черный метал
    black_metal_must = models.BooleanField(
        verbose_name='Черный метал Выдается',
        default=False,
    )
    black_metal_plan_days = models.PositiveSmallIntegerField(
        verbose_name='Черный метал План Дней',
        blank=True,
        null=True,
    )
    black_metal_plan_date = models.DateField(
        verbose_name='Черный метал План Дата',
        blank=True,
        null=True,
    )
    black_metal_fact_date = models.DateField(
        verbose_name='Черный метал Факт Дата',
        blank=True,
        null=True,
    )

# * Оцинкованный метал
    galvanized_metal_must = models.BooleanField(
        verbose_name='Оцинкованный метал Выдается',
        default=False,
    )
    galvanized_metal_plan_days = models.PositiveSmallIntegerField(
        verbose_name='Оцинкованный метал План Дней',
        blank=True,
        null=True,
    )
    galvanized_metal_plan_date = models.DateField(
        verbose_name='Оцинкованный метал План Дата',
        blank=True,
        null=True,
    )
    galvanized_fact_date = models.DateField(
        verbose_name='Оцинкованный метал Факт Дата',
        blank=True,
        null=True,
    )

# * Чугун
    cast_iron_must = models.BooleanField(
        verbose_name='Чугун Выдается',
        default=False,
    )
    cast_iron_plan_days = models.PositiveSmallIntegerField(
        verbose_name='Чугун План Дней',
        blank=True,
        null=True,
    )
    cast_iron_plan_date = models.DateField(
        verbose_name='Чугун План Дата',
        blank=True,
        null=True,
    )
    cast_iron_fact_date = models.DateField(
        verbose_name='Чугун Факт Дата',
        blank=True,
        null=True,
    )

# * Служебные даты
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

# * Мета
    class Meta:
        """Meta definition for OnItm."""

        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        """Unicode representation of OnItm."""
        return ("%s - %s") % (self.order_no, self.product_name)
    
    def get_date_period_small(self):
        """Краткий формат дат отгрузки. Отгрузка: 16.02-18.02.19"""
        if self.shipment_from:
            shipment_from = self.shipment_from.strftime("%d.%m")
            sep = "-"
        else:
            shipment_from = ''
            sep = ""
        if self.shipment_before:
            shipment_before = self.shipment_before.strftime("%d.%m.%y")
        else:
            shipment_before = ''
        return "%s%s%s" % (shipment_from, sep ,shipment_before)
    
    def get_date_period_full(self):
        """Полный формат дат отгрузки. Отгрузка: 16.02.2019-18.02.2019"""
        if self.shipment_from:
            shipment_from = self.shipment_from.strftime("%d.%m.%Y")
            sep = "-"
        else:
            shipment_from = ''
            sep = ""
        if self.shipment_before:
            shipment_before = self.shipment_before.strftime("%d.%m.%Y")
        else:
            shipment_before = ''
        return "%s%s%s" % (shipment_from, sep ,shipment_before)

    def sn_date_diff(self):
        """Разница между датой СЗ и датой получения СЗ."""
        try:
            return (self.sn_date-self.sn_date_fact).days
        except:
            return None

    def pickup_plan_date_count(self):
        return get_plan_date(self.pickup_plan_days, self.pickup_plan_date, self.sn_date, self.pickup_must)

    def shipping_plan_date_count(self):
        return get_plan_date(self.shipping_plan_days, self.shipping_plan_date, self.sn_date, self.shipping_must)

    def design_plan_date_count(self):
        return get_plan_date(self.design_plan_days, self.design_plan_date, self.sn_date, self.design_must)
    
    def material_plan_date_count(self):
        return get_plan_date(self.material_plan_days, self.material_plan_date, self.sn_date, self.material_must)

    def black_metal_plan_date_count(self):
        return get_plan_date(self.black_metal_plan_days, self.black_metal_plan_date, self.sn_date, self.black_metal_must)

    def galvanized_metal_plan_date_count(self):
        return get_plan_date(self.galvanized_metal_plan_days, self.galvanized_metal_plan_date, self.sn_date, self.galvanized_metal_must)

    def cast_iron_plan_date_count(self):
        return get_plan_date(self.cast_iron_plan_days, self.cast_iron_plan_date, self.sn_date, self.cast_iron_must)

    def pickup_fact_date_diff(self):
        if self.pickup_must:
            return '+'
        else:
            return '-'

class Couterparty(models.Model):
    """
    Модель Служебных записок.
    Название обязательное, вводится либо вручную либо автоматически.
    Путь должен парситься автоматически.
    """
# * Поля
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
    )

# * Мета
    class Meta:
        """Meta definition for Couterparty."""

        verbose_name = 'заказчика'
        verbose_name_plural = 'заказчики'

    def __str__(self):
        """Unicode representation of Couterparty."""
        return self.name


class OfficeNote(models.Model):
    """ 
    Служебная записка.
    """

# * Поля
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        # required=True,
        unique=True
    )
    path = models.CharField(
        verbose_name='Путь к файлу',
        max_length=255,
        # path='',
        # path=settings.FILE_PATH_FIELD_DIRECTORY,
        blank=True,
        null=True,
    )

# * Мета
    class Meta:
        """Meta definition for OfficeNote."""

        verbose_name = 'служебную записку'
        verbose_name_plural = 'служебные записки'

    def __str__(self):
        """Unicode representation of OfficeNote."""
        return self.name


class ProductType(models.Model):
    """Model definition for ProductType."""

# * Поля
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True
    )

# * Мета
    class Meta:
        """Meta definition for ProductType."""

        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'

    def __str__(self):
        """Unicode representation of ProductType."""
        return self.name
