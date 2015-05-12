# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20150326_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zones',
            name='superior_zone',
            field=models.ForeignKey(blank=True, to='main_app.Zones', null=True),
            preserve_default=True,
        ),
    ]
