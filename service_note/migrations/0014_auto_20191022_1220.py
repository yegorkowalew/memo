# Generated by Django 2.2.6 on 2019-10-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_note', '0013_auto_20191022_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waybill',
            name='document',
            field=models.CharField(max_length=255, verbose_name='Документ'),
        ),
    ]
