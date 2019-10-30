""" models for parsed files"""
from django.db import models
from django.urls import reverse


class ServiceNote(models.Model):
    """
    Добавить поля с комментариями и типом производимого устройства
    # Fields:
    ID
    Порядковый номер
    Отгрузка "от"
    Отгрузка "до"
    Продукция
    Контрагент
    № Заказа
    Кол-во
    № СЗ
    № СЗ с изменениями
    Дата СЗ
    Дата СЗ Факт
    Комплектовочные План Дней
    Комплектовочные План Дата
    Отгрузочные План Дней
    Отгрузочные План Дата
    Конструкторская документация План Дней
    Конструкторская документация План Дата
    Материалы План Дней
    Материалы План Дата
    Черный металл План Дней
    Черный металл План Дата
    Оцинкованный металл План Дней
    Оцинкованный металл План Дата
    Чугун План Дней
    Чугун План Дата
    """
    in_id = models.IntegerField(
        verbose_name='ID',
        unique=True,
    )
    in_sn_no = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер',
        blank=True,
        null=True,
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

    product_name = models.CharField(
        verbose_name='Продукция',
        max_length=255,
    )
    counterparty = models.CharField(
        verbose_name='Контрагент',
        max_length=255,
    )
    order_no = models.PositiveIntegerField(
        verbose_name='№ Заказа',
        blank=True,
        null=True,
    )
    amount = models.FloatField(
        verbose_name='Кол-во',
        null=True,
    )

    sn_no = models.PositiveIntegerField(
        verbose_name='№ СЗ',
        blank=True,
        null=True,
    )
    sn_no_amended = models.CharField(
        verbose_name='№ СЗ с изменениями',
        max_length=255,
        blank=True,
        null=True,
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
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ["in_id"]
        verbose_name = "служебную записку"
        verbose_name_plural = "служебные записки"

    def __str__(self):
        return str("%s - %s" % (self.in_id, self.product_name))

    def get_absolute_url(self):
        """mem_ServiceNote_detail"""
        return reverse("mem_ServiceNote_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_ServiceNote_update"""
        return reverse("mem_ServiceNote_update", args=(self.pk,))


class OperativeNote(models.Model):
    """
    Выкинуть из этого приложения
    # Fields:
    Отгрузка "от"
    Отгрузка "до"
    Продукция
    Контрагент
    № Заказа
    Кол-во
    № СЗ
    № СЗ с изменениями
    Дата СЗ
    Дата СЗ Факт
    Комплектовочные Дата План
    Отгрузочные Дата План
    Конструкторская документация Дата План
    Материалы Дата План
    Черный металл Дата План
    Оцинкованный металл Дата План
    Чугун Дата План
    """
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
    product_name = models.CharField(
        verbose_name='Продукция',
        max_length=255,
    )
    counterparty = models.CharField(
        verbose_name='Контрагент',
        max_length=255,
    )
    order_no = models.PositiveIntegerField(
        verbose_name='№ Заказа',
        blank=True,
        null=True,
    )
    amount = models.FloatField(
        verbose_name='Кол-во',
        null=True,
    )
    sn_no = models.PositiveIntegerField(
        verbose_name='№ СЗ',
        blank=True,
        null=True,
    )
    sn_no_amended = models.CharField(
        verbose_name='№ СЗ с изменениями',
        max_length=255,
        blank=True,
        null=True,
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
    pickup_plan_date = models.DateField(
        verbose_name='Комплектовочные Дата План',
        blank=True,
        null=True,
    )
    shipping_plan_date = models.DateField(
        verbose_name='Отгрузочные Дата План',
        blank=True,
        null=True,
    )
    design_plan_date = models.DateField(
        verbose_name='Конструкторская документация Дата План',
        blank=True,
        null=True,
    )
    material_plan_date = models.DateField(
        verbose_name='Материалы Дата План',
        blank=True,
        null=True,
    )
    black_metal_plan_date = models.DateField(
        verbose_name='Черный метал Дата План',
        blank=True,
        null=True,
    )
    galvanized_metal_plan_date = models.DateField(
        verbose_name='Оцинкованный метал Дата План',
        blank=True,
        null=True,
    )
    cast_iron_plan_date = models.DateField(
        verbose_name='Чугун Дата План',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "оперативную записку"
        verbose_name_plural = "оперативные записки"

    def __str__(self):
        return str("%s - %s" % (self.in_id, self.product_name))

    def get_absolute_url(self):
        """mem_OperativeNote_detail"""
        return reverse("mem_OperativeNote_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_OperativeNote_update"""
        return reverse("mem_OperativeNote_update", args=(self.pk,))


class ReadyOrder(models.Model):
    """
    ReadyOrder
    # Fields:
    ID
    Готово
    Готово Дата
    """
    in_id = models.IntegerField(
        verbose_name='ID',
        unique=True,
    )

    ready = models.BooleanField(
        verbose_name='Готово',
        blank=True,
        null=True,
    )
    ready_date = models.DateField(
        verbose_name='Готово Дата',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "готовый заказ"
        verbose_name_plural = "готовые заказы"

    def __str__(self):
        return str("%s - %s" % (self.pk, self.pk))

    def get_absolute_url(self):
        """mem_ReadyOrder_detail"""
        return reverse("mem_ReadyOrder_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_ReadyOrder_update"""
        return reverse("mem_ReadyOrder_update", args=(self.pk,))


class InDocument(models.Model):
    """
    InDocument
    # Fields:
    ID: in_id
    Диспетчер: dispatcher
    Комплектовочные Выдача: pickup_issue
    Комплектовочные Дата 1: pickup_date_1
    Комплектовочные Дата 2: pickup_date_2
    Комплектовочные Дата 3: pickup_date_3
    Отгрузочные Выдача: shipping_issue
    Отгрузочные Дата 1: shipping_date_1
    Отгрузочные Дата 2: shipping_date_2
    Отгрузочные Дата 3: shipping_date_3
    Конструкторские Выдача: design_issue
    Конструкторские Дата 1: design_date_1
    Конструкторские Дата 2: design_date_2
    Конструкторские Дата 3: design_date_3
    Изменения чертежей Выдача: drawings_issue
    Изменения чертежей Дата 1: drawings_date_1
    Изменения чертежей Дата 2: drawings_date_2
    Изменения чертежей Дата 3: drawings_date_3
    : created
    : last_updated
    """
    in_id = models.IntegerField(
        verbose_name='ID',
        # unique=True,
    )

    dispatcher = models.CharField(
        verbose_name='Диспетчер',
        max_length=255,
    )

    pickup_issue = models.BooleanField(
        verbose_name='Комплектовочные Выдача',
        blank=True,
        null=True,
    )
    pickup_date_1 = models.DateField(
        verbose_name='Комплектовочные Дата 1',
        blank=True,
        null=True,
    )
    pickup_date_2 = models.DateField(
        verbose_name='Комплектовочные Дата 2',
        blank=True,
        null=True,
    )
    pickup_date_3 = models.DateField(
        verbose_name='Комплектовочные Дата 3',
        blank=True,
        null=True,
    )

    shipping_issue = models.BooleanField(
        verbose_name='Отгрузочные Выдача',
        blank=True,
        null=True,
    )
    shipping_date_1 = models.DateField(
        verbose_name='Отгрузочные Дата 1',
        blank=True,
        null=True,
    )
    shipping_date_2 = models.DateField(
        verbose_name='Отгрузочные Дата 2',
        blank=True,
        null=True,
    )
    shipping_date_3 = models.DateField(
        verbose_name='Отгрузочные Дата 3',
        blank=True,
        null=True,
    )

    design_issue = models.BooleanField(
        verbose_name='Конструкторские Выдача',
        blank=True,
        null=True,
    )
    design_date_1 = models.DateField(
        verbose_name='Конструкторские Дата 1',
        blank=True,
        null=True,
    )
    design_date_2 = models.DateField(
        verbose_name='Конструкторские Дата 2',
        blank=True,
        null=True,
    )
    design_date_3 = models.DateField(
        verbose_name='Конструкторские Дата 3',
        blank=True,
        null=True,
    )

    drawings_issue = models.BooleanField(
        verbose_name='Изменение чертежей Выдача',
        blank=True,
        null=True,
    )
    drawings_date_1 = models.DateField(
        verbose_name='Изменение чертежей Дата 1',
        blank=True,
        null=True,
    )
    drawings_date_2 = models.DateField(
        verbose_name='Изменение чертежей Дата 2',
        blank=True,
        null=True,
    )
    drawings_date_3 = models.DateField(
        verbose_name='Изменение чертежей Дата 3',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False

    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ["in_id"]
        verbose_name = "график документации"
        verbose_name_plural = "график документации"

    def __str__(self):
        return str("%s - %s" % (self.pk, self.pk))

    def get_absolute_url(self):
        """mem_InDocument_detail"""
        return reverse("mem_InDocument_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_InDocument_update"""
        return reverse("mem_InDocument_update", args=(self.pk,))


class Waybill(models.Model):
    """Waybill
    'Документ':'document',
    'Номер':'number',
    'Дата':'date',
    'Проведен':'held',
    'ЗаказНомер':'order_no',
    'Склад':'stock',
    'ЦехПолучатель':'shop_recipient',
    'СкладПолучатель':'warehouse_recipient',
    'Номенклатура':'nomenclature',
    'ХарактеристикаНоменклатуры':'item_feature',
    'Количество':'amount',
    'ЕдиницаИзмерения':'measure',
    'Заказ':'order_no_text',
    'Ответственный':'responsible',
    'Коэффициент':'coefficient',
    'Ссылка':'link',
    """
    document = models.CharField(
        verbose_name='Документ',
        max_length=255,
        # unique=True,
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=255,
    )
    date = models.DateField(
        verbose_name='Дата',
        blank=True,
        null=True,
    )
    held = models.BooleanField(
        verbose_name='Проведен',
    )
    order_no = models.CharField(
        verbose_name='ЗаказНомер',
        max_length=255,
        blank=True,
        null=True,
    )
    stock = models.CharField(
        verbose_name='Склад',
        max_length=255,
        blank=True,
        null=True,
    )
    shop_recipient = models.CharField(
        verbose_name='ЦехПолучатель',
        max_length=255,
        blank=True,
        null=True,
    )
    warehouse_recipient = models.CharField(
        verbose_name='СкладПолучатель',
        max_length=255,
        blank=True,
        null=True,
    )
    nomenclature = models.CharField(
        verbose_name='Номенклатура',
        max_length=255,
        blank=True,
        null=True,
    )
    item_feature = models.CharField(
        verbose_name='ХарактеристикаНоменклатуры',
        max_length=255,
        blank=True,
        null=True,
    )
    amount = models.FloatField(
        verbose_name='Количество',
        null=True,
    )
    order_no_text = models.CharField(
        verbose_name='ЕдиницаИзмерения',
        max_length=255,
        blank=True,
        null=True,
    )
    measure = models.CharField(
        verbose_name='Заказ',
        max_length=255,
        blank=True,
        null=True,
    )
    responsible = models.CharField(
        verbose_name='Ответственный',
        max_length=255,
        blank=True,
        null=True,
    )
    coefficient = models.FloatField(
        verbose_name='Коэффициент',
        null=True,
        blank=True,
    )
    link = models.CharField(
        verbose_name='Ссылка',
        max_length=255,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ["date"]
        verbose_name = "накладные"
        verbose_name_plural = "накладные"

    def __str__(self):
        return str("%s - %s" % (self.number, self.order_no))

    def get_absolute_url(self):
        """mem_Waybill_detail"""
        return reverse("mem_Waybill_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_Waybill_update"""
        return reverse("mem_Waybill_update", args=(self.pk,))


class SheduleFile(models.Model):
    """
    Файлы графиков
    """
    dispatcher = models.CharField(
        verbose_name='Диспетчер',
        max_length=255,
    )
    file_path = models.CharField(
        verbose_name='Путь к файлу',
        max_length=255,
    )
    order_no = models.CharField(
        verbose_name='Заказ №',
        max_length=255,
    )
    date_creation = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        editable=False
    )
    date_modification = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now_add=True,
        editable=False
    )

    class Meta:
        ordering = ["dispatcher"]
        verbose_name = "файл графика"
        verbose_name_plural = "файл графика"

    def __str__(self):
        return str("%s - %s" % (self.dispatcher, self.order_no))

    def get_absolute_url(self):
        """mem_SheduleFile_detail"""
        return reverse("mem_SheduleFile_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_SheduleFile_update"""
        return reverse("mem_SheduleFile_update", args=(self.pk,))


class SheduleFileError(models.Model):
    """
    Файлы графиков с ошибками
    """
    dispatcher = models.CharField(
        verbose_name='Диспетчер',
        max_length=255,
    )
    file_path = models.CharField(
        verbose_name='Путь к файлу',
        max_length=255,
    )
    error = models.CharField(
        verbose_name='Заказ №',
        max_length=255,
    )

    class Meta:
        ordering = ["dispatcher"]
        verbose_name = "файл графика с ошибками"
        verbose_name_plural = "файл графика с ошибками"

    def __str__(self):
        return str("%s - %s" % (self.dispatcher, self.error))

    def get_absolute_url(self):
        """mem_SheduleFileError_detail"""
        return reverse("mem_SheduleFileError_detail", args=(self.pk,))

    def get_update_url(self):
        """mem_SheduleFileError_update"""
        return reverse("mem_SheduleFileError_update", args=(self.pk,))


class Shedule(models.Model):
    """
    Model definition for Shedule.
    'Внутренний номер': 'in_no',
    'Заказ №':'order_no',
    'Узел':'knot',
    'Наименование':'name',
    'Операция':'operation',
    'Кол-во Узел':'amount_knot',
    'Кол-во Изделие':'amount_product',
    'Кол-во Заказ':'amount_order',
    'Кол-во Массив':'amount_array',
    'Материал':'material',
    'Размер':'size',
    'Размер заготовки':'size_workpiece',
    'Росцеховка':'shop_path',
    """
    in_no = models.CharField(
        verbose_name='Внутренний номер',
        blank=True,
        null=True,
        max_length=245
    )
    order_no = models.CharField(
        verbose_name='Заказ №',
        blank=True,
        null=True,
        max_length=245
    )
    knot = models.CharField(
        verbose_name='Узел',
        blank=True,
        null=True,
        max_length=245
    )
    name = models.CharField(
        verbose_name='Наименование',
        blank=True,
        null=True,
        max_length=245
    )
    operation = models.CharField(
        verbose_name='Операция',
        blank=True,
        null=True,
        max_length=245
    )
    amount_knot = models.CharField(
        verbose_name='Кол-во Узел',
        blank=True,
        null=True,
        max_length=245
    )
    amount_product = models.CharField(
        verbose_name='Кол-во Изделие',
        blank=True,
        null=True,
        max_length=245
    )
    amount_order = models.CharField(
        verbose_name='Кол-во Заказ',
        blank=True,
        null=True,
        max_length=245
    )
    amount_array = models.CharField(
        verbose_name='Кол-во Массив',
        blank=True,
        null=True,
        max_length=245
    )
    material = models.CharField(
        verbose_name='Материал',
        blank=True,
        null=True,
        max_length=245
    )
    size = models.CharField(
        verbose_name='Размер',
        blank=True,
        null=True,
        max_length=245
    )
    size_workpiece = models.CharField(
        verbose_name='Размер заготовки',
        blank=True,
        null=True,
        max_length=245
    )
    shop_path = models.CharField(
        verbose_name='Росцеховка',
        blank=True,
        null=True,
        max_length=245
    )

    class Meta:
        """Meta definition for Shedule."""
        verbose_name = 'График'
        verbose_name_plural = 'Графики'

    def __str__(self):
        """Unicode representation of Shedule."""
        return '{}'.format(self.order_no)
