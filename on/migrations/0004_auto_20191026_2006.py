# Generated by Django 2.2.6 on 2019-10-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('on', '0003_auto_20191026_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sn_no_amended',
            field=models.ManyToManyField(blank=True, related_name='ons', to='on.OfficeNote', verbose_name='№ СЗ с изменениями'),
        ),
    ]
