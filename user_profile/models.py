# -*- coding: utf-8 -*-
""" Расширенная модель пользователя """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    fullname = models.CharField(
        verbose_name='Полное Ф.И.О',
        max_length=100,
        blank=True,
        null=True
    )
    fullname_small = models.CharField(
        verbose_name='Фамилия, инициалы',
        max_length=100,
        blank=True,
        null=True
    )
    user_no = models.PositiveSmallIntegerField(
        verbose_name='Номер',
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        try:
            fullname_list = self.fullname.split(' ')
            self.fullname_small = '%s %s.%s.' % (
                fullname_list[0], fullname_list[1][0], fullname_list[2][0])
        except:
            pass
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for Couterparty."""

        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        """Unicode representation of Couterparty."""
        if self.fullname:
            return '%s - %s' % (self.pk, self.fullname)
        else:
            return '%s' % self.pk


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
