# -*- coding: utf-8 -*-
""" Модели Документов """
from django.db import models
from user_profile.models import Profile
from on.models import Order

class DocumentDate(models.Model):
    """Model definition for DocumentDate."""

    DOCUMENT_TYPE_CHOICES = [
        ('pickup_fact_date', 'Комплектовочные Факт Дата'),
        ('shipping_fact_date', 'Отгрузочные Факт Дата'),
        ('design_fact_date', 'Конструкторская документация Факт Дата'),
        ('material_fact_date', 'Материалы Факт Дата'),
        ('black_metal_fact_date', 'Черный метал Факт Дата'),
        ('galvanized_fact_date', 'Оцинкованный метал Факт Дата'),
        ('cast_iron_fact_date', 'Чугун Факт Дата'),
    ]

# * Поля
    dispatcher = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )
    
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE
    )
    must = models.BooleanField(
            verbose_name='Выдаются',
            default=True,
    )
    document_type = models.CharField(
        max_length=40,
        choices=DOCUMENT_TYPE_CHOICES,
        default='pickup_fact_date',
    )
    date = models.DateField(
        verbose_name='Дата',
    )
# * Мета
    class Meta:
        """Meta definition for DocumentDate."""

        verbose_name = 'документ'
        verbose_name_plural = 'документы'

    def __str__(self):
        """Unicode representation of DocumentDate."""
        return "%s - %s - %s" % (self.dispatcher, self.order, self.document_type)
