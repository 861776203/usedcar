# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-22 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_orders_isdelete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '意愿表', 'verbose_name_plural': '意愿表'},
        ),
    ]
