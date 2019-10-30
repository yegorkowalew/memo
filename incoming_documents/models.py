# -*- coding: utf-8 -*-
""" Модели Документов """
from django.db import models


class Document(models.Model):
    """Model definition for Document."""

# * Поля
    in_id = models.IntegerField(
        verbose_name='ID',
        unique=True,
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=255)

# * Мета
    class Meta:
        """Meta definition for Document."""

        verbose_name = 'документ'
        verbose_name_plural = 'документы'

    def __str__(self):
        """Unicode representation of Document."""
        return "%s-%s" % (in_id, name)
