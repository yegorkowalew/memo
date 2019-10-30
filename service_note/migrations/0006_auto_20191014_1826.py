# Generated by Django 2.2.6 on 2019-10-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_note', '0005_auto_20191014_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperativeNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_id', models.IntegerField(unique=True, verbose_name='ID')),
                ('shipment_from', models.DateField(blank=True, null=True, verbose_name='Отгрузка "от"')),
                ('shipment_before', models.DateField(blank=True, null=True, verbose_name='Отгрузка "до"')),
                ('product_name', models.CharField(max_length=255, verbose_name='Продукция')),
                ('counterparty', models.CharField(max_length=255, verbose_name='Контрагент')),
                ('order_no', models.PositiveIntegerField(blank=True, null=True, verbose_name='№ Заказа')),
                ('amount', models.FloatField(null=True, verbose_name='Кол-во')),
                ('sn_no', models.PositiveIntegerField(blank=True, null=True, verbose_name='№ СЗ')),
                ('sn_no_amended', models.CharField(blank=True, max_length=255, null=True, verbose_name='№ СЗ с изменениями')),
                ('sn_date', models.DateField(blank=True, null=True, verbose_name='Дата СЗ')),
                ('sn_date_fact', models.DateField(blank=True, null=True, verbose_name='Дата СЗ Факт')),
                ('pickup_plan_date', models.DateField(blank=True, null=True, verbose_name='Комплектовочные Дата План')),
                ('shipping_date_date', models.DateField(blank=True, null=True, verbose_name='Отгрузочные Дата План')),
                ('design_plan_date', models.DateField(blank=True, null=True, verbose_name='Конструкторская документация Дата План')),
                ('material_plan_date', models.DateField(blank=True, null=True, verbose_name='Материалы Дата План')),
                ('black_metal_plan_date', models.DateField(blank=True, null=True, verbose_name='Черный метал Дата План')),
                ('galvanized_metal_plan_date', models.DateField(blank=True, null=True, verbose_name='Оцинкованный метал Дата План')),
                ('cast_iron_plan_date', models.DateField(blank=True, null=True, verbose_name='Чугун Дата План')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'оперативную записку',
                'verbose_name_plural': 'оперативные записки',
                'ordering': ['pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='servicenote',
            options={'ordering': ['in_id'], 'verbose_name': 'служебную записку', 'verbose_name_plural': 'служебные записки'},
        ),
    ]
