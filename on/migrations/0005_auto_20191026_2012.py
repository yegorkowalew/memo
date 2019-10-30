# Generated by Django 2.2.6 on 2019-10-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('on', '0004_auto_20191026_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couterparty',
            options={'verbose_name': 'заказчика', 'verbose_name_plural': 'заказчики'},
        ),
        migrations.AlterModelOptions(
            name='officenote',
            options={'verbose_name': 'служебную записку', 'verbose_name_plural': 'служебные записки'},
        ),
        migrations.RemoveField(
            model_name='couterparty',
            name='path',
        ),
        migrations.AddField(
            model_name='officenote',
            name='path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Путь к файлу'),
        ),
    ]
