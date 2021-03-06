# Generated by Django 2.2.6 on 2019-10-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_note', '0010_auto_20191015_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waybill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.IntegerField(unique=True, verbose_name='Документ')),
                ('number', models.CharField(max_length=255, verbose_name='Номер')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('held', models.BooleanField(verbose_name='Проведен')),
                ('order_no', models.PositiveIntegerField(blank=True, null=True, verbose_name='ЗаказНомер')),
                ('stock', models.CharField(max_length=255, verbose_name='Склад')),
                ('shop_recipient', models.CharField(max_length=255, verbose_name='ЦехПолучатель')),
                ('warehouse_recipient', models.CharField(max_length=255, verbose_name='СкладПолучатель')),
                ('nomenclature', models.CharField(max_length=255, verbose_name='Номенклатура')),
                ('item_feature', models.CharField(blank=True, max_length=255, null=True, verbose_name='ХарактеристикаНоменклатуры')),
                ('amount', models.FloatField(null=True, verbose_name='Количество')),
                ('order_no_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='ЕдиницаИзмерения')),
                ('measure', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заказ')),
                ('responsible', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ответственный')),
                ('coefficient', models.FloatField(null=True, verbose_name='Коэффициент')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'накладные',
                'verbose_name_plural': 'накладные',
                'ordering': ['date'],
            },
        ),
        migrations.AlterModelOptions(
            name='indocument',
            options={'ordering': ['in_id'], 'verbose_name': 'график документации', 'verbose_name_plural': 'график документации'},
        ),
    ]
