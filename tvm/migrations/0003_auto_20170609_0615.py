# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvm', '0002_auto_20170609_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvm',
            name='SellTimePeriod',
            field=models.IntegerField(choices=[(0, '100000-110000'), (1, '130000-140000'), (2, '093000-100000'), (3, '140000-150000')], verbose_name='开放时间'),
        ),
        migrations.AlterField(
            model_name='tvm',
            name='datetime',
            field=models.DateTimeField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tvm',
            name='name',
            field=models.IntegerField(choices=[(0, '360自行车'), (1, 'VR'), (2, '全息音效')], verbose_name='项目名称'),
        ),
    ]
